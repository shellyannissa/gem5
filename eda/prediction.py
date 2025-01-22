import re
from collections import (
    defaultdict,
    deque,
)

# Filepath to the address stream file
file_path = '/home/abishek/Desktop/SHELLY/gem5/eda/addr_pc.log'

# Initialize lists to store addresses and PCs
addresses = []
pcs = []

# Read the address stream file
with open(file_path, 'r') as file:
    for line in file:
        match = re.match(r'Addr: ([0-9a-fA-F]+) PC: ([0-9a-fA-F]+)', line)
        if match:
            addr = int(match.group(1), 16)  # Convert hex address to integer
            pc = int(match.group(2), 16)    # Convert hex PC to integer
            addresses.append(addr)
            pcs.append(pc)

class ContextBasedPrefetcher:
    def __init__(self, prefetch_window, reward_function):
        self.prefetchWindow = prefetch_window
        self.rewardFunction = reward_function
        self.states = defaultdict(lambda: {'ptrs': defaultdict(int), 'counter': 0})
        self.previousAccesses = deque()
        self.prefetchQueue = deque()

    def hash(self, addr):
        return (addr >> 2) & 0x3FF  # Example hash function

    def addToState(self, key, addr):
        self.states[key]['ptrs'][addr] += 1

    def getBestAddress(self, key):
        ptrs = self.states[key]['ptrs']
        if not ptrs:
            return 0, 0  # Return 0 address and 0 reward if no pointers
        best_addr = max(ptrs, key=ptrs.get)
        reward = ptrs[best_addr]
        return best_addr, reward

    def updateScores(self, addr):
        most_seen_offsets = self.getMostSeenOffsets()  # Method to get the most seen offsets
        for index, p in enumerate(self.prefetchQueue):
            for offset in most_seen_offsets:
                target_addr = addr - offset
                if p['addr'] == target_addr:
                    distance = index  # Calculate the position in the queue
                    reward = self.rewardFunction(distance)
                    self.states[p['key']]['ptrs'][addr + offset] += reward
                    print(f'Reward: {reward}, Distance: {distance}, Addr: {addr:x}, Offset: {offset}')
                    break

        # Ensure the prefetch queue does not exceed the size of 128
        while len(self.prefetchQueue) > 128:
            self.prefetchQueue.popleft()

    def getMostSeenOffsets(self):
        # This method should return a list of the most seen offsets
        # For simplicity, let's assume it returns a static list for now
        return [ 64, 4096, 72, 48, 56, 4, 128, -8128, 1, 0, 16, 8]

    def updatePreviousAccesses(self, addr):
        self.previousAccesses.append(addr)
        if len(self.previousAccesses) > self.prefetchWindow:
            self.previousAccesses.popleft()

    def predict(self, pc, addr):
        context = pc
        for a in self.previousAccesses:
            prev_key = self.hash(a)
            self.addToState(prev_key, addr)

        key = self.hash(addr)
        best_addr, reward = 0, 0
        if key in self.states:
            best_addr, reward = self.getBestAddress(key)
            self.prefetchQueue.append({'addr': best_addr, 'key': key, 'index': len(self.prefetchQueue)})

        self.updateScores(addr)
        self.updatePreviousAccesses(addr)

        # Print the current state of the prefetch queue
        # print(f'Prefetch Queue after processing addr {addr:x}:')
        # for p in self.prefetchQueue:
            # print(f'  Addr: {p["addr"]:x}, Key: {p["key"]}, Index: {p["index"]}')

        return best_addr if key in self.states else None, reward

# Reward function example
def reward_function(distance):
    # return max(0, 60 - distance)
    return 1

# Initialize the prefetcher
prefetcher = ContextBasedPrefetcher(prefetch_window=128, reward_function=reward_function)

# Track prediction accuracy and history
predictions = []
correct_predictions = 0
reward_threshold = 0  # Define a reward threshold

# Feed data to the algorithm
k = 0
block_size = 64  # Define the block size
for pc, addr in zip(pcs, addresses):
    prediction, reward = prefetcher.predict(pc, addr)
    if reward >= reward_threshold:
        predictions.append((pc, addr, prediction))
        if any((p['addr'] // block_size) == (addr // block_size) for p in prefetcher.prefetchQueue):
            correct_predictions += 1
    k += 1

# Calculate accuracy
accuracy = correct_predictions / len(predictions) if predictions else 0

# Print results
print(f'Prediction Accuracy: {accuracy * 100:.2f}%')
print(len(predictions), 'predictions made')
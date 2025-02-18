#include "mem/cache/prefetch/context_based_prefetcher.hh"
#include "debug/HWPrefetch.hh"
#include "params/ContextBasedPrefetcher.hh"
#include <cmath>
#include <numeric> // Include for std::accumulate

namespace gem5
{

namespace prefetch
{

ContextBasedPrefetcher::ContextBasedPrefetcher(const ContextBasedPrefetcherParams &p)
    : Queued(p),
      prefetchWindow(p.prefetch_window),
      rewardFunction(p.target_prefetch_distance, p.prefetch_window),
      rewardThreshold(60), // Initial reward threshold
      confidenceThreshold(10) // Initial confidence threshold
{
    // Initialize the most seen offsets (as in Python script)
    mostSeenOffsets = {1, 8, -8, 0, -16, 16, 4, -24, 176, -96};

    // Open the log file
    logFile.open("/home/abishek/Desktop/SHELLY/gem5/eda/addr.log");
    if (!logFile.is_open()) {
        fatal("Unable to open log file: /home/abishek/Desktop/SHELLY/gem5/eda/addr.log");
    }
}

void
ContextBasedPrefetcher::calculatePrefetch(const PrefetchInfo &pfi,
                                          std::vector<AddrPriority> &addresses,
                                          const CacheAccessor &cache)
{
    Addr addr = pfi.getAddr();
    int pc = pfi.getPC(); // Use PC as context
    int key = hash(addr, pc);

    // Log the address
    logFile << "Addr: " << std::hex << addr << std::endl;

    // Data collection: Update state with previous accesses
    for (Addr a : previousAccesses) {
        int prev_key = hash(a, pc);
        addToState(prev_key, addr);
    }

    // Prediction: Get the best address for the current context
    if (states.find(key) != states.end()) {
        Addr best_addr = getBestAddress(key);
        prefetchQueue.push_back({best_addr, key, (int)prefetchQueue.size()});
    }

    // Feedback: Update scores based on prefetch queue
    updateScores(addr);

    // Send prefetch: Add the best address to the prefetch queue if it exceeds the confidence threshold
    if (!prefetchQueue.empty()) {
        Addr next_pref = prefetchQueue.front().addr;
        prefetchQueue.pop_front();
        if (states[key].ptrs[next_pref] >= confidenceThreshold) {
            addresses.push_back(AddrPriority(next_pref, 0));
            DPRINTF(HWPrefetch, "Generated prefetch %#lx\n", next_pref);
        }
    }

    // Update previous accesses
    updatePreviousAccesses(addr);

    // Update reward threshold
    updateRewardThreshold();

    // Update offsets dynamically
    updateOffsets();
}

void
ContextBasedPrefetcher::notifyFill(const CacheAccessProbeArg &arg)
{
    // Implement if needed
}

int
ContextBasedPrefetcher::hash(Addr addr, int pc) const
{
    // Improved hash function
    int hash_value = (addr >> 2) & 0x3FF;  // Use lower bits of address
    hash_value ^= (pc & 0x3FF);            // XOR with lower bits of PC
    hash_value *= 2654435761;              // Multiply by a large prime for better mixing
    hash_value &= 0x3FF;                   // Keep the result within a 10-bit range
    return hash_value;
}

void
ContextBasedPrefetcher::addToState(int key, Addr addr)
{
    if (states.find(key) == states.end()) {
        states[key] = State();
    }
    states[key].ptrs[addr]++;
}

Addr
ContextBasedPrefetcher::getBestAddress(int key) const
{
    const auto &ptrs = states.at(key).ptrs;
    if (ptrs.empty()) {
        return 0; // Handle case where there are no addresses
    }
    return std::max_element(ptrs.begin(), ptrs.end(),
                            [](const auto &a, const auto &b) {
                                return a.second < b.second;
                            })->first;
}

void
ContextBasedPrefetcher::updateScores(Addr addr)
{
    for (auto &p : prefetchQueue) {
        for (int offset : mostSeenOffsets) {
            Addr target_addr = addr - offset;
            if (p.addr == target_addr) {
                int distance = p.index; // Distance is the position in the queue
                int reward = rewardFunction(distance);
                states[p.key].ptrs[addr + offset] += reward;
                DPRINTF(HWPrefetch, "Reward: %d, Distance: %d, Addr: %#lx, Offset: %d\n",
                        reward, distance, addr, offset);

                // Track offset frequencies
                offsetFrequencies[offset]++;
                break;
            }
        }
    }

    // Ensure the prefetch queue does not exceed the size of 128
    while (prefetchQueue.size() > 128) {
        prefetchQueue.pop_front();
    }
}

void
ContextBasedPrefetcher::updatePreviousAccesses(Addr addr)
{
    previousAccesses.push_back(addr);
    if (previousAccesses.size() > prefetchWindow) {
        previousAccesses.pop_front();
    }
}

std::vector<int>
ContextBasedPrefetcher::getMostSeenOffsets() const
{
    // Return the most seen offsets (as in Python script)
    return mostSeenOffsets;
}

void
ContextBasedPrefetcher::updateRewardThreshold()
{
    if (rewards.size() > 0) {
        int mean_reward = std::accumulate(rewards.begin(), rewards.end(), 0) / rewards.size();
        rewardThreshold = mean_reward * 1.5; // Adjust multiplier as needed
    }
}

void
ContextBasedPrefetcher::updateOffsets()
{
    // Update the most seen offsets based on observed frequencies
    std::vector<std::pair<int, int>> freq_vector(offsetFrequencies.begin(), offsetFrequencies.end());
    std::sort(freq_vector.begin(), freq_vector.end(), [](const auto &a, const auto &b) {
        return a.second > b.second;
    });

    mostSeenOffsets.clear();
    for (const auto &pair : freq_vector) {
        mostSeenOffsets.push_back(pair.first);
        if (mostSeenOffsets.size() >= 10) {
            break; // Limit to top 10 offsets
        }
    }
}

} // namespace prefetch
} // namespace gem5
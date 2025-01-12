import matplotlib.pyplot as plt

# Filepath to the log file
log_file_path = '/home/abishek/Desktop/SHELLY/gem5/eda/addresses.log'

# Specify the start and end index of lines to be considered
start_index = 1000
end_index = 2000

# Initialize lists to store time and addresses
times = []
addresses = []

# Read the log file
with open(log_file_path, 'r') as file:
    for i, line in enumerate(file):
        if i < start_index:
            continue
        if i >= end_index:
            break
        if line.startswith('Miss:'):
            parts = line.split()
            address = int(parts[1], 16)  # Convert hex address to integer
            addresses.append(address)
            times.append(i)  # Use the line number as the time

# Plot the addresses as a time series
plt.figure(figsize=(10, 6))
plt.plot(times, addresses, marker='o', linestyle='-', color='b')
plt.xlabel('Time')
plt.ylabel('Address')
plt.title('Addresses as a Time Series')
plt.grid(True)
plt.show()
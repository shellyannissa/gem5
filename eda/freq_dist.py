import matplotlib.pyplot as plt

# Filepath to the log file
log_file_path = '/home/abishek/Desktop/SHELLY/gem5/eda/addresses.log'

# Initialize a list to store addresses
addresses = []

# Read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        if line.startswith('Miss:'):
            parts = line.split()
            address = int(parts[1], 16)  # Convert hex address to integer
            addresses.append(address)

# Plot the frequency distribution of the addresses
plt.figure(figsize=(10, 6))
plt.hist(addresses, bins=50, color='blue', edgecolor='black')
plt.xlabel('Address')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Addresses')
plt.grid(True)
plt.show()
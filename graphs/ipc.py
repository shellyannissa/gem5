import matplotlib.pyplot as plt
import numpy as np

# import list called data from data.py
from data import data

# Extract benchmark names and prefetcher names
benchmarks = [benchmark["name"] for benchmark in data]
prefetcher_names = [prefetcher["name"] for prefetcher in data[0]["prefetchers"]]

# Extract ipc data and normalize with base ipc
ipc_data = {prefetcher: [] for prefetcher in prefetcher_names}
for benchmark in data:
    base_ipc = benchmark["base"]["ipc"]
    for prefetcher in benchmark["prefetchers"]:
        normalized_ipc = prefetcher["ipc"] / base_ipc
        ipc_data[prefetcher["name"]].append(normalized_ipc)

# Plotting
x = np.arange(len(benchmarks))  # the label locations
width = 0.2  # the width of the bars
benchmark_gap = 0.3  # the gap between different benchmarks

fig, ax = plt.subplots(figsize=(12, 8))

# Create bars for each prefetcher
for i, prefetcher in enumerate(prefetcher_names):
    ax.bar(x * (len(prefetcher_names) * width + benchmark_gap) + i * width, ipc_data[prefetcher], width, label=prefetcher)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Benchmarks')
ax.set_ylabel('Normalized ipc')
ax.set_title('Speedup using IPC by Prefetcher and Benchmark')
ax.set_xticks(x * (len(prefetcher_names) * width + benchmark_gap) + (len(prefetcher_names) - 1) * width / 2)
ax.set_xticklabels(benchmarks)
# ax.set_ylim(0, 1.2)  # Set y-axis limit to 1.2 for better visualization
ax.legend(fontsize='xx-large')  # Make the legend even bigger

fig.tight_layout()

plt.show()

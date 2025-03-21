import json
import os

# Define the required stats keys
STAT_KEYS = {
    "instructions": "simInsts",
    "accuracy": "system.l2.prefetcher.accuracy",
    "coverage": "system.l2.prefetcher.coverage",
    "pfIssued": "system.l2.prefetcher.pfIssued",
    "pfUseful": "system.l2.prefetcher.pfUseful",
    "pfHitInCache": "system.l2.prefetcher.pfHitInCache",
    "pfLate": "system.l2.prefetcher.pfLate",
    "cpi": "system.switch_cpus_1.cpi",
    "ipc": "system.switch_cpus_1.ipc",
    "misses": "system.l2.prefetcher.demandMshrMisses"
}

STAT_KEYS_BASE = {
    "instructions": "simInsts",
    "cpi": "system.switch_cpus_1.cpi",
    "ipc": "system.switch_cpus_1.ipc",
    "misses": "system.l2.demandMisses::total"
}

# Template structure
benchmarks = ["astar", "bzip2", "gobmk", "lbm", "libquantum", "mcf", "namd", "omnetpp"]
prefetchers = ["context", "stride", "bop", "signature", "indirect", "tagged"]

# Base JSON structure
data = []
for benchmark in benchmarks:
    entry = {
        "name": benchmark,
        "base": {},
        "prefetchers": []
    }

    stats_path = f"stats/{benchmark}/none/stats.txt"
    if not os.path.exists(stats_path):
        print(f"Warning: {stats_path} not found. Skipping...")
        continue
    
    # Read the stats file and extract required values
    extracted_stats = {}
    with open(stats_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) < 2:
                continue
            key, value = parts[0], parts[1]
            for stat_name, stat_key in STAT_KEYS_BASE.items():
                if key == stat_key:
                    extracted_stats[stat_name] = float(value)

    entry["base"] = {
        "instructions": extracted_stats.get("instructions", 0),
        "cpi": extracted_stats.get("cpi", 1),
        "ipc": extracted_stats.get("ipc", 1),
        "misses": extracted_stats.get("misses", 0),
        "mpki": extracted_stats.get("misses", 0) / extracted_stats.get("instructions", 1) * 1000
    }
    
    # Process each prefetcher
    for prefetcher in prefetchers:
        stats_path = f"stats/{benchmark}/{prefetcher}/stats.txt"
        if not os.path.exists(stats_path):
            print(f"Warning: {stats_path} not found. Skipping...")
            continue
        
        # Read the stats file and extract required values
        extracted_stats = {}
        with open(stats_path, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) < 2:
                    continue
                key, value = parts[0], parts[1]
                for stat_name, stat_key in STAT_KEYS.items():
                    if key == stat_key:
                        # check for nan values
                        if value == "nan":
                            value = 0
                        extracted_stats[stat_name] = float(value)
        
        # Ensure all required values exist, otherwise use defaults
        prefetcher_entry = {
            "name": prefetcher,
            "instructions": extracted_stats.get("instructions", 0),
            "accuracy": extracted_stats.get("accuracy", 0) * 100,
            "coverage": extracted_stats.get("coverage", 0) * 100,
            "pfIssued": extracted_stats.get("pfIssued", 0),
            "pfUseful": extracted_stats.get("pfUseful", 0),
            "pfHitInCache": extracted_stats.get("pfHitInCache", 0),
            "pfLate": extracted_stats.get("pfLate", 0),
            "cpi": extracted_stats.get("cpi", 1),
            "ipc": extracted_stats.get("ipc", 1),
            "misses": extracted_stats.get("misses", 0),
            "speedup": extracted_stats.get("ipc", 1) / entry["base"]["ipc"],
            "mpki": extracted_stats.get("misses", 0) / extracted_stats.get("instructions", 1) * 1000
        }

        entry["prefetchers"].append(prefetcher_entry)

    data.append(entry)

# Write the extracted data to JSON file
output_file = "output.json"
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Generated {output_file} successfully!")

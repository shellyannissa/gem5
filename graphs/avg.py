# go through the output.json file and find the avg of each prefetcher
# [
#     {
#         "name": "astar",
#         "base": {
#             "instructions": 1560004.0,
#             "cpi": 1.046761,
#             "ipc": 0.955328,
#             "misses": 7418.0,
#             "mpki": 4.755116012523044
#         },
#         "prefetchers": [
#             {
#                 "name": "context",
#                 "instructions": 1560004.0,
#                 "accuracy": 48.9689,
#                 "coverage": 36.8299,
#                 "pfIssued": 5528.0,
#                 "pfUseful": 2707.0,
#                 "pfHitInCache": 1966.0,
#                 "pfLate": 2034.0,
#                 "cpi": 0.892921,
#                 "ipc": 1.11992,
#                 "misses": 4643.0,
#                 "speedup": 1.1722884705567094,
#                 "mpki": 2.97627441980918
#             },

# average of accuracy and coverage

import json
import os

import numpy as np

# Define the keys for the stats we want to extract

# read the data from the JSON file
def get_data_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def get_average(prefetcher, metric):
    data = get_data_from_json("output.json")
    sum = 0
    count = 0

    for entry in data:
        if metric == "misses" or metric == "ipc":
            base = entry["base"][metric]
        for prefetcher_entry in entry["prefetchers"]:
            if prefetcher_entry["name"] == prefetcher:
                # print(prefetcher_entry[metric])
                # print(base)
                if metric == "misses" or metric == "ipc":
                    prefetcher_entry[metric] = prefetcher_entry[metric] / base
                print(prefetcher_entry[metric])
                sum += prefetcher_entry[metric]
                count += 1
                break

    avg =  sum / count if count > 0 else 0

    return avg

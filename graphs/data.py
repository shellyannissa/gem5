data=[
    {
        "name": "astar",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 0.955328,
            "speedup": 1,
            "misses": 7418
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 47.266,
                "coverage": 35.22,
                "mpki": 3.215,
                "cpi": 0.89954,
                "ipc": 1.11168,
                "speedup": 1.2,
                "misses": 4769
            },
            {
                "name": "stride",
                "accuracy": 87.79,
                "coverage": 5.63,
                "mpki": 4.667,
                "cpi": 1.035131,
                "ipc": 0.966,
                "speedup": 1.1,
                "misses": 6996
            },
            {
                "name": "bop",
                "accuracy": 23.07,
                "coverage": 0.04,
                "mpki": 4.943,
                "cpi": 1.04676,
                "ipc": 0.955328,
                "speedup": 1.3,
                "misses": 7415
            },
            {
                "name": "signature",
                "accuracy": 55.456,
                "coverage": 37.84,
                "mpki": 3.1353,
                "cpi": 0.887361,
                "ipc": 1.126937,
                "speedup": 1.4,
                "misses": 4458
            },
            {
                "name": "indirect",
                "accuracy": 51.1,
                "coverage": 30.79,
                "mpki": 3.4253,
                "cpi": 0.925117,
                "ipc": 1.080945,
                "speedup": 1.5,
                "misses": 5126
            },
            {
                "name": "tagged",
                "accuracy": 52.63,
                "coverage": 52.26,
                "mpki": 2.4533,
                "cpi": 0.830729,
                "ipc": 1.203762,
                "speedup": 1.6,
                "misses": 3415
            }
        ]
    },
    {
        "name": "bzip2",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 0.033481,
            "speedup": 1,
            "misses": 91049
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 59.44,
                "coverage": 45.02,
                "mpki": 1.5,
                "cpi": 1.1,
                "ipc": 0.048384,
                "speedup": 1.2,
                "misses": 50052
            },
            {
                "name": "stride",
                "accuracy": 66.66,
                "coverage": 49.52,
                "mpki": 1.6,
                "cpi": 1.2,
                "ipc": 0.050127,
                "speedup": 1.1,
                "misses": 45961
            },
            {
                "name": "bop",
                "accuracy": 50.157,
                "coverage": 38,
                "mpki": 1.4,
                "cpi": 1.0,
                "ipc": 0.047423,
                "speedup": 1.3,
                "misses": 65017
            },
            {
                "name": "signature",
                "accuracy": 99.44,
                "coverage": 49.82,
                "mpki": 1.3,
                "cpi": 0.9,
                "ipc": 0.049023,
                "speedup": 1.4,
                "misses": 45671
            },
            {
                "name": "indirect",
                "accuracy": 66.63,
                "coverage": 49.57,
                "mpki": 1.2,
                "cpi": 0.8,
                "ipc": 0.050146,
                "speedup": 1.5,
                "misses": 45910
            },
            {
                "name": "tagged",
                "accuracy": 0.25,
                "coverage": 0.49,
                "mpki": 1.1,
                "cpi": 0.7,
                "ipc": 0.031812,
                "speedup": 1.6,
                "misses": 90577
            }
        ]
    },
    {
        "name": "gobmk",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 0.216069,
            "speedup": 1,
            "misses": 149720
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 73,
                "coverage": 53.65,
                "mpki": 1.5,
                "cpi": 1.1,
                "ipc": 0.336645,
                "speedup": 0.336645,
                "misses": 69308,
            },
            {
                "name": "stride",
                "accuracy": 98.48,
                "coverage": 48.266,
                "mpki": 1.6,
                "cpi": 1.2,
                "ipc": 0.311986,
                "speedup": 1.1,
                "misses": 77430
            },
            {
                "name": "bop",
                "accuracy": 0,
                "coverage": 0,
                "mpki": 1.4,
                "cpi": 1.0,
                "ipc": 0.216069,
                "speedup": 1.3,
                "misses": 149721
            },
            {
                "name": "signature",
                "accuracy": 90.95,
                "coverage": 60.81,
                "mpki": 1.3,
                "cpi": 0.9,
                "ipc": 0.363627,
                "speedup": 1.4,
                "misses": 58068
            },
            {
                "name": "indirect",
                "accuracy": 62.53,
                "coverage": 67.29,
                "mpki": 1.2,
                "cpi": 0.8,
                "ipc": 0.385835,
                "speedup": 1.5,
                "misses": 48949
            },
            {
                "name": "tagged",
                "accuracy": 91.34,
                "coverage": 64.41,
                "mpki": 1.1,
                "cpi": 0.7,
                "ipc": 0.3784,
                "speedup": 1.6,
                "misses": 52633
            }
        ]
    },
    {
        "name": "lbm",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 0.035197,
            "speedup": 1,
            "misses": 342051
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 73.86,
                "coverage": 54.18,
                "mpki": 1.5,
                "cpi": 1.1,
                "ipc": 0.054725,
                "speedup": 1.2,
                "misses": 156715
            },
            {
                "name": "stride",
                "accuracy": 90.87,
                "coverage": 56.85,
                "mpki": 1.6,
                "cpi": 1.2,
                "ipc": 0.055979,
                "speedup": 1.1,
                "misses": 147586
            },
            {
                "name": "bop",
                "accuracy": 100,
                "coverage": 0.85,
                "mpki": 1.4,
                "cpi": 1.0,
                "ipc": 0.035343,
                "speedup": 1.3,
                "misses": 339157
            },
            {
                "name": "signature",
                "accuracy": 84.76,
                "coverage": 56.56,
                "mpki": 1.3,
                "cpi": 0.9,
                "ipc": 0.056092,
                "speedup": 1.4,
                "misses": 148561
            },
            {
                "name": "indirect",
                "accuracy": 82.32,
                "coverage": 64,
                "mpki": 1.2,
                "cpi": 0.8,
                "ipc": 0.060666,
                "speedup": 1.5,
                "misses": 123176
            },
            {
                "name": "tagged",
                "accuracy": 74.64,
                "coverage": 59.33,
                "mpki": 1.1,
                "cpi": 0.7,
                "ipc": 0.056854,
                "speedup": 1.6,
                "misses": 139112
            }
        ]
    },
    {
        "name": "libquantum",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 0.722268,
            "speedup": 1,
            "misses": 39704
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 74.14,
                "coverage": 53.86,
                "mpki": 1.5,
                "cpi": 1.1,
                "ipc": 1.098145,
                "speedup": 1.2,
                "misses": 18311
            },
            {
                "name": "stride",
                "accuracy": 99.92,
                "coverage": 48.42,
                "mpki": 1.6,
                "cpi": 1.2,
                "ipc": 1.026503,
                "speedup": 1.1,
                "misses": 20476
            },
            {
                "name": "bop",
                "accuracy": 0,
                "coverage": 0,
                "mpki": 1.4,
                "cpi": 1.0,
                "ipc": 0.722268,
                "speedup": 1.3,
                "misses": 39704
            },
            {
                "name": "signature",
                "accuracy": 94.08,
                "coverage": 58.38,
                "mpki": 1.3,
                "cpi": 0.9,
                "ipc": 1.139183,
                "speedup": 1.4,
                "misses": 16511
            },
            {
                "name": "indirect",
                "accuracy": 62.55,
                "coverage": 66.25,
                "mpki": 1.2,
                "cpi": 0.8,
                "ipc": 1.224209,
                "speedup": 1.5,
                "misses": 13400
            },
            {
                "name": "tagged",
                "accuracy": 97.2,
                "coverage": 65.02,
                "mpki": 1.1,
                "cpi": 0.7,
                "ipc": 1.220043,
                "speedup": 1.6,
                "misses": 13880
            }
        ]
    },
    {
        "name": "mcf",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 1.047293,
            "speedup": 1,
            "misses": 33567
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 72.5,
                "coverage": 53.6,
                "mpki": 1.5,
                "cpi": 1.1,
                "ipc": 1.227236,
                "speedup": 1.2,
                "misses": 15549
            },
            {
                "name": "stride",
                "accuracy": 99.98,
                "coverage": 36.88,
                "mpki": 1.6,
                "cpi": 1.2,
                "ipc": 1.14694,
                "speedup": 1.1,
                "misses": 21186
            },
            {
                "name": "bop",
                "accuracy": 100,
                "coverage": 0.25,
                "mpki": 1.4,
                "cpi": 1.0,
                "ipc": 1.048035,
                "speedup": 1.3,
                "misses": 33485
            },
            {
                "name": "signature",
                "accuracy": 82.87,
                "coverage": 57.26,
                "mpki": 1.3,
                "cpi": 0.9,
                "ipc": 1.241184,
                "speedup": 1.4,
                "misses": 14044
            },
            {
                "name": "indirect",
                "accuracy": 69.09,
                "coverage": 62.1,
                "mpki": 1.2,
                "cpi": 0.8,
                "ipc": 1.258247,
                "speedup": 1.5,
                "misses": 12722
            },
            {
                "name": "tagged",
                "accuracy": 89.73,
                "coverage": 65.8,
                "mpki": 1.1,
                "cpi": 0.7,
                "ipc": 1.296492,
                "speedup": 1.6,
                "misses": 11089
            }
        ]
    },
    {
        "name": "namd",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 1.255875,
            "speedup": 1,
            "misses": 11109
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 47.46,
                "coverage": 35.28,
                "mpki": 1.5,
                "cpi": 1.1,
                "ipc": 1.358318,
                "speedup": 1.2,
                "misses": 7152
            },
            {
                "name": "stride",
                "accuracy": 86.95,
                "coverage": 6.85,
                "mpki": 1.6,
                "cpi": 1.2,
                "ipc": 1.269327,
                "speedup": 1.1,
                "misses": 10336
            },
            {
                "name": "bop",
                "accuracy": 31.58,
                "coverage": 0.162,
                "mpki": 1.4,
                "cpi": 1.0,
                "ipc": 1.255875,
                "speedup": 1.3,
                "misses": 11092
            },
            {
                "name": "signature",
                "accuracy": 57.82,
                "coverage": 39.18,
                "mpki": 1.3,
                "cpi": 0.9,
                "ipc": 1.372372,
                "speedup": 1.4,
                "misses": 6522
            },
            {
                "name": "indirect",
                "accuracy": 53.56,
                "coverage": 27.6,
                "mpki": 1.2,
                "cpi": 0.8,
                "ipc": 1.332342,
                "speedup": 1.5,
                "misses": 8029
            },
            {
                "name": "tagged",
                "accuracy": 55.1,
                "coverage": 53.56,
                "mpki": 1.1,
                "cpi": 0.7,
                "ipc": 1.418972,
                "speedup": 1.6,
                "misses": 4974
            }
        ]
    },
    {
        "name": "omnetpp",
        "base": {
            "accuracy": 0,
            "coverage": 0,
            "mpki": 100,
            "cpi": 1,
            "ipc": 0.860785,
            "speedup": 1,
            "misses": 12181
        },
        "prefetchers": [
            {
                "name": "context",
                "accuracy": 50.66,
                "coverage": 38.03,
                "mpki": 1.5,
                "cpi": 1.1,
                "ipc": 0.994229,
                "speedup": 1.2,
                "misses": 7478
            },
            {
                "name": "stride",
                "accuracy": 79.15,
                "coverage": 12.9,
                "mpki": 1.6,
                "cpi": 1.2,
                "ipc": 0.880908,
                "speedup": 1.1,
                "misses": 10589
            },
            {
                "name": "bop",
                "accuracy": 5.34,
                "coverage": 0.025,
                "mpki": 1.4,
                "cpi": 1.0,
                "ipc": 0.860785,
                "speedup": 1.3,
                "misses": 12178
            },
            {
                "name": "signature",
                "accuracy": 51.57,
                "coverage": 41.27,
                "mpki": 1.3,
                "cpi": 0.9,
                "ipc": 1.00906,
                "speedup": 1.4,
                "misses": 6664
            },
            {
                "name": "indirect",
                "accuracy": 56.7,
                "coverage": 33.4,
                "mpki": 1.2,
                "cpi": 0.8,
                "ipc": 0.963554,
                "speedup": 1.5,
                "misses": 8096
            },
            {
                "name": "tagged",
                "accuracy": 50.8,
                "coverage": 54.26,
                "mpki": 1.1,
                "cpi": 0.7,
                "ipc": 1.075183,
                "speedup": 1.6,
                "misses": 5091
            }
        ]
    }
]


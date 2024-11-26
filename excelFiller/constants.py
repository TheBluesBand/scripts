# List of TimeIDs
TIME_IDS = [f'T{i}' for i in range(1, 10)]

# List of TeamIDs
TEAM_IDS = [f'TM{i}' for i in range(1, 7)]

# List of AreaIDs
AREA_IDS = [f'AR{i}' for i in range(1, 5)]

# List of MetricIDs (example)
METRIC_IDS = [f'M{i:03}' for i in range(1, 12)]

# Dictionary of Metric Values, Scores, and Weights
metric_ranges = {
    'M001': {'value': (0, 50), 'score': [1, 2], 'weight': 1},
    'M002': {'value': (-100, 100), 'score': [1, 2, 3], 'weight': 1},
    'M003': {'value': (20, 70), 'score': [1, 2, 3], 'weight': 1},
    'M004': {'value': (0, 100), 'score': [1, 2, 3], 'weight': 1},
    'M005': {'value': (0, 10), 'score': [1, 2, 3], 'weight': 3},
    'M006': {'value': (0, 100), 'score': [1, 2, 3], 'weight': 1},
    'M007': {'value': (0, 100), 'score': [1, 2, 3], 'weight': 1},
    'M008': {'value': (1, 5), 'score': [1, 2, 3], 'weight': 1},
    'M009': {'value': ['No Critical/High/Med Issues', 'Medium Issues, No Critical/High', 'Otherwise'], 'score': [3, 2, 1], 'weight': 2},
    'M010': {'value': (0, 100), 'score': [1, 2, 3], 'weight': 1},
    'M011': {'value': (0, 100), 'score': [1, 2, 3], 'weight': 1},
}
import random

def generate_area_facts_data(time_ids, team_ids, area_ids):
    """
    Generate mock data for area facts.

    Args:
        time_ids (list): List of TimeIDs.
        team_ids (list): List of TeamIDs.
        area_ids (list): List of AreaIDs.

    Returns:
        dict: A dictionary containing the generated data with keys 'AreaID', 'TimeID', 'TeamID', 'WeightedScore', and 'MaxScore'.
    """
    # Initialize lists to store the data
    area_list = []          # List of AreaIDs
    time_list = []          # List of TimeIDs
    team_list = []          # List of TeamIDs
    weighted_scores = []    # List of weighted scores
    max_scores = []         # List of max scores

    # Generate data by iterating through each combination of time, team, and area
    for time_id in time_ids:
        for team_id in team_ids:
            for area_id in area_ids:
                area_list.append(area_id)
                time_list.append(time_id)
                team_list.append(team_id)
                weighted_scores.append(random.randint(0, 10))  # Random weighted score between 0 and 10
                max_scores.append(10)

    # Return the generated data as a dictionary
    return {
        'AreaID': area_list,
        'TimeID': time_list,
        'TeamID': team_list,
        'WeightedScore': weighted_scores,
        'MaxScore': max_scores,
    }

def generate_metric_facts_data(time_ids, team_ids):
    """
    Generate mock data for metric facts.

    Args:
        time_ids (list): List of TimeIDs.
        team_ids (list): List of TeamIDs.

    Returns:
        dict: A dictionary containing the generated data with keys 'Entry', 'MetricID', 'TimeID', 'TeamID', 'Value', 'Score', and 'WeightedScore'.
    """

    # Initialize lists to store the data
    entry_ids = []          # List of EntryIDs
    metric_ids = []          # List of MetricIDs
    time_ids = []          # List of TimeIDs
    team_ids = []          # List of TeamIDs
    values = []    # List of Values
    scores = []         # List of Scores
    weighted_scores = []         # List of Weight

    for time_id in time_ids:
        for team_id in team_ids:
            for metric_id in metric_ids:
                entry_ids.append(f'{time_id}_{team_id}_{metric_id}')
                metric_ids.append(metric_id)
                time_ids.append(time_id)
                team_ids.append(team_id)
                values.append(random.randint(0, 100))
                scores.append(random.randint(0, 10))
                weighted_scores.append(random.randint(0, 10))

    # Return the generated data as a dictionary
    return {
        'Entry': entry_ids,
        'MetricID': metric_ids,
        'TimeID': time_ids,
        'TeamID': team_ids,
        'Value': values,
        'Score': scores,
        'WeightedScore': weighted_scores,
    }
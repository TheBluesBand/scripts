import random

from constants import METRIC_IDS, TEAM_IDS, TIME_IDS
from datetime import datetime, timedelta

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

def calculate_score(metric_id, value):
    """
    Calculate the score based on the metric ID and value.

    Args:
        metric_id (str): The metric ID.
        value (float): The value for which the score needs to be calculated.

    Returns:
        int: The calculated score.
    """
    if metric_id == "M001":
        return 2 if value < 30 else 1
    elif metric_id == "M002":
        if value >= 0:
            return 3
        elif value >= -0.05:
            return 2
        else:
            return 1
    elif metric_id == "M003":
        if value > 0.25:
            return 1
        elif value > 0.1:
            return 2
        else:
            return 3
    elif metric_id == "M004":
        if value > 0.75:
            return 3
        elif value >= 0.25:
            return 2
        else:
            return 1
    elif metric_id == "M005":
        if value == 0:
            return 3
        elif value <= 5:
            return 2
        else:
            return 1
    elif metric_id == "M006":
        if value > 0.8:
            return 3
        elif value >= 0.6:
            return 2
        else:
            return 1
    elif metric_id == "M007":
        if value > 0.8:
            return 3
        elif value >= 0.6:
            return 2
        else:
            return 1
    elif metric_id == "M008":
        if value > 4:
            return 3
        elif value > 3:
            return 2
        else:
            return 1
    elif metric_id == "M009":
        if value >= 3:
            return 3
        elif value == 2:
            return 2
        else:
            return 1
    elif metric_id == "M010":
        if value > 0.85:
            return 3
        elif value > 0.75:
            return 2
        else:
            return 1
    elif metric_id == "M011":
        if value < 0.1:
            return 3
        elif value < 0.15:
            return 2
        else:
            return 1
    else:
        return 0

def generate_metric_facts_data():
    """
    Generate mock data for metric facts.

    Returns:
        dict: A dictionary containing the generated data with keys 'Entry', 'MetricID', 'TimeID', 'TeamID', 'Value', and 'Score'.
    """

    # Initialize lists to store the data
    entry_ids = []          # List of EntryIDs
    metric_ids = []         # List of MetricIDs
    time_ids = []           # List of TimeIDs
    team_ids = []           # List of TeamIDs
    value = []             # List of Weights
    scores = []             # List of Values
    weight = []             # List of Scores

    counter = 1

    for time_id in TIME_IDS:
        for team_id in TEAM_IDS:
            for metric_id in METRIC_IDS:
                entry_ids.append(counter)
                counter += 1
                metric_ids.append(metric_id)
                time_ids.append(time_id)
                team_ids.append(team_id)
                temp_value = random.uniform(0.1, 12.0)
                value.append(temp_value)
                scores.append(calculate_score(metric_id, temp_value))
                weight.append(random.randint(2, 10))

    # Return the generated data as a dictionary
    return {
        'EntryID': entry_ids,
        'MetricID': metric_ids,
        'TimeID': time_ids,
        'TeamID': team_ids,
        'Value': value,
        'Score': scores,
        'Weight': weight,
    }

def generate_time_dim(year):
    """
    Generate TimeDim data for an entire year.

    Args:
        year (int): The year for which to generate the data.

    Returns:
        dict: A dictionary containing the generated data with keys 'TimeID', 'Date', 'Month', 'Quarter', and 'Year'.
    """
    time_ids = []
    dates = []
    months = []
    quarters = []
    years = []

    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    current_date = start_date
    index = 1

    while current_date <= end_date:
        time_ids.append(f'T{index}')
        index += 1
        dates.append(current_date.strftime('%d/%m/%Y'))
        months.append(current_date.strftime('%B'))
        quarters.append(f'Q{(current_date.month - 1) // 3 + 1}')
        years.append(current_date.year)
        current_date += timedelta(days=1)

    return {
        'TimeID': time_ids,
        'Date': dates,
        'Month': months,
        'Quarter': quarters,
        'Year': years,
    }
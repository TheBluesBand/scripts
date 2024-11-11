import pandas as pd
import random
import logging

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

def export_to_excel(data, filename):
    """
    Export data to an Excel file.

    Args:
        data (dict): The data to be exported, in dictionary format.
        filename (str): The name of the output Excel file.

    Returns:
        None
    """
    try:
        # Create a DataFrame from the data dictionary
        df = pd.DataFrame(data)
        # Export the DataFrame to an Excel file
        df.to_excel(filename, index=False)
        logging.info(f"Data has been exported to {filename}")
    except Exception as e:
        # Log an error message if the export fails
        logging.error(f"Failed to export data to Excel: {e}")

def main(time_ids, team_ids, area_ids, output_file):
    """
    Main function to generate data and export it to an Excel file.

    Args:
        time_ids (list): List of TimeIDs.
        team_ids (list): List of TeamIDs.
        area_ids (list): List of AreaIDs.
        output_file (str): The name of the output Excel file.

    Returns:
        None
    """
    # Generate the data
    data = generate_area_facts_data(time_ids, team_ids, area_ids)
    # Export the generated data to an Excel file
    export_to_excel(data, output_file)

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    time_ids = [f'T{i}' for i in range(1, 10)]  # List of TimeIDs (T1 to T9)
    team_ids = [f'TM{i}' for i in range(1, 8)]  # List of TeamIDs (TM1 to TM7)
    area_ids = [f'AR{i}' for i in range(1, 5)]  # List of AreaIDs (AR1 to AR4)
    output_file = 'output.xlsx'

    # Run the main function with the specified parameters
    main(time_ids, team_ids, area_ids, output_file)
import pandas as pd
import logging
from generate_data import generate_area_facts_data
from constants import TIME_IDS, TEAM_IDS, AREA_IDS
from export_excel import export_to_excel



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
    output_file = 'output.xlsx'

    # Run the main function with the specified parameters
    main(TIME_IDS, TEAM_IDS, AREA_IDS, output_file)
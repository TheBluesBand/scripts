import pandas as pd
import logging

from generate_data import generate_area_facts_data, generate_time_dim

def main():
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
    from generate_data import generate_metric_facts_data
    from export_excel import export_to_excel

    print("Select the type of data to generate:")
    print("1. Generate Area Facts Data")
    print("2. Generate Metric Facts Data")
    print("3. Generate Time Dim Data")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        data = generate_area_facts_data()
        output_file = 'area_facts.xlsx'
    elif choice == '2':
        data = generate_metric_facts_data()
        output_file = 'metric_facts.xlsx'
    elif choice == '3':
        year = int(input("Enter the year for Time Dim data: "))
        data = generate_time_dim(year)
        output_file = 'time_dim.xlsx'
    else:
        print("Invalid choice. Exiting.")
        return

    # Export the generated data to an Excel file
    export_to_excel(data, output_file)

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Run the main function with the specified parameters
    main()
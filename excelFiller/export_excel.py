import pandas as pd
import logging

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
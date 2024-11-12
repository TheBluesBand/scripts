# Excel Filler

## Overview

The `excelFiller` directory contains scripts to generate mock data and export it to an Excel file. These scripts are useful for testing and demonstration purposes. The main components include data generation functions, constants, and an export function.

## Files

`excelFiller.py`
This is the main script that orchestrates the data generation and export process.

## Functions

- `main(time_ids, team_ids, area_ids, output_file)`:
  - Generates data and exports it to an Excel file.
  - Args:
    - time_ids (list): List of TimeIDs.
    - team_ids (list): List of TeamIDs.
    - area_ids (list): List of AreaIDs.
    - output_file (str): The name of the output Excel file.
  - Returns: None

## Usage

```bash
python excelFiller.py
```

`generate_data.py`

This script contains functions to generate mock data for area facts and metric facts.

## Functions

- `generate_area_facts_data(time_ids, team_ids, area_ids)`:
  - Generates mock data for area facts.
  - Args:
    - time_ids (list): List of TimeIDs.
    - team_ids (list): List of TeamIDs.
    - area_ids (list): List of AreaIDs.
  - Returns: A dictionary containing the generated data with keys 'AreaID', 'TimeID', 'TeamID', 'WeightedScore', and 'MaxScore'.
- `generate_metric_facts_data(time_ids, team_ids)`:
  - Generates mock data for metric facts.
  - Args:
    - time_ids (list): List of TimeIDs.
    - team_ids (list): List of TeamIDs.
  - Returns: A dictionary containing the generated data with keys 'Entry', 'MetricID', 'TimeID', 'TeamID', 'Value', 'Score', and 'WeightedScore'.

`constants.py`

This script defines constants used across the other scripts.

## Constants

- `TIME_IDS`: List of TimeIDs (e.g., `['T1', 'T2', ..., 'T9']`).
- `TEAM_IDS`: List of TeamIDs (e.g., `['TM1', 'TM2', ..., 'TM7']`).
- `AREA_IDS`: List of AreaIDs (e.g., `['AR1', 'AR2', ..., 'AR4']`).
- `METRIC_IDS`: List of MetricIDs (e.g., `['M001', 'M002', ..., 'M011']`).
- `metric_ranges`: Dictionary mapping MetricIDs to their value ranges, score sets, and weights.

`export_excel.py`

This script contains a function to export data to an Excel file.

## Functions

- `export_to_excel(data, filename)`:
  - Exports data to an Excel file.
  - Args:
    - data (dict): The data to be exported, in dictionary format.
    - filename (str): The name of the output Excel file.
  - Returns: None

# Example Usage

1. Generate and Export Data:
   Run the excelFiller.py script to generate mock data and export it to an Excel file.

```bash
python excelFiller.py
```

2. Customize Constants:
   - Modify the constants.py file to update the lists of TimeIDs, TeamIDs, AreaIDs, and MetricIDs as needed.
3. Generate Area Facts Data:
   - Use the generate_area_facts_data function in generate_data.py to generate mock data for area facts.
4. Generate Metric Facts Data:
   - Use the generate_metric_facts_data function in generate_data.py to generate mock data for metric facts.
5. Export Data to Excel:
   -Use the export_to_excel function in export_excel.py to export data to an Excel file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

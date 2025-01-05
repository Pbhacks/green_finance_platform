import pandas as pd
from tkinter import filedialog, Tk

# Function to collect and process data from any CSV file
def collect_and_process_data(file_path=None):
    if not file_path:
        raise ValueError("No file path provided")

    # Read the CSV file
    df = pd.read_csv(file_path)

    print("Initial DataFrame:\n", df.head())  # Debugging line to check the data before processing

    # Define the required columns
    required_columns = ['project_id', 'emissions_reduction', 'cost', 'risk', 'kpi']

    # Check for missing columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"Warning: Missing columns in the CSV: {', '.join(missing_columns)}")
        # Proceed with available columns and fill missing ones with default values (0 or NaN)
        for col in missing_columns:
            df[col] = 0  # You can also set NaN for missing columns if you prefer

    # Handle potential issues with non-numeric values and clean data
    for col in ['emissions_reduction', 'cost', 'risk', 'kpi']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Converts invalid data to NaN
            df[col] = df[col].fillna(0)  # Replace NaNs with 0 (or NaN as needed)

    # Normalize KPI column (optional, can be adjusted if needed)
    if 'kpi' in df.columns:
        df['normalized_kpi'] = df['kpi'] / df['kpi'].max() if df['kpi'].max() != 0 else 0
    else:
        df['normalized_kpi'] = 0  # Default if 'kpi' column is missing

    # Only keep relevant columns (in case there are extra columns in the CSV)
    df = df[['project_id', 'emissions_reduction', 'cost', 'risk', 'kpi', 'normalized_kpi']]

    print("Processed DataFrame:\n", df.head())  # Debugging line to check the processed data

    return df

# Function to open a file dialog and let the user choose a CSV file
def open_file_dialog():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

import pandas as pd
from tkinter import filedialog
from tkinter import Tk

def collect_and_process_data(file_path=None):
    # Simulated data collection if no file is selected (you can replace this with actual data)
    if not file_path:
        data = {
            'project_id': [1, 2, 3],
            'emissions_reduction': [20, 30, 15],
            'cost': [500000, 750000, 400000],
            'risk': [0.1, 0.2, 0.15],
            'kpi': [0.8, 0.9, 0.85]
        }
        df = pd.DataFrame(data)
    else:
        # Read CSV file selected by user
        df = pd.read_csv(file_path)

    # Normalize the KPI column for better scoring
    df['normalized_kpi'] = df['kpi'] / df['kpi'].max()

    return df

def open_file_dialog():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

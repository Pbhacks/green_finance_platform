import pandas as pd

def score_projects(df):
    # Required columns check
    required_columns = ['emissions_reduction', 'kpi', 'cost', 'risk']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    # Data type validation
    for col in required_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric
    
    # Handle missing values
    if df[required_columns].isnull().any().any():
        raise ValueError("Dataset contains missing values in scoring columns")
    
    print("Data before scoring:\n", df.head())
    
    # Calculate average score
    df['score'] = df[required_columns].mean(axis=1)  # Calculate mean across specified columns
    
    # Scale scores to 0-100 range for better interpretability
    min_score = df['score'].min()
    max_score = df['score'].max()
    if max_score - min_score > 0:
        df['score'] = ((df['score'] - min_score) / (max_score - min_score)) * 100
    
    # Ensure no negative scores
    df['score'] = df['score'].clip(lower=0)
    
    print("Data after scoring:\n", df[['project_id', 'score']].head())
    
    return df

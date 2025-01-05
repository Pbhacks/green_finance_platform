from scipy.optimize import linprog

def optimize_investments(df, total_budget=10000000):
    # Check if 'score' and 'cost' are present
    if 'score' not in df.columns or 'cost' not in df.columns:
        raise ValueError("Missing 'score' or 'cost' columns for optimization.")
    
    print("Data before optimization:\n", df.head())  # Debugging line to check data before optimization

    # Linear programming optimization to maximize the ESG impact within a given budget
    c = -df['score'].values  # Negative because linprog minimizes by default

    # Constraints:
    # 1. The total cost should not exceed the budget
    A = [df['cost'].values]
    b = [total_budget]
    
    # Bounds for each project (between 0 and 1: don't invest more than 100% in each project)
    x_bounds = [(0, 1) for _ in range(len(df))]
    
    # Solve the optimization problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
    
    # Extract optimized investments
    df['optimized_investment'] = res.x

    # Calculate optimized scores based on investments
    df['optimized_score'] = df['score'] * df['optimized_investment']
    
    print("Data after optimization:\n", df.head())  # Debugging line to check data after optimization

    return df

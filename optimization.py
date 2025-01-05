from scipy.optimize import linprog

def optimize_investments(scored_projects):
    # Example: Budget constraint for optimization
    budget = 1000000  # Example budget constraint
    costs = scored_projects['cost'].values
    scores = scored_projects['score'].values

    # Linear programming to maximize the score (minimize negative score)
    res = linprog(-scores, A_ub=[costs], b_ub=[budget], bounds=[(0, 1)]*len(costs), method='highs')

    # Include optimized allocation in the dataframe
    scored_projects['allocation'] = res.x
    return scored_projects[scored_projects['allocation'] > 0]  # Filter projects with positive allocation

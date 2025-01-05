def score_projects(data):
    # Weighted scoring for multiple ESG metrics (emissions reduction, risk, KPI, etc.)
    data['score'] = (0.5 * data['emissions_reduction'] +
                     0.3 * data['normalized_kpi'] -
                     0.2 * data['risk'])
    
    # Rank projects by their score
    return data.sort_values(by='score', ascending=False)

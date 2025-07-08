def suggest_interventions(row):
    suggestions = []
    if row['risk_flag'] == 'High':
        if row['bmi'] > 27:
            suggestions.append("Enroll in fitness and nutrition plan")
        if row['alcohol'] >= 2:
            suggestions.append("Counseling for alcohol moderation")
        if row['smoke'] == 1:
            suggestions.append("Smoking cessation program")
        if row['expenditure'] < 2000:
            suggestions.append("Financial wellness session")
    return "; ".join(suggestions)

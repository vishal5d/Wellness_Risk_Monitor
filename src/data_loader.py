import pandas as pd

def load_health_data(path="data/employees.csv"):
    df = pd.read_csv(path)

    # Map categorical to numeric
    df['sex'] = df['sex'].map({'male': 1, 'female': 0})
    df['alcohol'] = df['alcohol'].map({'never': 0, 'rarely': 1, 'occasionally': 2, 'daily': 3})
    df['smoke'] = df['smoke'].map({'no': 0, 'yes': 1})
    df['zone'] = df['zone'].astype('category').cat.codes

    # Keep only required columns
    df = df[['age', 'bmi', 'dependent', 'alcohol', 'smoke', 'expenditure']]
    
    df.dropna(inplace=True)
    return df

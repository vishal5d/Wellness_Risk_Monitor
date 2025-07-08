from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    features = ['age', 'bmi', 'dependent', 'alcohol', 'smoke', 'expenditure']

    model = IsolationForest(contamination=0.2, random_state=42)

    df['risk_flag'] = model.fit_predict(df[features])
    df['risk_flag'] = df['risk_flag'].map({1: 'Low', -1: 'High'})
    return df
from sklearn.cluster import KMeans

def assign_clusters(df, n_clusters=3):
    features = ['age', 'bmi', 'dependent', 'alcohol', 'smoke', 'expenditure']
    model = KMeans(n_clusters=n_clusters, random_state=42)
    df['risk_cluster'] = model.fit_predict(df[features])
    return df
from src.data_loader import load_health_data
from src.risk_assessment import detect_anomalies, assign_clusters  # <-- include assign_clusters
from src.interventions import suggest_interventions
from src.report_generator import export_report
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = load_health_data()
    df = detect_anomalies(df)
    df = assign_clusters(df)
    sns.countplot(data=df, x='risk_cluster')
    plt.title("Employee Risk Cluster Distribution")
    plt.show()  # <-- apply clustering here
    df['risk_flag'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Overall Risk Levels")
    plt.show()
    df['interventions'] = df.apply(suggest_interventions, axis=1)
    export_report(df)

if __name__ == "__main__":
    main()

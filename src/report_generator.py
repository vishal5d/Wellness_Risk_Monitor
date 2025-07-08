def export_report(df, out_path="reports/wellness_report.csv"):
    df.to_csv(out_path, index=False)
    print(f"✅ Report saved to {out_path}")
 

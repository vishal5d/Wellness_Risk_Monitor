# 🧠 Workplace Wellness Risk Monitor

A modular AI-based system that analyzes workplace health data to identify employees at risk for occupational health issues and suggests personalized interventions to improve overall wellness and reduce future risks.

---

## 🚩 Problem Statement

> **Build a system that analyzes workplace health data to identify employees at risk for occupational health issues and suggests targeted interventions.**

This project demonstrates:
- 🔍 Anomaly Detection for unusual health metrics
- 📊 Clustering employees into risk groups
- 💡 Rule-based suggestions for interventions
- 📁 Clean modular architecture
- 📉 Visual insights from risk profiling

---

## 🎯 Project Goals

- Analyze real workplace health data
- Detect risky behavior or health trends
- Assign employees to risk clusters
- Suggest wellness plans (e.g., smoking/alcohol reduction, diet, fitness)
- Export actionable reports for HR/health teams

---

## 🧱 Tech Stack

| Category        | Tools / Libraries                         |
|----------------|--------------------------------------------|
| Language        | Python 3.12                               |
| Data Handling   | pandas, numpy                             |
| ML Algorithms   | scikit-learn (Isolation Forest, KMeans)   |
| Visualization   | matplotlib, seaborn                       |
| DevOps          | Git, GitHub                               |

---

## 🗂️ Project Structure

workplace_wellness_monitor/
├── data/ # Input employee health data
│ └── employees.csv
├── reports/ # Output wellness reports + plots
│ └── wellness_report.csv
│ └── cluster_distribution.png
├── src/ # Source code modules
│ ├── data_loader.py
│ ├── risk_assessment.py
│ ├── interventions.py
│ └── report_generator.py
├── main.py # Main pipeline script
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 📌 Key Modules

| Module               | Purpose                                                 |
|----------------------|---------------------------------------------------------|
| `data_loader.py`     | Loads and preprocesses employee health data             |
| `risk_assessment.py` | Detects anomalies and clusters employees by risk        |
| `interventions.py`   | Suggests wellness interventions based on risk profile   |
| `report_generator.py`| Generates CSV reports for management teams              |

---

## 🧠 Algorithms Used

- **Isolation Forest**: Detects anomalies/outliers in employee health behavior.
- **KMeans Clustering**: Groups employees into wellness clusters based on lifestyle and health indicators.
- **Rule-based Recommendations**: Maps risky patterns to interventions (e.g., smoking cessation, fitness plans).

---

## ⚙️ How to Run

### 🧩 1. Clone the Repo

```bash
git clone https://github.com/vishal5d/Wellness_Risk_Monitor.git
cd Wellness_Risk_Monitor
```
### 📦 2. Install Requirements

pip install -r requirements.txt

### 3. Run the Project

python main.py



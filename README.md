<h1 align="center">📊 Telco Customer Churn Prediction</h1>

<p align="center">
  End-to-End ML web app that predicts telecom customer churn risk
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge">
</p>

---

## 🎯 Business Problem

Telecom companies lose millions every year to customer churn.
Identifying **which customers are likely to leave — before they do** allows
retention teams to act early with targeted offers and interventions.

This project simulates a real-world CRM analytics tool that gives a
**churn risk score + business recommendation** for any customer profile.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Core Programming |
| Scikit-learn | ML Model (Classification) |
| Pandas | Data Processing |
| Streamlit | Web Application |
| Pickle | Model Serialisation |
| IBM Telco Dataset | 7,043 customer records |

---

## 📊 Features

- Predicts churn probability as a percentage
- Interactive input fields — tenure, charges, contract type, services
- Risk classification — Low Risk vs High Risk with business status
- Business-focused recommendations for retention strategy
- Deployed locally via Streamlit

---

## 🧠 How It Works

1. **Data Cleaning** — handled missing values, encoded categorical variables
2. **Feature Selection** — selected 6 key churn predictors
3. **Model Training** — trained classifier on 80% of 7,043 records
4. **Deployment** — model saved as `.pkl`, loaded into Streamlit app
5. **Prediction** — user inputs customer details → app returns churn % + status

---

## 💡 Key Insights

- Customers on **month-to-month contracts** churn 3x more than annual holders
- **High monthly charges (>$65)** correlate strongly with churn risk
- Customers with **no tech support + fibre internet** show highest churn rates
- **Tenure under 12 months** is the strongest single predictor of churn

---

## 📁 Project Structure
telco-customer-churn-prediction/
│
├── app.py                                   # Streamlit web app
├── churn_prediction.py                      # Model training script
├── churn_model.pkl                          # Trained ML model
├── churn_eda_plots.png                      # EDA visualisation
├── WA_Fn-UseC_-Telco-Customer-Churn.csv     # Dataset
└── README.md
---

## ▶️ Run Locally

```bash
pip install streamlit scikit-learn pandas
streamlit run app.py
```

---

## 📸 Screenshots

<img width="989" alt="high-risk" src="https://github.com/user-attachments/assets/4764b1f3-a016-4f2b-b9ea-6d393f22403a" />
<img width="1038" alt="low-risk" src="https://github.com/user-attachments/assets/a47392a7-8b0a-4270-9067-80e82582e319" />
<img width="1205" alt="app-ui" src="https://github.com/user-attachments/assets/2a346526-b61c-486f-924a-ca58760dc760" />

---

## 👨‍💻 Author

**Affan Chaudhary**
BSc Data Science 
📧 chaudharyaffan25@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/affan-chaudhary) · [GitHub](https://github.com/chaudharyaffan)

---

*Built as part of an analytics portfolio targeting Data Analyst
and Business Intelligence roles

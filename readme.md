# AI-Based Phishing Website Detection

This project presents a Machine Learning–based system to detect phishing websites using URL and domain-based features. The model analyzes structural and behavioral characteristics of websites to classify them as either legitimate or phishing.

The system is deployed as an interactive web application using Streamlit, allowing users to check any URL in real time.

---

## Live Application

Public URL:
[https://YOUR-DEPLOYED-APP-LINK](https://definably-gushy-brunilda.ngrok-free.dev/)

Users can enter a website URL and receive:
- Website classification (Legitimate or Phishing)
- Confidence score of the prediction

---

## Problem Statement

Phishing websites impersonate trusted platforms such as banks, payment gateways, and social media sites to steal sensitive user information. Traditional blacklist-based detection systems fail to identify newly created phishing websites.

This project addresses the problem by applying supervised machine learning techniques to detect phishing websites based on URL structure, domain attributes, and website behavior.

---

## Technology Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Random Forest Classifier
- Streamlit
- Google Colab
- GitHub

---

## Dataset Description

- Source: Kaggle Phishing Website Dataset
- Total Samples: 11,000+
- Number of Features: 30
- Target Variable:
  - 1: Legitimate Website
  - -1: Phishing Website

The dataset contains URL-based, domain-based, and content-based features extracted from real-world websites.

---

## Machine Learning Models

The following models were evaluated:

| Model | Accuracy |
|------|----------|
| Logistic Regression | ~92% |
| Random Forest Classifier | ~97% |

The Random Forest model was selected for deployment due to its higher accuracy and robustness.

---

## Feature Engineering

Key features include:
- URL length
- Presence of IP address in URL
- Use of URL shortening services
- SSL certificate status
- Domain registration length
- Google indexing status
- Number of external links
- Use of pop-ups and iframes

---

## Model Interpretability

Feature importance analysis was performed using the Random Forest classifier to identify the most influential features contributing to phishing detection.

---

## Web Application

The web interface is built using Streamlit and provides:
- A text input field for entering URLs
- Real-time predictions
- Classification confidence scores

<img width="1909" height="946" alt="image" src="https://github.com/user-attachments/assets/ed8c860a-4d8f-4929-b69a-ea6cd7b72316" />



---

## Project Structure
phishing-website-detection/
│
├── app.py
├── dataset.csv
├── phishing_detector_rf.pkl
├── requirements.txt
├── README.md
└── logs.txt

Future Enhancements

Deploy on Streamlit Cloud for permanent access

Add Explainable AI using SHAP

Integrate real-time feature extraction from live URLs

Provide REST API support for external integration

Author

Chirayu Bangera
B.Tech, Computer Science and Engineering (AI Specialization)

GitHub: https://github.com/Chirayu1264


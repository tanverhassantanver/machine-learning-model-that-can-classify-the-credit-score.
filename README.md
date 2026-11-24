# 💳 Credit Score Classification Using Machine Learning

## 📌 Project Overview

This project aims to develop an intelligent machine learning system that classifies individuals into different credit score categories based on their banking and financial information. The system analyzes customer financial behavior and predicts credit scores to reduce manual assessment efforts and support efficient credit risk evaluation.

## 🎯 Project Objectives

- Predict customer credit score categories.
- Analyze banking and financial information.
- Automate the credit score classification process.
- Reduce manual credit assessment efforts.
- Support data-driven financial decision-making.

## 📊 Dataset Information

The dataset contains customer banking and credit-related information, including:

- Annual Income
- Monthly In-hand Salary
- Number of Bank Accounts
- Number of Credit Cards
- Interest Rate
- Outstanding Debt
- Credit History Age
- Payment Behaviour
- Credit Utilization Ratio

**Target Variable:** `Credit_Score`

**Classification Categories:**
- Good
- Standard
- Poor

## ⚙️ Project Workflow

1. Data Collection
2. Data Exploration and Analysis
3. Data Cleaning and Preprocessing
4. Missing Value Handling
5. Feature Engineering
6. Categorical Data Encoding
7. Model Training
8. Model Evaluation
9. Hyperparameter Tuning
10. Model Saving

## 🤖 Machine Learning Algorithms

The following algorithms were explored:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- LightGBM Classifier
- CatBoost Classifier

## 🏆 Best Performing Model

**Random Forest Classifier**

- Accuracy: 78.93%
- Precision: 78.89%
- Recall: 78.93%
- F1-Score: 78.90%

## 🛠️ Technologies & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Joblib
- Flask

## 📁 Project Structure

```text
Credit-Score-Classification/
│
├── dataset/
├── notebooks/
├── models/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📥 Trained Model Download

The trained Random Forest model is hosted on Google Drive because of its large file size.

**[Download Trained Model](PASTE_YOUR_GOOGLE_DRIVE_LINK_HERE)**

After downloading, place the model file in the appropriate project directory before running the application.

## 🚀 Installation & Usage

**1. Clone the Repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the Project Folder**

```bash
cd YOUR_PROJECT_FOLDER
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Application**

```bash
python app.py
```

## 🌟 Project Applications

- Automated credit score assessment.
- Financial risk analysis.
- Customer credit evaluation.
- Data-driven banking decisions.

## pkl.file link:
https://drive.google.com/drive/folders/1ZdUcYswlo5wKiXz_xvxW9YI0h8LnXQyw?usp=sharing

## 👨‍💻 Author

**Tanver Hassan Tanver**

## 📌 Conclusion

This project demonstrates how machine learning can automate credit score classification using customer banking and financial data. By leveraging multiple classification algorithms and selecting the best-performing model, the system provides an efficient approach to credit assessment and financial decision support.

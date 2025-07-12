# 🩺 Diabetes Prediction Using Machine Learning

This project uses various machine learning models to predict whether a person has diabetes, based on health-related features such as age, BMI, blood glucose level, and more. The dataset used is publicly available and has been preprocessed for high-quality classification.

---

## 📊 Project Goals

- Clean and explore the dataset
- Apply feature engineering (including binning of age, BMI, and glucose level)
- Build multiple classification models:
  - Logistic Regression
  - Random Forest
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors (KNN)
  - XGBoost
- Evaluate and compare model performance using metrics like:
  - Precision
  - Recall
  - F1-Score
  - Accuracy
- Select the best model for predicting diabetes

---

## 🧠 Dataset Description

- **Source**: [Kaggle Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)
- **Features**:
  - `age`
  - `gender`
  - `hypertension`
  - `heart_disease`
  - `smoking_history`
  - `bmi`
  - `HbA1c_level`
  - `blood_glucose_level`
  - `diabetes` (Target variable: 1 = diabetic, 0 = non-diabetic)

---

## 🧰 Technologies Used

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- xgboost

---

## ⚙️ Project Workflow

1. **Data Cleaning**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Engineering**:
   - Binning of age, BMI, and glucose level into categories
4. **Model Training & Evaluation**:
   - Trained multiple models
   - Compared using classification report (Precision, Recall, F1)
5. **Result Summary**:
   - XGBoost performed best with highest F1-score and recall on diabetic class

---

## 📈 Results Snapshot

| Model              | Precision | Recall | F1-Score | Diabetes Class (1) |
|-------------------|-----------|--------|----------|---------------------|
| XGBoost            | 0.81      | 0.68   | 0.74     | ✅ Best performer   |
| Random Forest      | 0.84      | 0.61   | 0.71     |                    |
| Logistic Regression| 0.76      | 0.45   | 0.56     |                    |

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/diabetes-prediction.git
   cd diabetes-prediction
   pip install -r requirements.txt
🧠 Author
Michy Bliss
Data Scientist | Lifelong Learner | Passionate about Tech A Data Enthuisast

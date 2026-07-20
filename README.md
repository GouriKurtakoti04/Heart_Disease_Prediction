# 🫀 Heart Disease Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?style=flat-square&logo=powerbi)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat-square&logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

> A machine learning project that predicts the risk of heart disease in patients based on clinical attributes using KNN Classification and Logistic Regression — evaluated with ROC Curve, Confusion Matrix, and visualized through a Power BI dashboard.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Workflow](#-workflow)
- [Data Preprocessing](#-data-preprocessing)
- [Models Used](#-models-used)
- [Results & Evaluation](#-results--evaluation)
- [Model Comparison](#-model-comparison)
- [Power BI Dashboard](#-power-bi-dashboard)
- [How to Run](#-how-to-run)
- [Conclusion](#-conclusion)
- [Future Scope](#-future-scope)

---

## 📌 Overview

Heart disease is one of the leading causes of mortality worldwide. Early and accurate prediction can help medical professionals intervene at the right time and potentially save lives.

This project builds a **binary classification system** that predicts whether a patient has heart disease or not, based on 13 clinical features such as age, blood pressure, cholesterol, and maximum heart rate. Two machine learning models — **K-Nearest Neighbors (KNN)** and **Logistic Regression** — were trained, tested, and compared.

Key highlights:
- ✅ 83.41% accuracy with KNN
- ✅ AUC Score of 0.95 (Excellent)
- ✅ Clean, balanced dataset with no missing values
- ✅ Power BI dashboard for visual insights

---

## 📊 Dataset

| Property | Details |
|---|---|
| **Name** | UCI Heart Disease Dataset (Cleveland) |
| **Source** | [Kaggle — Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) |
| **Records** | 1025 patients |
| **Features** | 14 columns (13 input + 1 target) |
| **Target** | 0 = No Disease, 1 = Disease Present |
| **Class Balance** | 526 Disease (51.3%) / 499 No Disease (48.7%) |

### Feature Description

| Feature | Description | Type |
|---|---|---|
| `age` | Age of the patient (years) | Numerical |
| `sex` | Gender (1 = Male, 0 = Female) | Categorical |
| `cp` | Chest pain type (0–3) | Categorical |
| `trestbps` | Resting blood pressure (mm Hg) | Numerical |
| `chol` | Serum cholesterol (mg/dl) | Numerical |
| `fbs` | Fasting blood sugar > 120 mg/dl (1 = Yes) | Categorical |
| `restecg` | Resting ECG results (0–2) | Categorical |
| `thalach` | Maximum heart rate achieved | Numerical |
| `exang` | Exercise-induced angina (1 = Yes, 0 = No) | Categorical |
| `oldpeak` | ST depression induced by exercise | Numerical |
| `slope` | Slope of peak exercise ST segment (0–2) | Categorical |
| `ca` | Number of major vessels coloured by fluoroscopy (0–4) | Numerical |
| `thal` | Thalassemia type (0–3) | Categorical |
| `target` | **Heart disease present (1) or not (0)** — Output label | Label |

---

## 📁 Project Structure

```
heart-disease-prediction/
│
├── heart.csv                        # Dataset
├── heart_disease_results.csv        # Exported results with predictions
│
├── Heart_Disease_Prediction.ipynb   # Main Jupyter Notebook
│
├── dashboard/
│   └── Heart_Disease_Dashboard.pbix # Power BI Dashboard file
│
├── report/
│   └── Heart_Disease_Project_Report.docx  # Full project report
│
└── README.md
```

---

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Pandas | Data loading and manipulation |
| NumPy | Numerical computations |
| Matplotlib | Plotting graphs |
| Seaborn | Statistical visualizations (heatmap, histplot) |
| Scikit-learn | ML model training and evaluation |
| Power BI Desktop | Interactive dashboard |
| Jupyter Notebook | Development environment |

---

## 🔄 Workflow

```
1. Load Dataset (heart.csv)
        ↓
2. Exploratory Data Analysis
   - Shape, Info, Describe
   - Null value check
   - Target distribution
        ↓
3. Data Visualization
   - Count plot, Histogram, Correlation Heatmap
        ↓
4. Preprocessing
   - Feature/Label separation (X, y)
   - Train-Test Split (80:20)
   - Standard Scaling
        ↓
5. Model Training
   - KNN (k=5)
   - Logistic Regression (max_iter=1000)
        ↓
6. Evaluation
   - Accuracy Score
   - Confusion Matrix
   - Classification Report
   - ROC Curve + AUC Score
        ↓
7. Export Results → heart_disease_results.csv
        ↓
8. Power BI Dashboard
```

---

## ⚙️ Data Preprocessing

### Exploratory Data Analysis
```python
df.shape        # (1025, 14)
df.info()       # All 1025 non-null — no missing values
df.describe()   # Age: 29–77, Chol: 126–564
df['target'].value_counts()
# 1 → 526  (51.3%)
# 0 → 499  (48.7%)
```

### Train-Test Split
```python
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Training: 820 samples | Testing: 205 samples
```

### Feature Scaling
```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)
```

> `fit_transform` is applied only on training data to learn scaling parameters. `transform` is applied on test data using the already-learned parameters — this prevents **data leakage**.

---

## 🤖 Models Used

### 1. K-Nearest Neighbors (KNN)

KNN is a non-parametric, instance-based algorithm. It classifies a new patient by finding the K nearest patients in the training data and taking a majority vote.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
```

**How it works here:** For each test patient, the model finds the 5 most similar patients in training data. If 3 or more have heart disease → predicts Disease.

---

### 2. Logistic Regression

Logistic Regression uses the sigmoid function to compute the probability of a patient having heart disease. If probability > 0.5 → predicts Disease.

```python
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
```

---

## 📈 Results & Evaluation

### Accuracy

| Model | Accuracy |
|---|---|
| **KNN (k=5)** | **83.41%** ✅ |
| Logistic Regression | 79.51% |

---

### Confusion Matrix — KNN

```
                  Predicted: No Disease    Predicted: Disease
Actual: No Disease        79                     23
Actual: Disease           11                     92
```

- **True Negatives (TN):** 79 — Correctly predicted No Disease
- **True Positives (TP):** 92 — Correctly predicted Disease
- **False Positives (FP):** 23 — Predicted Disease when actually No Disease
- **False Negatives (FN):** 11 — Missed actual Disease cases ⚠️

---

### Confusion Matrix — Logistic Regression

```
                  Predicted: No Disease    Predicted: Disease
Actual: No Disease        73                     29
Actual: Disease           13                     90
```

---

### Classification Report — KNN

```
              precision    recall  f1-score   support

           0       0.88      0.77      0.82       102
           1       0.80      0.89      0.84       103

    accuracy                           0.83       205
   macro avg       0.84      0.83      0.83       205
weighted avg       0.84      0.83      0.83       205
```

---

### Classification Report — Logistic Regression

```
              precision    recall  f1-score   support

           0       0.85      0.72      0.78       102
           1       0.76      0.87      0.81       103

    accuracy                           0.80       205
   macro avg       0.80      0.79      0.79       205
weighted avg       0.80      0.80      0.79       205
```

---

### ROC Curve & AUC Score

```python
KNN AUC                : 0.95  ← Excellent
Logistic Regression AUC: 0.88  ← Good
```

> An AUC of **0.95** means the KNN model can correctly distinguish between a diseased and healthy patient **95% of the time**.  
> AUC > 0.90 is generally considered **Excellent**.

---

## ⚖️ Model Comparison

| Metric | KNN (k=5) | Logistic Regression |
|---|---|---|
| **Accuracy** | **83.41%** ✅ | 79.51% |
| **AUC Score** | **0.95** ✅ | 0.88 |
| **Precision (Class 1)** | **80%** ✅ | 76% |
| **Recall (Class 1)** | **89%** ✅ | 87% |
| **F1 Score (Class 1)** | **0.84** ✅ | 0.81 |
| **True Positives** | **92** ✅ | 90 |
| **False Negatives** | **11** ✅ | 13 |

**Winner: KNN** — outperforms Logistic Regression on every metric for this dataset.

KNN works better here because the decision boundary for heart disease classification is **non-linear**, which KNN handles naturally by working in feature space rather than assuming a linear relationship like Logistic Regression does.

---

## 📊 Power BI Dashboard

The final results were exported to `heart_disease_results.csv` and loaded into Power BI to create an interactive dashboard with 4 visuals:

| Visual | Chart Type | Insight |
|---|---|---|
| Disease Distribution | Pie Chart | 526 (51.3%) Disease vs 499 (48.7%) No Disease |
| Age vs Heart Disease | Stacked Bar Chart | Disease more frequent in ages 50–65 |
| KNN vs LR Comparison | Clustered Bar Chart | KNN predicted disease cases more accurately |
| Patient Data Table | Table | age, sex, cholesterol, heart rate, result per patient |

---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/saniya/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Launch Jupyter Notebook
```bash
jupyter notebook
```

### 4. Open and Run
Open `Heart_Disease_Prediction.ipynb` and run all cells top to bottom.

> Make sure `heart.csv` is in the same directory as the notebook.

---

## ✅ Conclusion

This project successfully demonstrated the use of machine learning for early heart disease detection. KNN with k=5 gave the best results with **83.41% accuracy** and **AUC of 0.95**, making it the preferred model for this dataset.

The results confirm that clinical attributes like chest pain type, maximum heart rate, and ST depression are strong indicators of heart disease. Machine learning models can serve as effective decision-support tools for medical professionals.

---

## 🔭 Future Scope

- Try advanced models like **Random Forest**, **XGBoost**, or **SVM** for higher accuracy
- Apply **GridSearchCV** for hyperparameter tuning
- Use **k-fold cross-validation** for more reliable evaluation
- Build a **web app using Flask or Streamlit** for real-time patient prediction
- Deploy the model using **Docker** or **Heroku**
- Use a **larger and more diverse dataset** for better generalization


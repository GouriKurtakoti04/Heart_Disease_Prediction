# ❤️ Heart Disease Prediction

A machine learning project that predicts the likelihood of heart disease in a patient based on clinical and demographic features. This project applies data preprocessing, exploratory data analysis (EDA), and classification algorithms to build an accurate predictive model.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Project Workflow](#project-workflow)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 📖 About the Project

Cardiovascular disease is one of the leading causes of death worldwide. Early prediction can help in timely medical intervention. This project uses supervised machine learning techniques to classify whether a patient is likely to have heart disease based on features like age, cholesterol level, blood pressure, chest pain type, and more.

---

## 📊 Dataset

- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease) / Kaggle
- **Features include:**
  - Age
  - Sex
  - Chest Pain Type (cp)
  - Resting Blood Pressure (trestbps)
  - Serum Cholesterol (chol)
  - Fasting Blood Sugar (fbs)
  - Resting ECG results (restecg)
  - Maximum Heart Rate Achieved (thalach)
  - Exercise Induced Angina (exang)
  - ST Depression (oldpeak)
  - Number of Major Vessels (ca)
  - Thalassemia (thal)
- **Target:** Presence (1) or absence (0) of heart disease

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:**
  - `pandas`, `numpy` – Data manipulation
  - `matplotlib`, `seaborn` – Data visualization
  - `scikit-learn` – Model building & evaluation
  - `jupyter notebook` – Development environment

---

## 🔄 Project Workflow

1. **Data Collection** – Import dataset
2. **Data Cleaning** – Handle missing values, duplicates, outliers
3. **Exploratory Data Analysis (EDA)** – Visualize distributions, correlations
4. **Feature Engineering** – Encoding categorical variables, feature scaling
5. **Model Building** – Train multiple classification models:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - K-Nearest Neighbors (KNN)
   - Support Vector Machine (SVM)
6. **Model Evaluation** – Compare accuracy, precision, recall, F1-score
7. **Model Selection** – Choose best-performing model

---

## 📈 Model Performance

| Model                  | Accuracy |
|-------------------------|----------|
| Logistic Regression     | XX%      |
| Decision Tree            | XX%      |
| Random Forest            | XX%      |
| KNN                       | XX%      |
| SVM                       | XX%      |

> Replace with your actual results after running the models.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Jupyter Notebook:

```bash
jupyter notebook Heart_Disease_Prediction.ipynb
```

Or run the Python script:

```bash
python predict.py
```

---

## 📂 Project Structure

```
heart-disease-prediction/
│
├── data/
│   └── heart.csv
├── notebooks/
│   └── Heart_Disease_Prediction.ipynb
├── src/
│   └── predict.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Future Improvements

- Deploy model using Flask/Streamlit as a web app
- Add deep learning models (ANN) for comparison
- Hyperparameter tuning using GridSearchCV
- Integrate with a real-time health monitoring system

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♀️ Author

**Saniya**
Basaveshwar Engineering College
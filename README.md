# ✈️ Customer Satisfaction Probability Prediction

A machine learning web application that predicts whether an airline passenger is **satisfied** or **neutral/dissatisfied** based on their flight experience and service ratings.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model](#model)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Tech Stack](#tech-stack)
- [Author](#author)

---

## Overview

This project builds an end-to-end machine learning pipeline to predict **customer satisfaction** for airline passengers. It covers the full workflow — from raw data exploration and preprocessing to model training, evaluation, and deployment as an interactive **Streamlit** web application.

The trained model takes 22 passenger-related features (demographics, travel type, flight class, service ratings, and delays) and outputs a binary prediction: **Satisfied** 😆 or **Neutral / Dissatisfied** 😒.

---

## Demo

> Run locally using the instructions in the [Usage](#usage) section.

| Sidebar Inputs | Prediction Output |
|---|---|
| Demographics, travel class, service ratings | ✅ Satisfied / ❌ Neutral or Dissatisfied |

---

## Project Structure

```
├── data_preprocessing_and_model_training.ipynb   # Full EDA, preprocessing & model training notebook
├── app.py                                         # Streamlit web application
├── model.pkl                                      # Serialized trained Random Forest model
├── customer_satisfication_dataset.csv             # Raw dataset (not included — see Dataset section)
├── requirements.txt                               # Python dependencies
└── README.md                                      # Project documentation
```

---

## Dataset

The dataset used is the **Airline Passenger Satisfaction** dataset, containing survey responses and flight details for thousands of passengers.

**Key columns include:**

| Column | Type | Description |
|---|---|---|
| `Gender` | Categorical | Male / Female |
| `Customer Type` | Categorical | Loyal / Disloyal Customer |
| `Age` | Numeric | Passenger age |
| `Type of Travel` | Categorical | Business / Personal Travel |
| `Class` | Categorical | Business, Eco, Eco Plus |
| `Flight Distance` | Numeric | Distance of the flight (miles) |
| `Inflight wifi service` | Numeric | Rating 0–5 |
| `Seat comfort` | Numeric | Rating 0–5 |
| `Departure Delay in Minutes` | Numeric | Departure delay duration |
| `Arrival Delay in Minutes` | Numeric | Arrival delay duration |
| `satisfaction` | Target | Satisfied / Neutral or Dissatisfied |

> **Note:** The dataset file (`customer_satisfication_dataset.csv`) is not included in this repository. You can find a compatible dataset on [Kaggle — Airline Passenger Satisfaction](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction).

---

## Exploratory Data Analysis

The notebook covers a thorough EDA including:

- ✅ Shape, dtypes, and column inventory
- ✅ Missing value analysis (`Arrival Delay in Minutes` — filled with median)
- ✅ Duplicate detection
- ✅ Satisfaction distribution (count plot)
- ✅ Satisfied vs. Dissatisfied breakdown by **Gender**, **Class**, and **Type of Travel**
- ✅ Correlation heatmap across all numeric features

---

## Model

A **Random Forest Classifier** was trained with the following configuration:

```python
RandomForestClassifier(n_estimators=350, min_samples_split=11)
```

**Preprocessing steps applied before training:**

1. Dropped irrelevant columns: `Unnamed: 0`, `id`
2. Imputed missing values in `Arrival Delay in Minutes` with the column median
3. Label-encoded all categorical features:
   - `Gender`: Male → 1, Female → 0
   - `Customer Type`: Loyal → 1, Disloyal → 0
   - `Type of Travel`: Business → 1, Personal → 0
   - `Class`: Business → 1, Eco → 2, Eco Plus → 3
   - `satisfaction`: Satisfied → 1, Neutral/Dissatisfied → 0
4. 80/20 train-test split (`random_state=42`)

The trained model is serialized and saved as `model.pkl` using Python's `pickle` module.

---

## Features

The Streamlit app accepts the following 22 input features via the sidebar:

| # | Feature | Input Type | Range / Options |
|---|---|---|---|
| 1 | Gender | Selectbox | Male, Female |
| 2 | Customer Type | Selectbox | Loyal, Disloyal |
| 3 | Age | Number Input | 7 – 85 |
| 4 | Type of Travel | Selectbox | Business, Personal |
| 5 | Class | Selectbox | Business, Eco, Eco Plus |
| 6 | Flight Distance | Number Input | 31 – 4983 |
| 7 | Inflight wifi service | Number Input | 0 – 5 |
| 8 | Departure/Arrival time convenient | Number Input | 0 – 5 |
| 9 | Ease of Online booking | Number Input | 0 – 5 |
| 10 | Gate location | Number Input | 1 – 5 |
| 11 | Food and drink | Number Input | 0 – 5 |
| 12 | Online boarding | Number Input | 0 – 5 |
| 13 | Seat comfort | Number Input | 0 – 5 |
| 14 | Inflight entertainment | Number Input | 0 – 5 |
| 15 | On-board service | Number Input | 0 – 5 |
| 16 | Leg room service | Number Input | 0 – 5 |
| 17 | Baggage handling | Number Input | 1 – 5 |
| 18 | Checkin service | Number Input | 0 – 5 |
| 19 | Inflight service | Number Input | 0 – 5 |
| 20 | Cleanliness | Number Input | 0 – 5 |
| 21 | Departure Delay in Minutes | Number Input | 0 – 1592 |
| 22 | Arrival Delay in Minutes | Number Input | 0 – 1584 |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/customer-satisfaction-prediction.git
cd customer-satisfaction-prediction
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

### Retrain the Model

Open and run the Jupyter notebook:

```bash
jupyter notebook data_preprocessing_and_model_training.ipynb
```

This will regenerate `model.pkl` with the latest data.

---

## Model Performance

| Metric | Score |
|---|---|
| **Accuracy** | 96% |
| **Precision** | 95% |
| **Recall** | 98% |

> Evaluated on a held-out 20% test set.

---

## Tech Stack

| Category | Library / Tool |
|---|---|
| Language | Python 3.x |
| Data Manipulation | pandas |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn |
| Model Serialization | pickle |
| Web App | Streamlit |
| Notebook | Jupyter |

---

## Author

Built by **Zakir Ali** — Machine Learning Engineer

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)

---

> ⭐ If you found this project helpful, feel free to star the repository!

# 🎓 Student Performance Analysis Dashboard with ML

An interactive data analysis and machine learning dashboard built using **pandas**, **matplotlib**, and **Streamlit** to explore, analyze, and predict student performance outcomes.

---

## 📌 Project Highlights

- 📊 **Data Cleaning & Preprocessing**
- 📈 **Visual Analysis** based on gender, parental education, and test prep
- 🤖 **ML Model** to predict if a student will pass or fail
- ⚙️ **Streamlit Dashboard** with filters and live prediction form

---

## 🧠 Objective

To understand how different socio-academic factors affect student performance and provide an interactive tool to predict whether a student is likely to pass or fail based on their profile and scores.

---

## 📂 Dataset Info

- Source: [Kaggle - Students Performance Dataset](https://www.kaggle.com/spscientist/students-performance-in-exams)
- Features:
  - Gender, Race/Ethnicity
  - Parental Level of Education
  - Lunch Type, Test Preparation Course
  - Math, Reading, and Writing Scores

---

## 🔧 Tech Stack

| Tool / Library | Purpose                      |
| -------------- | ---------------------------- |
| `pandas`       | Data cleaning & manipulation |
| `matplotlib`   | Data visualization           |
| `sklearn`      | Machine learning model       |
| `Streamlit`    | Web app/dashboard            |
| `pickle`       | Model saving/loading         |

---

## 📊 Dashboard Features

- Sidebar filters: Gender, Race, Test Prep
- 📉 Dynamic charts:
  - Average Score by Parental Education
  - Average Score by Gender
- 🔍 ML Prediction Form:
  - Input scores and background info
  - Predict Pass/Fail with 1 click

---

## 🧠 ML Model

- Algorithm: `RandomForestClassifier`
- Accuracy: **100%** (on balanced, encoded dataset)
- Target Variable: `result` (`pass` / `fail`)
- Saved model used in Streamlit: `student_prediction_model.sav`

---

## 🚀 How to Run the Dashboard

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/student-performance-analysis.git
   cd student-performance-analysis
   ```
2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   streamlit run "path where you Dashboard_streamlit.py file is located"

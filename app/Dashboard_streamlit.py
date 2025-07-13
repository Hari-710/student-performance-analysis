import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Load data and model
df = pd.read_csv("C:/Desktop Files/Student-performance-analysis/output/StudentsPerformance_cleaned.csv")
model = pickle.load(open("C:/Desktop Files/Student-performance-analysis/output/student_prediction_model.sav", 'rb'))

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("🎓 Student Performance Dashboard with ML Prediction")

# Sidebar Filters
st.sidebar.header("Filter Dataset:")
gender = st.sidebar.selectbox("Gender", df['gender'].unique())
race = st.sidebar.selectbox("Race/Ethnicity", df['race/ethnicity'].unique())
prep = st.sidebar.selectbox("Test Preparation Course", df['test_preparation_course'].unique())

# Filtered Data
filtered_df = df[
    (df['gender'] == gender) &
    (df['race/ethnicity'] == race) &
    (df['test_preparation_course'] == prep)
]

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)

# ----- VISUALIZATIONS -----
st.subheader("Data Insights (based on filtered data)")
col1, col2 = st.columns(2)

# Chart 1: Parental Education
with col1:
    parent_avg = filtered_df.groupby('parental_level_of_education')['average_score'].mean().sort_values()
    fig1, ax1 = plt.subplots(figsize=(5, 2))
    parent_avg.plot(kind='barh', color='skyblue', ax=ax1)
    ax1.set_title("Average Score by Parental Education")
    ax1.set_xlabel("Avg Score")
    st.pyplot(fig1)

# Chart 2: Gender Average Score
with col2:
    gender_avg = filtered_df.groupby('gender')['average_score'].mean()
    fig2, ax2 = plt.subplots(figsize=(10, 3))
    gender_avg.plot(kind='bar', color='orchid', ax=ax2)
    ax2.set_title("Average Score by Gender")
    ax2.set_ylabel("Avg Score")
    st.pyplot(fig2)

# ----- ML PREDICTION -----
st.subheader("Predict Pass/Fail Based on Student Inputs")
col1, col2, col3 = st.columns(3)

with col1:
    gender_input = st.selectbox("Gender", ['male', 'female'])

with col2:
    race_input = st.selectbox("Race/Ethnicity", df['race/ethnicity'].unique())

with col3:
    parent_edu = st.selectbox("Parental Level of Education", df['parental_level_of_education'].unique())
    
with col1:
    lunch = st.selectbox("Lunch Type", df['lunch'].unique())

with col2:
    test_prep = st.selectbox("Test Preparation Course", df['test_preparation_course'].unique())

with col3:
    math = st.slider("Math Score", 0, 100, 50)
    reading = st.slider("Reading Score", 0, 100, 50)
    writing = st.slider("Writing Score", 0, 100, 50)

# Encoding logic
label_encodings = {
    'gender': {'female': 0, 'male': 1},
    'race/ethnicity': {'group a': 0, 'group b': 1, 'group c': 2, 'group d': 3, 'group e': 4},
    'parental_level_of_education': {
        "associate's degree": 0,
        "bachelor's degree": 1,
        "high school": 2,
        "master's degree": 3,
        "some college": 4,
        "some high school": 5
    },
    'lunch': {'free/reduced': 0, 'standard': 1},
    'test_preparation_course': {'completed': 0, 'none': 1}
}

if st.button("Predict Result"):
    total = math + reading + writing
    avg = total / 3

    encoded_input = [
        label_encodings['gender'][gender_input],
        label_encodings['race/ethnicity'][race_input],
        label_encodings['parental_level_of_education'][parent_edu],
        label_encodings['lunch'][lunch],
        label_encodings['test_preparation_course'][test_prep],
        math,
        reading,
        writing,
        total,
        avg
    ]

    result = model.predict([encoded_input])[0]
    if result == 1 or result == 'pass':
        st.success("Predicted Result: Pass")
    else:
        st.error("Predicted Result: Fail")

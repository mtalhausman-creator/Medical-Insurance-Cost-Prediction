
import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")
st.write("Enter the details below to predict the estimated insurance cost.")

age = st.number_input("Age", min_value=1, max_value=100, value=25)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

gender = st.selectbox("Gender", ["Male", "Female"])

smoker = st.selectbox("Smoker", ["Yes", "No"])

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

region = st.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

if st.button("Predict"):

    sex_male = 1 if gender == "Male" else 0
    smoker_yes = 1 if smoker == "Yes" else 0

    region_northwest = 1 if region == "Northwest" else 0
    region_southeast = 1 if region == "Southeast" else 0
    region_southwest = 1 if region == "Southwest" else 0

    input_data = pd.DataFrame([{
        "age": age,
        "bmi": bmi,
        "children": children,
        "sex_male": sex_male,
        "smoker_yes": smoker_yes,
        "region_northwest": region_northwest,
        "region_southeast": region_southeast,
        "region_southwest": region_southwest
    }])

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Insurance Cost: ${prediction[0]:,.2f}"
    )

import streamlit as st
import pickle

model = pickle.load(open('C:/Users/DELL/OneDrive/Desktop/ML Project/model (1).pkl', 'rb')) 
   
def main():
    st.title("Diabetes Prediction App")
    st.write("Enter the patient details to predict diabetes risk.")

   
    # Create input fields for features
    gender = st.selectbox("gender",["male","female"])
    smoking_history = st.selectbox("smoking_history", ["never", "No","current","former"])
    heart_disease = st.selectbox("Heart Disease", ["Yes", "No"])
    blood_glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=0, max_value=500, step=1)
    bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=100.0, step=0.1)
    age = st.number_input("Age (in years)", min_value=0, max_value=120, step=1)
    hypertension = st.selectbox("Hypertension", ["Yes", "No"])
    hba1c_level = st.number_input("HbA1c Level (%)", min_value=0.0, max_value=20.0, step=0.1)
    

    # Encode categorical variables (Gender, Smoking History)
    gender_encoded = 1 if gender == "Male" else 0
    smoking_mapping = {"Never": 0, "Former": 1, "Current": 2}
    

    # Prepare input data for prediction
    # Make prediction
    if st.button("Predict"):
        make_prediction =  model.predict([[heart_disease, bmi, 
        age,gender_encoded, hypertension, hba1c_level, smoking_history, blood_glucose]])
        output = round(make_prediction[0], 2)
        st.success('The predicted risk of diabetes is {}'.format(output))
        
if __name__ == "__main__":
    main()
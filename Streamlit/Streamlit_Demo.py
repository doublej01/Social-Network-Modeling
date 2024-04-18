# import necessary libraries

import streamlit as st
import pandas as pd
import numpy as np
from statistics import mode
from sklearn.ensemble import RandomForestRegressor
import pickle 
import seaborn as sns

# Load the main dataset and the model
df = pd.read_csv("./trained_data.csv")
with open("./rf_model2.pkl", 'rb') as model_file:
     model = pickle.load(model_file)

# Function to prepare input data
def prepare_input(selected_title, selected_work_type, selected_experience_level, selected_remote_allowed, selected_median_salary):
    input_data = {col: 0 for col in df.columns}  # Initialize all columns to 0

    # Assuming 'title_' is the prefix for title-related dummy columns
    title_key = f"title_{selected_title.replace(' ', '_').lower()}"
    if title_key in input_data:
        input_data[title_key] = 1
    
    work_type_key = f"{selected_work_type.replace(' ', '_').lower()}"
    if work_type_key in input_data:
        input_data[work_type_key] = 1

    exp_level_key = f"{selected_experience_level.replace(' ', '_').lower()}"
    if exp_level_key in input_data:
        input_data[exp_level_key] = 1

    input_data['remote_allowed'] = selected_remote_allowed  # Ensure no comma here
    input_data['med_salary'] = selected_median_salary

    return pd.DataFrame([input_data])

# Load column names
dummy_columns = df.columns.tolist()

top_20_keywords = ['manager', 'engineer', 'senior', 'sales', 'specialist', 'associate', 'assistant', 'analyst', 'director', 'technician', 'nurse', 'project', 'm', 'time', 'business', 'lead', 'service', 'coordinator', 'representative', 'developer'] 

def main():
    # Sidebar Navigator
    st.sidebar.title("Pages")
    pages = st.sidebar.radio("Go to", ("Home", "Projected View Count"))

    if pages == "Home":
        st.image('./linkedin_img2.png')
        st.header("Forecasting Views on LinkedIn Job Listings", divider='blue')
        st.write("Welcome to the LinkedIn Job Post Insights and Views Prediction App!")
        st.write("Using the Streamlit interface, we can explore the latest job trends and factors that influence the visibility of LinkedIn Job Listings. Moreover, this application also showcases a forecast of number of views of a future job posting based on varying job attributes.")
        #st.subheader("Areas of Interest", divider='blue')
        #st.write("How can we leverage the job postings data collected from LinkedIn in 2023 to add significant values to both companies and job applicants? Our main focus is to gain insights from the views columns and identify which variables contribute to higher views in teh company job postings.")
        #st.subheader("Impact", divider='blue')
        #st.write("The analysis of LinkedIn job postings offers considerable value to both employers and job seekers, potentially reshaping the recruitment landscape.")
        #st.markdown("""
                    #- Companies & Recruiters: understand which aspects of a job posting attract the most applicants allows for more targeted and effective recruitment strategies. Such insights can enhance job post visibility, attract higher quality candidates, and decrease the time it takes to fill a position.
                    #- Job applicants: access to detailed analytics on highly viewed job postings provides a wealth of information on current market trends and the most sought-after skills and experiences. This knowledge enables candidates to tailor their applications to better meet the needs of employers, significantly boosting their chances of securing jobs that match their skills and career aspirations.
        #""")
        st.subheader("LinkedIn Job Posting Dataset", divider='blue')
        st.markdown("""
                    - The LinkedIn Job Postings dataset has been retrieved from an open source called Kaggle.
                    - The dataset contains a comprehensive record of 33,000+ job postings listed over the course of 2 days, months apart.
                    - Each individual posting contains 27 valuable attributes, including title, job description, salary, location, application, work-types, and experience levels.
        """)
        st.subheader("Procedure", divider='blue')
        st.markdown("""
                    1. Data exploration through Exploratory Data Analysis (EDA)
                    2. Data cleaning and preprocessing for modeling
                    3. Text analysis through Natural Language Processing (NLP)
                    4. Advanced modeling, such as Random Forest and XGBoost Regressor to uncover relationships between views and different job attributes.
        """)    
        st.subheader("Additional Insights", divider='blue')
        st.image('./gitqr.png', caption="Redirecting to the project repository in GitHub", width=300)

    elif pages == "Projected View Count":
        st.header("Forecasting Views on LinkedIn Job Listings", divider='blue')

        # Generate options for 'Work Type' and 'Experience Level' from column names
        work_type_options = [col.replace('formatted_work_type_', '').replace('_', ' ').title() for col in dummy_columns if col.startswith('formatted_work_type_')]
        experience_level_options = [col.replace('formatted_experience_level_', '').replace('_', ' ').title() for col in dummy_columns if col.startswith('formatted_experience_level_')]

        selected_title = st.selectbox("Title", top_20_keywords, index=None, placeholder="Select a Title Keyword")  
        selected_work_type = st.selectbox("Work Type", work_type_options, index=None, placeholder="Select a Work Type")
        selected_experience_level = st.selectbox("Experience Level", experience_level_options, index=None, placeholder="Select an Experience Level")
        remote_options = {'In-person': 0, 'Remote': 1}
        selected_remote_allowed_label = st.radio("Work Mode", list(remote_options.keys()))
        selected_remote_allowed = remote_options[selected_remote_allowed_label]
        selected_median_salary = st.number_input("Median Salary", min_value=0, max_value=None, value=0, step=1)

        # Predict 
        if st.button("Predict"): 
            # Convert back the cleaned-up values to the original format for prediction
            work_type_key = f"formatted_work_type_{selected_work_type.lower().replace(' ', '_')}"
            experience_level_key = f"formatted_experience_level_{selected_experience_level.lower().replace(' ', '_')}"
            input_df = prepare_input(selected_title, selected_work_type, selected_experience_level, selected_remote_allowed, selected_median_salary)
            prediction = model.predict(input_df)
            st.write("Predicted Views:", prediction[0])
            


if __name__ == "__main__":
    main()

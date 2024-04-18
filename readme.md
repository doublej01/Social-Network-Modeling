# Capstone Project: Number of Views on LinkedIn Job Postings

Dataset Link: https://drive.google.com/drive/folders/14E6gphWmyFft1VgnIfx0yqqb8aOsJats?usp=sharing

Author: JJ Park

Date: 15/05/2024

Contact: doublej01@outlook.com

## Project Overview

### Problem Area
How can we leverage the job postings data collected from LinkedIn in 2023 to add significant values to both companies and job applicants? Our main focus is to gain insights from the `views` column by conducting preliminary EDA to find relationships between different variables within the dataset. Ultimately, we want to identify which variables contribute to higher views in the company job postings.

### Who's Affected?
The analysis of this dataset can benefit companies and recruiters as they can identify which elements within a job posting attract more applicants. On the other hand, applicants can predict the overall job market trends by analyzing job postings with high number of views. They can get further insights by identifying popular requirements listed within the job postings to understand companies' demands.

### Proposed Data Science Solutions
This project will primarily focus on the number of views of job postings from LinkedIn. The proposed data science solution involves the following components:

1. Exploratory Data Analysis (EDA): 
- Exploring and understanding the dataset to understand the distribution of views, identify outliers, and explore relationships between different variables.
- Identify key factors that contribute to higher views in job postings, such as job title, company size, industry, location, required skills, experience level, and salary range.
- Visualize insights gained from EDA to communicate findings effectively to stakeholders.

2. Feature Engineering:
- Engineer new features from existing data, such as creating binary columns to represent the presence of certain information in job postings (e.g., presence of closed time information, skills description, etc.).
- Extract relevant information from text fields, such as job descriptions, to create features that capture the uniqueness and attractiveness of job postings.

3. Predictive Modeling:
- Build predictive models to forecast the number of views for new job postings based on features extracted from the dataset.
- Utilize regression techniques, such as linear regression or random forest regression, to predict the views of job postings.
- Evaluate model performance using appropriate metrics and fine-tune models to improve accuracy.
- Regression models like Linear Regression, Random Forest and XG Boost.
- Natural Language Processing: word embedding.
- Evaluation Metrics: Mean Absolute Error (MAE) and R^2 to assess model performance.

### Impact of the Solutions

The analysis of LinkedIn job postings offers considerable value to both employers and job seekers, potentially reshaping the recruitment landscape. For companies and recruiters, understanding which aspects of a job posting attract the most applicants allows for more targeted and effective recruitment strategies. Such insights can enhance job post visibility, attract higher quality candidates, and decrease the time it takes to fill a position. This is critical in a job market where, according to LinkedIn, 89% of hiring managers report finding the right candidate within a month can significantly save costs and increase team productivity.

For job applicants, having access to detailed analytics on highly viewed job postings provides a wealth of information on current market trends and the most sought-after skills and experiences. This knowledge enables candidates to tailor their applications to better meet the needs of employers, significantly boosting their chances of securing jobs that match their skills and career aspirations. A survey from Zety found that tailored applications are 30% more likely to receive positive responses from employers. By effectively leveraging the insights from LinkedIn job posting analyses, both recruiters and job seekers can make more informed decisions, enhancing efficiency and efficacy in the job market, which is crucial for economic growth and personal career development.

### Dataset Description
The dataset consists of the following variables:

| Column | Description |
| --- | --- |
| job_id | The job ID as defined by LinkedIn |
| company_id | Identifier for the company associated with the job posting |
| title | Job title |
| description | Job description |
| max_salary | Maximum salary |
| med_salary | Median salary |
| min_salary | Minimum salary |
| pay_period | Pay period for salary (Hourly, Monthly, Yearly) |
| formatted_work_type | Type of work (Fulltime, Parttime, Contract) |
| location | Job location |
| applies | Number of applications that have been submitted |
| original_listed_time | Original time the job was listed |
| remote_allowed | Whether job permits remote work |
| views | Number of times the job posting has been viewed |
| job_posting_url | URL to the job posting on a platform |
| application_url | URL where applications can be submitted |
| application_type | Type of application process (offsite, complex/simple onsite) |
| expiry | Expiration date or time for the job listing |
| closed_time | Time to close job listing |
| formatted_experience_level | Job experience level (entry, associate, executive, etc) |
| skills_desc | Description detailing required skills for job |
| listed_time | Time when the job was listed |
| posting_domain | Domain of the website with application |
| sponsored | Whether the job listing is sponsored or promoted |
| work_type | Type of work associated with the job |
| currency | Currency in which the salary is provided |
| compensation_type | Type of compensation for the job | 

**Acknowledgement: the dataset description is directly sourced from: https://github.com/ArshKA/LinkedIn-Job-Scraper/blob/master/DatabaseStructure.md**

## Flowchart
1. **Data Collection:** 
- Retrieve the dataset

2. **Data Preprocessing:**
- Address data quality issues
- Check for Datatypes
- Filter duplicates
- Handle null values
- Perform feature engineering

3. **Exploratory Data Analysis:**
- Analyze distributions of variables
- Visualize patterns and correlations 
- Formulate initial questions for further analysis

4. **Baseline Modeling:**
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- Evaluation metrics: MAE and R-squared
- Interpret model coefficients 

5. **NLP**
- Splitting the dataset into train and test sets
- Identifying key words or phrases 
- Word Embedding

6. **Advanced Modeling**
- Fine tune hyperparameters
- Cross validation
- Grid search 

7. **Summary & Business Implications**
- Overall summary of the findings 
- Limitations and Next steps
- Business objectives and impacts on the society 

## Repository Navigation
Folders:
 1. **Documents** : Sprint1, Sprint2, Sprint3 presenations.
 2. **Notebooks** :
    
    a.PartI_LinkedIn_Preliminary_EDA.ipynb
    
    b.PartII_Advanced_EDA_and_Modeling.ipynb
    
    c.PartIII_NLP_and_Advanced_Modeling.ipynb
    
 3. **Data** : All the dataset CSVs
 
 4. **Streamlit** : Consists of datasets to execute the streamlit app
 a. **Streamlit_Demo.py** is the app python file
 b. **rf_model.pkl** is the random forest model pickle file
 c. **cleaned_dataset.csv** is the pretrained dataset needed to run the model

 5. **readme.md** : Details about this project.

## Notebook Usage Instructions

**Execution Order**

To run this entire project download all the files in the **Notebooks** folder into one single folder and run each notebook in this order: 

1. PartI_LinkedIn_Preliminary_EDA.ipynb
2. PartII_Advanced_EDA_and_Modeling.ipynb
3. PartIII_NLP_and_Advanced_Modeling.ipynb

The data files(CSVs) for each of these notebboks is present in the **'Data'** folder: job_postings.csv, clean_linkedin_job_postings.csv, preprocessed_linkedin_job_posting.csv

PartI_LinkedIn_Preliminary_EDA.ipynb
- Load the dataset 'job_postings.csv' from the 'Data' folder.
- Basic exploratory data analysis (EDA) has been performed to understand the overall structure of the data, address data quality issues, visualize key patterns among different job features, explore basic statistics, and check for outliers and correlations for modeling in the following notebooks.

PartII_Advanced_EDA_and_Modeling.ipynb
- Load the 'clean_linkedin_job_postings.csv' csv file from the 'Data' folder.
- Advanced EDA and preprocessing have been conducted to prepare a dataset for modeling (i.e., converting categorical variables into dummies through one hot encoding).
- The baseline modeling of linear regression, random forest, and XGBoost have been performed. 
- The models have been evaluated using standard metrics of Mean Absolute Error (MAE) and R-squared. 

PartIII_NLP_and_Advanced_Modeling.ipynb
- Load the 'preprocessed_linkedin_job_posting.csv' csv file from the 'Data' folder.
- Random Forest and XGBoost Regressor have been performed with cross-validation and hyperparameter-tuning to improve the model performance.
- The models have been evaluated using standard metrics of Mean Absolute Error (MAE) and R-squared.

## Acknowledgements and Source
**Source:** https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data?select=job_postings.csv





# Capstone Project: Number of Views on LinkedIn Job Postings

Dataset Link: https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data?select=job_postings.csv

Author: JJ Park

Date: 28/02/2024

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

**More solutions will be added as we delve into modeling and evaluations in Sprint 2 and 3.**

### Impact of the Solutions
The analysis of the LinkedIn job posting dataset can add significant values to:

- Companies and Recruiters: Gain insights into which elements within a job posting attract more applicants, allowing them to optimize their job postings and recruitment strategies. This can lead to increased visibility, better quality applicants, and reduced time-to-hire.
- Job Applicants: Access trends and insights from job postings with high views, helping them understand market demands and tailor their applications to align with popular requirements. This can improve their chances of securing relevant job opportunities and making informed career decisions.

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
- Deal with null values
- Perform feature engineering

3. **Exploratory Data Analysis:**
- Analyze distributions of variables
- Visualize patterns and correlations 
- Formulate initial questions for further analysis

**More steps will follow to address the problem area in more details using various modelling techniques.**

**Repository User Guide and Notebook Usage Instructions will be added in Sprint 2 and 3.**
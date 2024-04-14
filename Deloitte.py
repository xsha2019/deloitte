#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import random

# Define the path to the CSV files (adapt these paths according to your actual file locations)
file_paths = {
    'Deloitte General Background & Skills': 'Deloitte General Background & Skills.csv',
    'Deloitte Problem-Solving & Initiative': 'Deloitte Problem-Solving & Initiative.csv',
    'Deloitte Teamwork & Communication': 'Deloitte Teamwork & Communication.csv',
    'Deloitte Deloitte Specific': 'Deloitte Deloitte Specific.csv',
    'Deloitte Statistics & Probability':'Deloitte Statistics & Probability.csv',
    'Deloitte Statistics & Probability': 'Deloitte Statistics & Probability.csv',
    'Deloitte Machine Learning': 'Deloitte Machine Learning.csv',
    'Deloitte Data Wrangling & Programming': 'Deloitte Data Wrangling & Programming.csv',
    'Deloitte Scenario-Based Questions': 'Deloitte Scenario-Based Questions.csv',
    'Deloitte Deep Learning & Natural Language': 'Deloitte Deep Learning & Natural Language.csv',
    'Deloitte Big Data & Cloud Computing': 'Deloitte Big Data & Cloud Computing.csv',
    'Deloitte Time Series Analysis & Optimization': 'Deloitte Time Series Analysis & Optimization.csv',
    'Deloitte AB Testing & Business Acumen': 'Deloitte AB Testing & Business Acumen.csv'
}





# In[3]:


# Title of the app
st.title('Deloitte Data Scientists Interview Questions Selector')

# Allow the user to select a category
category = st.selectbox('Choose a category:', list(file_paths.keys()))

# Button to get random questions
if st.button('Get Random Questions'):
    # Load the selected file
    questions_df = pd.read_csv(file_paths[category])
    if 'Questions' not in questions_df.columns:
        st.error("The selected file does not contain a column named 'Questions'. Please check the file structure.")
    else:
        # Extract questions into a list
        questions_list = questions_df['Questions'].tolist()
        
        # Select 4 random questions
        selected_questions = random.sample(questions_list, min(4, len(questions_list)))
        
        # Display the questions
        for i, question in enumerate(selected_questions, start=1):
            st.write(f'Question {i}: {question}')

# Sidebar information
st.sidebar.write('Select a category and click the button to get a set of 4 random questions.')


# In[ ]:





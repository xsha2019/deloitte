#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import random

# Define the path to the CSV files (adapt these paths according to your actual file locations)
file_paths = {
    'Amazon Behavioral Questions': 'deloitte/Amazon_Behavioral_Questions.csv',
    'Amazon Technical Questions SQL': 'deloitte/Amazon_Technical_Questions_SQL.csv',
    'Data Structure and Statistics': 'deloitte/Data_structure_and_statistics.csv',
    'Data Science': 'deloitte/Data_Science.csv'
}



# In[2]:


# Title of the app
st.title('Random Question Selector')

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





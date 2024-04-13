#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import random

# Function to load data from a given sheet
def load_data(sheet_name):
    df = pd.read_excel('Deloitte_Interview_Questions.xlsx', sheet_name=sheet_name)
    return df.dropna()  # Assuming questions are in a single column without header


# Read Excel file to get sheet names
sheet_names = pd.ExcelFile('Deloitte_Interview_Questions.xlsx').sheet_names


# In[2]:


# Streamlit UI
st.title('Random Interview Questions Selector')

# Dropdown to select the sheet
selected_sheet = st.selectbox('Choose a question section:', sheet_names)

# Load data based on selection
if selected_sheet:
    data = load_data(selected_sheet)
    if st.button('Get Random Questions'):
        # Assuming questions are stored in the first column
        questions = data[data.columns[0]].tolist()  # Adjust if the structure is different
        random_questions = random.sample(questions, min(5, len(questions)))
        st.write('Here are your random questions:')
        for question in random_questions:
            st.markdown(f"- {question}")


# In[ ]:





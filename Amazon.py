#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import random

# Function to load data from the given sheet
def load_data(sheet_name):
    # Assuming the path to the Excel file is in the same directory as this script
    # Adjust the path if your file is located elsewhere
    df = pd.read_excel('Amazon_Interview_Questions.xlsx', sheet_name=sheet_name)
    # Assuming that questions are stored in the first column without headers
    return df[df.columns[0]].dropna().tolist()



# In[2]:


# Streamlit UI
st.title('Interview Question Selector from Amazon')

# Read Excel file to get sheet names for dropdown
try:
    sheet_names = pd.ExcelFile('Amazon_Interview_Questions.xlsx').sheet_names
    selected_sheet = st.selectbox('Choose a question section:', sheet_names)

    # Button to get random questions
    if st.button('Get Random Questions'):
        questions = load_data(selected_sheet)
        if len(questions) < 5:
            st.error("There are less than 5 questions in this section.")
        else:
            random_questions = random.sample(questions, 5)
            st.subheader('Here are your random questions:')
            for idx, question in enumerate(random_questions, start=1):
                st.write(f"{idx}. {question}")
except Exception as e:
    st.error(f"Failed to read the Excel file: {e}")


# In[ ]:





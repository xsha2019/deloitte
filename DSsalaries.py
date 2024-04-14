#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and setup
st.title('Data Science Salary Exploration')

# Load the data
#@st.cache
def load_data():
    data = pd.read_csv('Data_Science_Salaries.csv')
    return data



# In[16]:


data = load_data()

# Title of the app
st.title('Data Science Salary Exploration')

# Sidebar for user inputs and settings
st.sidebar.title("Settings")
selected_year = st.sidebar.slider("Select the year", min_value=int(data['Year'].min()), max_value=int(data['Year'].max()), value=int(data['Year'].max()))
filtered_data = data[data['Year'] == selected_year]

# Display filters based on job title and company location
job_title = st.sidebar.selectbox('Select a job title:', options=['All'] + list(data['Job Title'].unique()))
if job_title != 'All':
    filtered_data = filtered_data[filtered_data['Job Title'] == job_title]

country = st.sidebar.selectbox('Select a country:', options=['All'] + list(data['Company Location'].unique()))
if country != 'All':
    filtered_data = filtered_data[filtered_data['Company Location'] == country]

# Question 1: Average salary by job title
st.header("1. Average Salary by Job Title")
avg_salary_by_job = filtered_data.groupby('Job Title')['Salary in USD'].mean().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots()
sns.barplot(x=avg_salary_by_job.values, y=avg_salary_by_job.index, ax=ax1)
ax1.set_xlabel('Average Salary in USD')
ax1.set_ylabel('Job Title')
st.pyplot(fig1)

# Question 2: Salary variation by experience level
st.header("2. Salary Variation by Experience Level")
salary_by_experience = filtered_data.groupby('Experience Level')['Salary in USD'].mean().sort_values()
fig2, ax2 = plt.subplots()
sns.barplot(x=salary_by_experience.values, y=salary_by_experience.index, ax=ax2)
ax2.set_xlabel('Average Salary in USD')
ax2.set_ylabel('Experience Level')
st.pyplot(fig2)

# Question 3: Compare salaries between experts and non-experts
st.header("3. Salary Comparison: Experts vs. Non-Experts")
expert_salary = filtered_data[filtered_data['Expertise Level'] == 'Expert']['Salary in USD']
non_expert_salary = filtered_data[filtered_data['Expertise Level'] != 'Expert']['Salary in USD']
fig3, ax3 = plt.subplots()
sns.histplot(expert_salary, color="red", label='Experts', kde=True, ax=ax3)
sns.histplot(non_expert_salary, color="blue", label='Non-Experts', kde=True, ax=ax3)
ax3.set_xlabel('Salary in USD')
ax3.set_ylabel('Frequency')
ax3.legend()
st.pyplot(fig3)

# Question 4: Impact of employment type on salary
st.header("4. Impact of Employment Type on Salary")
salary_by_employment_type = filtered_data.groupby('Employment Type')['Salary in USD'].mean().sort_values()
fig4, ax4 = plt.subplots()
sns.barplot(x=salary_by_employment_type.values, y=salary_by_employment_type.index, ax=ax4)
ax4.set_xlabel('Average Salary in USD')
ax4.set_ylabel('Employment Type')
st.pyplot(fig4)

# Question 5: Highest average salary by country
st.header("5. Highest Average Salary by Country")
avg_salary_by_country = filtered_data.groupby('Company Location')['Salary in USD'].mean().sort_values(ascending=False).head(10)
fig5, ax5 = plt.subplots()
sns.barplot(x=avg_salary_by_country.values, y=avg_salary_by_country.index, ax=ax5)
ax5.set_xlabel('Average Salary in USD')
ax5.set_ylabel('Country')
st.pyplot(fig5)

# Question 6: How company size affects salaries
st.header("6. How Company Size Affects Salaries")
salary_by_company_size = filtered_data.groupby('Company Size')['Salary in USD'].mean().sort_values()
fig6, ax6 = plt.subplots()
sns.barplot(x=salary_by_company_size.values, y=salary_by_company_size.index, ax=ax6)
ax6.set_xlabel('Average Salary in USD')
ax6.set_ylabel('Company Size')
st.pyplot(fig6)

# Question 7: Trends in data science salaries over the years
st.header("7. Trends in Data Science Salaries Over the Years")
salary_trends_over_years = data.groupby('Year')['Salary in USD'].mean()
fig7, ax7 = plt.subplots()
sns.lineplot(x=salary_trends_over_years.index, y=salary_trends_over_years.values, ax=ax7)
ax7.set_xlabel('Year')
ax7.set_ylabel('Average Salary in USD')
st.pyplot(fig7)

# Question 8: Salary distribution within the United States
st.header("8. Salary Distribution in the United States")
us_salaries = filtered_data[filtered_data['Company Location'] == 'United States']['Salary in USD']
fig8, ax8 = plt.subplots()
sns.histplot(us_salaries, bins=30, kde=True, ax=ax8)
ax8.set_xlabel('Salary in USD')
ax8.set_ylabel('Frequency')
st.pyplot(fig8)



# Question 9: Common job titles and their frequency
st.header("9. Common Job Titles and Their Frequency")
job_title_counts = filtered_data['Job Title'].value_counts().head(10)
fig10, ax10 = plt.subplots()
job_title_counts.plot(kind='bar', ax=ax10)
ax10.set_xlabel('Job Title')
ax10.set_ylabel('Frequency')
st.pyplot(fig10)

# Ensure that visualizations fit the data and consider adding more interactive features to refine user input and data filtering.


# In[ ]:





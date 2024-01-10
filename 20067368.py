#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your ID number and name
student_id = '20067368'
student_name = 'chinni raj paul juthiga'

# Provide the path to your CSV file on your local machine
file_path = 'Economic Indicators 2014.csv'

# Read data from CSV file
df = pd.read_csv('Economic Indicators 2014.csv')

# Set a consistent figure size for all subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))

# Bar plot of GDP for each country with rotated x-axis labels
sns.barplot(x='Country Name', y='GDP', data=df, palette='viridis', ax=axes[0, 0])
axes[0, 0].set_title('GDP for Each Country')
axes[0, 0].set_xticklabels(df['Country Name'], rotation=45, ha='right')  # Rotate x-axis labels for better visibility
# axes[0, 0].text(0.5, -0.15, f'Student ID: {student_id}\nStudent Name: {student_name}', ha='center', va='center', transform=axes[0, 0].transAxes)

# Horizontal bar plot for Life Expectancy at Birth
sns.barplot(x='LEB', y='Country Name', data=df, palette='viridis', ax=axes[0, 1])
axes[0, 1].set_title('Life Expectancy at Birth for Each Country')
# axes[0, 1].text(0.5, -0.15, f'Student ID: {student_id}\nStudent Name: {student_name}', ha='center', va='center', transform=axes[0, 1].transAxes)

# Bar chart for External Sector Expenditure (ESE)
selected_countries = df.head(5)
axes[1, 0].bar(selected_countries['Country Name'], selected_countries['ESE'], color='skyblue')
axes[1, 0].set_title('External Sector Expenditure (ESE) for Top 5 Countries')
axes[1, 0].set_xlabel('Country')
axes[1, 0].set_ylabel('ESE')
# axes[1, 0].text(0.5, -0.15, f'Student ID: {student_id}\nStudent Name: {student_name}', ha='center', va='center', transform=axes[1, 0].transAxes)

# Pie chart for Life Expectancy at Birth with visible labels
life_expectancy_labels = df['Country Name'].head(5)
life_expectancy_sizes = df['LEB'].head(5)

axes[1, 1].pie(life_expectancy_sizes, labels=life_expectancy_labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3), textprops={'fontsize': 10})
axes[1, 1].set_title('Life Expectancy at Birth Distribution (Top 5 Countries)')
axes[1, 1].text(0.5, -0.15, f'Student ID: {student_id}\nStudent Name: {student_name}', ha='center', va='center', transform=axes[1, 1].transAxes)

# No need to use plt.tight_layout() since we are saving individual subplots

# Save individual plots
plt.savefig('gdp_plot.png')
plt.savefig('life_expectancy_plot.png')
plt.savefig('ese_plot.png')

# Save the combined plot (optional)
plt.savefig('combined_plot.png')

# Show or save the combined plot (optional)
plt.show()


# In[ ]:





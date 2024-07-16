import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the kaggle csv
custs = pd.read_csv('marketing_campaign.csv', delimiter='\t')  # specify the delimiter of the csv

# Introduction to the data
print(custs.head())  # grab the first 5 records
print(custs.describe())  # grab the statistical info about it
print(custs.info())  # info about the dataset
print(custs.shape)  # shape of the customers
print(custs.columns)  # give in a list the columns
print(custs.index)  # same for the indexes

# Explanatory Data Analysis

# 1) What is the top 5 most common education levels in this dataset?
print(custs['Education'].value_counts().head(5))

# Visualizing the top 5 most common education levels
plt.figure(figsize=(10, 6))
sns.countplot(y='Education', data=custs, order=custs['Education'].value_counts().index)
plt.title('Top 5 Most Common Education Levels')
plt.xlabel('Count')
plt.ylabel('Education Level')
plt.show()

# 2) How many people are born after 1988?
print(custs[custs['Year_Birth'] >= 1988].count())

# Visualizing the distribution of birth years
plt.figure(figsize=(10, 6))
sns.histplot(custs['Year_Birth'], bins=30, kde=True)
plt.axvline(1988, color='r', linestyle='dashed', linewidth=1)
plt.title('Distribution of Birth Years')
plt.xlabel('Year of Birth')
plt.ylabel('Count')
plt.show()

# 3) How many distinct values are there in the complain field and what is their meaning?
print(custs['Complain'].value_counts())

# Visualizing the complain field
plt.figure(figsize=(10, 6))
sns.countplot(x='Complain', data=custs)
plt.title('Distribution of Complaints')
plt.xlabel('Complaint')
plt.ylabel('Count')
plt.show()

# 4) What is the average income for each marital status?
print(custs['Marital_Status'].value_counts())
print(custs.groupby('Marital_Status')['Income'].mean())

# Visualizing the average income for each marital status
plt.figure(figsize=(10, 6))
sns.barplot(x='Marital_Status', y='Income', data=custs, estimator=np.mean)
plt.title('Average Income for Each Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Average Income')
plt.show()

# 5) Which marital status has the biggest mean income?
aux_custs = custs.groupby('Marital_Status')['Income'].mean()
print("The marital status with the maximum average salary({}) is {}.".format(aux_custs.max(), aux_custs.idxmax()))

# 6) Does the data have any null values and if so how many are there?
print(custs.isnull().sum())

# Visualizing the null values in the dataset
plt.figure(figsize=(10, 6))
sns.heatmap(custs.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Values')
plt.show()

# 7) Find how many customers have the Date of customer's enrollment with the company later than 2012
custs['Dt_Customer'] = pd.to_datetime(custs['Dt_Customer'])
print(custs['Dt_Customer'].dtype)

custs['Year_Customer'] = custs['Dt_Customer'].dt.year
print(custs[custs['Year_Customer'] > 2012].shape[0])

# Visualizing the count of customers enrolled each year
plt.figure(figsize=(10, 6))
sns.histplot(custs['Year_Customer'], bins=20, kde=True)
plt.axvline(2012, color='r', linestyle='dashed', linewidth=1)
plt.title('Distribution of Customer Enrollment Years')
plt.xlabel('Year of Enrollment')
plt.ylabel('Count')
plt.show()

# 8) How many customers have a Teenhome count greater than 0 and recency more than the average?
def teenhome_greater_than_one_and_recency_greater_than_avg(custs):
    return len(custs[(custs['Recency'] > custs['Recency'].mean()) & (custs['Teenhome'] > 0)])

print(str(teenhome_greater_than_one_and_recency_greater_than_avg(custs)))

# Visualizing the Recency and Teenhome count
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Recency', y='Teenhome', data=custs)
plt.axhline(0, color='r', linestyle='dashed', linewidth=1)
plt.axvline(custs['Recency'].mean(), color='g', linestyle='dashed', linewidth=1)
plt.title('Recency vs Teenhome Count')
plt.xlabel('Recency')
plt.ylabel('Teenhome Count')
plt.show()

# Additional Visualizations

# 9) Income Distribution
plt.figure(figsize=(10, 6))
sns.histplot(custs['Income'], bins=30, kde=True)
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Count')
plt.show()

# 10) Spending on Different Product Categories
product_categories = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
custs['Total_Spending'] = custs[product_categories].sum(axis=1)

plt.figure(figsize=(10, 6))
sns.histplot(custs['Total_Spending'], bins=30, kde=True)
plt.title('Total Spending Distribution')
plt.xlabel('Total Spending')
plt.ylabel('Count')
plt.show()

# 11) Heatmap of Correlation Matrix
plt.figure(figsize=(14, 12))
sns.heatmap(custs.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

# 12) lmplot of Income vs Total Spending with hue as Marital Status
plt.figure(figsize=(10, 6))
sns.lmplot(x='Income', y='Total_Spending', hue='Marital_Status', data=custs, aspect=2, height=6)
plt.title('Income vs Total Spending by Marital Status')
plt.xlabel('Income')
plt.ylabel('Total Spending')
plt.show()

# 13) Violin plot of Income by Education Level
plt.figure(figsize=(10, 6))
sns.violinplot(x='Education', y='Income', data=custs)
plt.title('Income Distribution by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Income')
plt.show()

# 14) Box plot of Total Spending by Marital Status
plt.figure(figsize=(10, 6))
sns.boxplot(x='Marital_Status', y='Total_Spending', data=custs)
plt.title('Total Spending by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Total Spending')
plt.show()


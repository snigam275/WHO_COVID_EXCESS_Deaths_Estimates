#importing required dataset to work on it
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
file_path = "C:\\Users\\shrey\\Desktop\\Python_dashboard_excel_sheet\\WHO_COVID_EXCESS_Deaths_Estimates_by_country.xlsx"
data = pd.read_excel(file_path)
data

#To display the information of the dataset
data.info()
data.head()
print("\nSummary of the dataset: \n",data.describe())
print("\nColumn Names:\n", data.columns)
print("\nUnique Values:\n ",data.nunique())  #use to count unique values.


#Handling the missing data
print("\nMissing Values in Each Column:\n",data.isnull().sum())
print("\nIf null values, then fill with NaN: \n", data.dropna())  #use to replace (if there) any null values present in the dataset with NaN

#(If we want to delete specific column or row, we use drop() with label/index of column or row)
print("\nDelete specific column:\n",data.drop(columns=["iso3"]))

#Objectives achieves from the dataset
# 1) Yearly Excess Death Trends

#Creating a bar graph to represent the yearly excess death trend and summarise excess death of each year of pandemic(mostly 2020,2021)across all countries 
# Group by year and sum the excess deaths
yearly_trend = data.groupby("year")["excess.mean*"].sum()

# Plotting
plt.figure(figsize=(5, 4))
yearly_trend.plot(kind="bar", color=["Red","Green"], edgecolor="black")

# Add labels and title and legends
plt.title("Yearly Excess Death Trend (Global)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Total Excess Deaths")
plt.legend("excess_death",loc="upper left")
# Show plot
plt.show()

# Yearly Excess Death Trend by age group 
age_trend = data.groupby(["year", "age_group"])["excess.mean*"].sum()
cl = ["green","blue","red"]
age_trend.plot(kind='bar', color=cl, figsize=(10, 7))
plt.title("Yearly Excess Death Trend by Age Group")
plt.xlabel("Year with Age")
plt.ylabel("Total Excess Deaths")
plt.legend("Group",loc="upper left")


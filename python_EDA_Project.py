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

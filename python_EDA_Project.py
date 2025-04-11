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

# 2) Country wise Comparison of Excess deaths

#Creating a scatter plot to show country-wise comparison of Excess deaths during pandemic
grouped = data.groupby(['country', 'year'])['excess.mean*'].sum().reset_index()

# Get excess deaths for 2020
excess_2020 = grouped[grouped['year'] == 2020][['country', 'excess.mean*']].rename(columns={'excess.mean*': 'Excess_2020'})

# Get excess deaths for 2021
excess_2021 = grouped[grouped['year'] == 2021][['country', 'excess.mean*']].rename(columns={'excess.mean*': 'Excess_2021'})

# Merge the two years on country
merged_data = pd.merge(excess_2020, excess_2021, on='country')

# Create the scatter plot
plt.figure(figsize=(7, 4))
sns.scatterplot(data=merged_data,x='Excess_2020',y='Excess_2021',hue='country',palette='tab20',s=100,alpha=0.6,legend=False)

# Labels and title
plt.title("Country-wise Excess Deaths: 2020 vs 2021", fontsize=14)
plt.xlabel("Excess Deaths in 2020",fontsize=12)
plt.ylabel("Excess Deaths in 2021",fontsize=12)
plt.show()

# 3)Age-group wise COVID impact 

#Creating a barplot to show the impact of COVID on different age group during pandemic

age_data = data[['age_group', 'excess.mean*']].dropna()
age_data = age_data[age_data['excess.mean*'] >= 0]

# Group by age group and sum the excess deaths
age_summary = age_data.groupby('age_group', as_index=False)['excess.mean*'].sum()

# Create the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='age_group', y='excess.mean*', data=age_summary, hue='age_group', palette='viridis',legend=False)

# Label the axes and title
plt.xlabel('Age Group')
plt.ylabel('Excess Deaths')
plt.title('COVID-19 Impact by Age Group')

plt.show() 

# 4) Top 10 countries with the highest Excess Death

#Creating a pie chart to show the top 10 countries with highest excess death during pandemic

# Group by country and sum excess deaths across all years
country_deaths = data.groupby('country')['excess.mean*'].sum().reset_index()

# Sort and get top 10 countries
top10 = country_deaths.sort_values(by='excess.mean*', ascending=False).head(10)

# Plot pie chart
plt.figure(figsize=(9, 7))
#clr = ['Skyblue', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'gray']
clr =  plt.cm.tab20.colors # A colormap with 10 distinct colors 
plt.pie(top10['excess.mean*'], labels=top10['country'], autopct='%1.1f%%', startangle=160,colors=clr,textprops={'fontsize': 10})

# Label the title
plt.title('Top 10 Countries by Total Excess Deaths (COVID-19)', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures pie chart is a circle 

plt.show()

# 5) Expected vs Actual Excess Death

#Creating a line graph  to show the top 10 countries with highest excess death during pandemic

# Plot line graph for all data points
plt.figure(figsize=(10,5))

# Plot expected deaths (all countries, years, age groups)
#here
 # X-axis: age groups
# Y-axis: expected deaths
#alpha=0.5,  # Transparency to handle overlapping points
plt.plot(data['age_group'],  data['expected.mean'],  linestyle='--',marker='D', color='blue', alpha=0.5,label='Expected Deaths (All Data)')

# Plot excess deaths (all countries, years, age groups)
plt.plot(data['age_group'],data['excess.mean*'],linestyle='-',marker='o', markeredgecolor='yellow', markerfacecolor='red',color='green',alpha=0.7,label='Excess Deaths')

# Formatting
plt.title('Expected vs. Actual Excess Deaths Across All Countries in different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Number of Deaths')
plt.grid(True)
plt.show()

#To visually analyze the relationships between different COVID death metrics (expected, actual, and excess) and see how they differ based on gender
#Select numeric and one categorical column and check the missing values in column
selected_columns = ['expected.mean', 'acm.mean', 'excess.mean*', 'sex']
pair_data = data[selected_columns].dropna()

#Set a clean and readable style
sns.set(style="whitegrid")

#Creating the pairplot with color coding by 'sex'
pairplot = sns.pairplot(pair_data,hue='sex',palette='bright',diag_kind='kde',height=3,plot_kws={'alpha': 0.7, 's': 50, 'edgecolor': 'k'},corner=False)

#Add title
pairplot.fig.suptitle("Pairplot of COVID Death Estimates Grouped by Sex", fontsize=14, y=1.02)

#To analyze the relationships between expected.mean, acm.mean, and excess.mean* values — and see how they vary across different age groups

selected_columns = ['expected.mean', 'acm.mean', 'excess.mean*', 'age_group']
pair_data = data[selected_columns].dropna()  #Drop rows with missing values
sns.set(style="whitegrid")  #Set a clean and readable style

#Create the pairplot with color coding by age_group
pairplot = sns.pairplot(pair_data,hue='age_group',palette='Paired',diag_kind='kde',height=3,plot_kws={'alpha': 0.7,'s': 50,'edgecolor':'k'},corner=False)

#Add title
pairplot.fig.suptitle("Pairplot of COVID Death Estimates Grouped by Age", fontsize=14, y=1.02)
plt.show()

#visualize the relationship between COVID-19 related death metrics (expected.mean, acm.mean, and excess.mean*) using a correlation heatmap.
# Select only numerical columns
columns = ['expected.mean', 'acm.mean', 'excess.mean*']
numeric_data = data[columns].dropna()

# Calculate correlation matrix
correlation = numeric_data.corr()

# Set style
sns.set(style="white")

# Create the heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Between COVID Death Metrics")
plt.show()

#visualize outliers in the "excess.mean*" column based on the year using a boxplot.
# Drop rows with missing values in 'excess.mean*'
data = data.dropna(subset=['excess.mean*'])

# Calculate IQR to find outliers
Q1 = data['excess.mean*'].quantile(0.25)
Q3 = data['excess.mean*'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find the outliers
outliers = data[(data['excess.mean*'] < lower_bound) | (data['excess.mean*'] > upper_bound)]

# Print how many outliers are found
print("Number of outliers:", len(outliers))

# Plot the boxplot for Excess Deaths by Year
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='year', y='excess.mean*')
plt.title("Boxplot: Excess Deaths by Year (with Outliers)")
plt.show()

#visualize the distribution and outliers of excess deaths across the top 20 countries (by data availability) using a boxplot
data = data.dropna(subset=['excess.mean*'])

# Calculate IQR to find outliers
Q1 = data['excess.mean*'].quantile(0.25)
Q3 = data['excess.mean*'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find the outliers
outliers = data[(data['excess.mean*'] < lower_bound) | (data['excess.mean*'] > upper_bound)]
print("Number of outliers:", len(outliers))

# Get top 20 countries by number of rows
top_countries = data['country'].value_counts().head(20).index

# Filter the data for only these top 20 countries
data_top = data[data['country'].isin(top_countries)]

# Plot boxplot for excess deaths by top 20 countries
plt.figure(figsize=(10, 7))
sns.boxplot(data=data_top, x='country', y='excess.mean*')
plt.title("Boxplot: Excess Deaths by Top 20 Countries")
plt.show()

# WHO_COVID_EXCESS_Deaths_Estimates
EDA on Dataset containing WHO estimates of excess mortality by country associated with the COVID-19 pandemic.A data-driven project analyzing WHO's estimates of excess COVID-19 deaths by country to assess the pandemic's true global impact.
This project aims to:
1) Analyze and visualize WHO's COVID-19 excess death estimates by country to understand pandemic impact.
2) Perform data cleaning and summarization to gain insights.
3) Visualize key trends using scatter plots, line graphs, boxplots, pie charts, and more.
4) Detect outliers and patterns in excess COVID-19 death estimates across countries using WHO data.
5) Provide a clear, visual analysis of excess COVID-19 death estimates by country to support decision-making and reporting
---   
# 📌**Overview of Dataset**
- ## Dataset Name
  WHO_COVID_EXCESS_Deaths_Estimates_by_country
- ## Purpose
  To analyze excess mortality caused by the COVID-19 pandemic, using data provided by WHO across countries, years, sexes, and age groups.
- ## Columns
  * Country : Represent the name of the country present in the dataset
  * iso3 : 3-letter ISO code identifying each country uniquely
  * Year : The year of data entry
  * Sex : Represent gender category
  * Age_group : The age bracket of the population
  * Type : Type of estimation used
  * Expected.mean : Predicted number of deaths based on historical data if there had been no pandemic.
  * acm.mean (All-Cause Mortality) : Actual number of reported deaths during the pandemic.
  * excess.mean : The difference between actual and expected deaths—indicating excess mortality, possibly due to COVID-19
---
# 🗂️**Features & Visualizations**
  ## 🎯Features 
- ### 📌 1. Data OverView
  This project analyzes the excess deaths during the COVID-19 pandemic using WHO-provided datasets. It focuses on country-wise comparisons, age-group impacts, and temporal trends for the years 2020 
  and 2021.
- ### 📌 2. Data Cleaning
  * Removed NaN and negative excess death values.
  * Focused on country, year, and age_group for core analysis.
- ### 📌 3. Feature Engineering
  * Grouped total excess deaths by country and year.
  * Extracted top countries and trends by time and demographics
--- 
  ## 📈 Visualizations
- ### 📌 1. Age-Group Wise COVID Impact (Bar Plot)
  Shows how various age groups were affected. Elderly groups often show higher 
  excess 
  deaths.
- ### 📌 2. Country-Wise Comparison: 2020 vs 2021 (Scatter Plot)
  Helps visualize trends and countries with increasing or decreasing deaths year 
  over 
  year.
- ### 📌 3. Top 10 Countries by Excess Deaths (Pie Chart)
  * Dynamic pie chart using tab20 or gradient colors.
  * Percentage of global excess deaths attributed to each country.
- ### 📌 4. COVID-19 Impact by Age Group
  * Bar plot showing total excess deaths for each age group.
- ### 📌 5. Expected vs. Actual Excess Deaths by Age Group
  * Line plot comparing expected vs actual excess deaths across age groups.
- ### 📌 6. Pairplot: Death Estimates Grouped by Sex
  * Pairplot showing relationships between expected.mean, acm.mean, excess.mean*, 
    colored by sex.
- ### 📌 7. Pairplot: Death Estimates Grouped by Age Group
  * Pairplot showing the same metrics, colored by age group.
- ### 📌 8. Boxplot of Excess Deaths by Year
  * Boxplot visualizing distribution and outliers of excess deaths per year.
- ### 📌 9. Boxplot of Excess Deaths for Top 20 Countries
  * Boxplot showing distribution and outliers of excess deaths across top 20 
    countries (by data availability).

--- 
# 💻**Technologies Used**
    * Language 
      Python
    * Libraries :
       *Numpy
       *Pandas
       *Matplotlib
       *Seaborn

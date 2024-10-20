# Maji Ndogo: Automating Farming with Data-Driven Insights

## Introduction
Welcome to the Maji Ndogo project! This initiative focuses on automating farming practices in Maji Ndogo, a region known for its diverse and challenging agricultural landscapes. The key to successful automation isn't just about technology—it's about making well-informed decisions based on an in-depth analysis of geographical, climate, and soil data.

Our goal is to determine where and what crops to plant by analyzing various factors such as rainfall, soil fertility, climate, and topography. This project's analysis will serve as the groundwork for future automation, helping farmers optimize crop selection based on the land’s natural characteristics.

We'll be working with a dataset stored in an SQLite database, which contains multiple tables. The challenge is to clean, organize, and merge these tables into a single DataFrame for analysis. By uncovering patterns in the data, we aim to make informed recommendations on how to automate farming operations in Maji Ndogo.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data Dictionary](#data-dictionary)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Project Workflow](#project-workflow)
   - [Data Cleaning](#data-cleaning)
   - [Data Analysis](#data-analysis)
   - [Crop Recommendations](#crop-recommendations)
5. [Future Work](#future-work)
6. [License](#license)
7. [Visualizing Data](#visualizing-data)
8. [How to Run](#how-to-run)

## Project Overview
The Maji Ndogo project aims to optimize farming practices by leveraging data analytics. By analyzing variables such as soil fertility, climate conditions, and geographical data, we aim to identify the most suitable locations for planting various crops. This information will be crucial for automating farming practices and increasing yields across the region.

The dataset consists of multiple tables in an SQLite database, which we'll clean, merge, and analyze to generate actionable insights for sustainable agriculture in Maji Ndogo.

## Data Dictionary
The dataset consists of several features grouped into four main categories: 

### Geographic Features
- **Field_ID**: Unique identifier for each field (BigInt).
- **Elevation**: Elevation of the field above sea level (Float).
- **Latitude**: Latitude of the field (Float).
- **Longitude**: Longitude of the field (Float).
- **Location**: Province where the field is located (Text).
- **Slope**: Slope of the land in the field (Float).

### Weather Features
- **Field_ID**: Corresponding field identifier (BigInt).
- **Rainfall**: Amount of rainfall in the area (mm) (Float).
- **Min_temperature_C**: Average minimum temperature recorded (Celsius) (Float).
- **Max_temperature_C**: Average maximum temperature recorded (Celsius) (Float).
- **Ave_temps**: Average temperature (Celsius) (Float).

### Soil and Crop Features
- **Field_ID**: Corresponding field identifier (BigInt).
- **Soil_fertility**: Soil fertility measure (0 for infertile, 1 for very fertile) (Float).
- **Soil_type**: Type of soil (Text).
- **pH**: pH level of the soil (Float).

### Farm Management Features
- **Field_ID**: Corresponding field identifier (BigInt).
- **Pollution_level**: Pollution level (0 for unpolluted, 1 for very polluted) (Float).
- **Plot_size**: Size of the plot in hectares (Float).
- **Chosen_crop**: Type of crop chosen for cultivation (Text).
- **Annual_yield**: Total annual output from the field (Float).
- **Standard_yield**: Standardized yield expected, normalized per crop (Float).

### Average Yield (tons/Ha) per Crop:
- **Coffee**: 1.5 tons/Ha
- **Wheat**: 3 tons/Ha
- **Rice**: 4.5 tons/Ha
- **Maize**: 5.5 tons/Ha
- **Tea**: 1.2 tons/Ha
- **Potato**: 20 tons/Ha
- **Banana**: 30 tons/Ha
- **Cassava**: 13 tons/Ha

## Getting Started

### Prerequisites
- Python 3.x
- SQLite3 for handling the database
- Libraries like `pandas`, `numpy`, and `matplotlib` for data manipulation and visualization.

### Installation
Clone the repository:

```bash
git clone https://github.com/birdcoreone/Maji-Ndogo-Farming-Project.git
cd Maji-Ndogo-Farming-Project
```

### Install the required Python libraries:
```bash
pip install -r requirements.txt
```
## Project Workflow
### Data Loading Example
Below is an example of how we loaded the dataset from the SQLite database:
```python
import pandas as pd # importing the Pandas package with an alias, pd
from sqlalchemy import create_engine, text # Importing the SQL interface. If this fails, run !pip install sqlalchemy in another cell.

# Create an engine for the database
engine = create_engine('sqlite:///Maji_Ndogo_farm_survey_small.db') #Make sure to have the .db file in the same directory as this notebook, and the file name matches.

#Next, we'll write an SQL query to join our tables. Combine all of the tables into a single query, using Field_ID

sql_query = """
-- This query joins multiple tables.... In SQL, --

SELECT *
FROM geographic_features AS g
JOIN weather_features AS w ON g.Field_ID = w.Field_ID
JOIN soil_and_crop_features AS s ON g.Field_ID = s.Field_ID
JOIN farm_management_features AS f ON g.Field_ID = f.Field_ID
"""
```
## Data Cleaning
The initial dataset might have missing or inconsistent data. We'll clean it by:

- Handling missing values.
- Normalizing data formats.
- Removing any duplicates.

## Data Analysis
We'll analyze the dataset to identify patterns such as:

- The impact of rainfall and soil type on crop yield.
- Optimal crops for different provinces based on environmental factors.

For example, to calculate the average standard yield by crop type:
```python
average_yield_per_crop = df.groupby('Chosen_crop')['Standard_yield'].mean()
average_yield_per_crop.plot(kind='bar', title='Average Standard Yield per Crop')
```
## Crop Recommendations
After analyzing the data, we can provide recommendations for each field, such as:

- Best crops to plant based on soil fertility, rainfall, and temperature.
- Expected yields per hectare for each recommended crop.

## Future Work
- Develop machine learning models to predict future yields.
- Integrate real-time weather data to make dynamic farming recommendations.
- Expand the project to include other agricultural regions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Visualizing Data
We can visualize the data to get a better understanding of trends.
### Bar Plot of Average Yield per Crop
```python
df.groupby('Chosen_crop')['Standard_yield'].mean().plot(kind='bar', title='Average Yield per Crop')
```
### Histogram of Standard Yield
```python
df['Standard_yield'].plot(kind='hist', bins=20, title='Standard Yield Distribution')
```
### Scatter Plot of Pollution Level vs. Standard Yield
```python
df.plot(kind='scatter', x='Pollution_level', y='Standard_yield', title='Pollution Level vs. Yield')
```
## How to Run
To reproduce this analysis on your local machine:

1. Clone the repository:
```bash
git clone https://github.com/birdcoreone/Maji-Ndogo-Farming-Project.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Python scripts: You can run the analysis scripts from the `scripts/` folder:
```bash
python scripts/data_analysis.py
```
4. Or open the Jupyter notebook: 
Open the notebooks/analysis.ipynb in Jupyter to see step-by-step explanations, code, and visualizations:
```bash
jupyter notebook notebooks/Maji_Ndogo_farm_automation.ipynb
```
## Running on Google Colab
You can also run this notebook on Google Colab by following these steps:

1. Open the notebook link in Google Colab:

   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/birdcoreone/Maji-Ndogo-Farming-Automation/blob/main/notebooks/Maji_Ndogo_farm_automation.ipynb)

2. Ensure the required libraries are installed by running the first cell, which contains the !pip install commands for the necessary dependencies.

3. Continue running the rest of the notebook cells as needed.



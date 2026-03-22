import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Show first 5 rows
print(df.head())

# -------------------------------
# STEP 3: UNDERSTAND DATA
# -------------------------------

# Basic information about dataset
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Column names
print("\nColumn Names:")
print(df.columns)


# -------------------------------
# STEP 4: DATA CLEANING
# -------------------------------

# Check missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Fill missing values with mean (only numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Check again after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())



# -------------------------------
# STEP 5: DATA ANALYSIS
# -------------------------------

# Average scores
print("\nAverage Scores:")
print(df[['math score', 'reading score', 'writing score']].mean())

# Maximum scores
print("\nMaximum Scores:")
print(df[['math score', 'reading score', 'writing score']].max())

# Minimum scores
print("\nMinimum Scores:")
print(df[['math score', 'reading score', 'writing score']].min())
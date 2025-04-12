import pandas as pd

df = pd.read_csv("seattle-weather.csv")

#Check for any missing values
print(df.isnull().sum())

#Drop rows with missing values and assign to value "df cleaned"
df_cleaned = df.dropna()

#Fill missing values with mean for numerical data and assign to variable df filled
df_filled = df.fillna(df.mean(numeric_only=True))


print(df.head())
print(df.describe())
print(df.info())

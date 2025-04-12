import pandas as pd

df = pd.read_csv("seattle-weather.csv")

#Check for any missing values
print(df.isnull().sum())

#Drop rows with missing values and assign to value "df cleaned"
df_cleaned = df.dropna()

#Fill missing values with mean for numerical data and assign to variable df filled
df_filled = df.fillna(df.mean(numeric_only=True))

#Replace missing values with mean of each column
#df.fillna(df.mean(), inplace=True)

#Identifying duplicates
print(df.duplicated().sum())

#Removing duplicats
df_no_duplicats = df.drop_duplicates()



print(df.head())
print(df.describe())
print(df.info())

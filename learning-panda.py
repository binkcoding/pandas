import pandas as pd

df = pd.read_csv("seattle-weather.csv")

#Check for any missing values
print(df.isnull().sum())

#Drop rows with missing values and assign to value "df cleaned"
df_cleaned = df.dropna()

#Fill missing values with mean for numerical data and assign to variable df filled
df_filled = df.fillna(df.mean(numeric_only=True))

#Replace missing values with mean of each column
df.fillna(df.mean(), inplace=True)

#Identifying duplicates
print(df.duplicated().sum())

#Removing duplicats
df_no_duplicats = df.drop_duplicates()

#Convert data types to other data types
df['Column 1'] = df['Column1'].astype(float)

#Convert categorical data to numerical data
# df_encode = pd.get_dummies(df, columns=[car_brand])

#Identifying outliers
Q1 = df["precipitation"].quantile(0.25)
Q3 = df["temp_max"].quantile(0.75)
IQR = Q3 - Q1


#Find out what each column data type is
print(df.dtypes)

print(df.head())
print(df.describe())
print(df.info())

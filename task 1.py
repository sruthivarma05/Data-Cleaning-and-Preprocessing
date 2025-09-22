import pandas as pd

df = pd.read_csv(r"netflix_titles.csv")

#handling missing values
#filling as "unknown"
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)
df['country'].fillna("Unknown", inplace=True)
#filling common date
df['date_added'].fillna("01-01-2000", inplace=True)
#mode method
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
#dropping rows since there are only 3 rows with missing values for duration column
df = df.dropna(subset=['duration'])
print(df.isnull().sum())

#removing duplicates
#there are no duplicates
df = df.drop_duplicates()

#standardizing text values
#removing extra spaces and converting to lowercase
df['type']=df['type'].str.strip().str.lower()
#Converting specific columns to title case
df['title'] = df['title'].str.title()
df['director'] = df['director'].str.title()
df['cast'] = df['cast'].str.title()
df['country'] = df['country'].str.title()
#converting to uppercase
df['rating'] = df['rating'].str.upper()

#Converting to datetime type first
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', dayfirst=True)
#Formating as dd-mm-yyyy
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

print(df['date_added'].head(10))

#Renaming column headers to lowercase, removing spaces and replacing spaces with underscores
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_").str.replace("-", "_")

#checking datatypes
print(df.dtypes)
#converting to the datetime type (datetime64[ns]) in Pandas.
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', dayfirst=True)
print(df.dtypes)
df['date_added'].fillna("01-01-2000", inplace=True)

#number of missing values
print("Missing values per column:")
print(df.isnull().sum())
print("-"*50)

#number of duplicate rows
print("Number of duplicate rows:", df.duplicated().sum())
print("-"*50)

#Check data types
print("Data types of each column:")
print(df.dtypes)
print("-"*50)

#Preview first 10 rows
print("First 10 rows of the dataset:")
print(df.head(10))










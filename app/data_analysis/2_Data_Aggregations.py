import pandas as pd
from app.config.AppSettings import AppSettings
from github import Github, Auth
from io import StringIO

settings = AppSettings()

auth = Auth.Token(settings._token)
g = Github(auth=auth)

repo = g.get_repo(settings._common_url)
cleaned_csv_url = settings._cleaned_files_path + settings._cleaned_csv_path

contents = repo.get_contents(cleaned_csv_url, ref="main")
decoded_csv_content = contents.decoded_content.decode()

csv_data = StringIO(decoded_csv_content)

#Reading Cleaned CSV
df = pd.read_csv(csv_data, sep=",", header=0, skipinitialspace=True)

#Overall picture of the data
df.head()

#Subset of data for further processing
df_group_by = df[["Fuel_Type", "Kilometers_Driven", "Price", "Car_Age"]]

#Arithmetic Mean
df_group_by.groupby("Fuel_Type").mean()

#Median
df_group_by.groupby("Fuel_Type").median()

#Minimum
df_group_by.groupby("Fuel_Type").min()

#Maximum
df_group_by.groupby("Fuel_Type").max()

#Sum
df_group_by.groupby("Fuel_Type").sum()

#Creating data frame for pivot table processing
df_pivot = df[["Location", "Year", "Fuel_Type", "Kilometers_Driven", "Price", "Car_Age"]]

# Pandas Pivot table with defaults (Aggregation is mean)
pd.pivot_table(df_pivot, index=["Location", "Year", "Fuel_Type"])

# Pivot table with specific subset of columns (Aggregation is Sum)
pd.pivot_table(df_pivot, index=["Location", "Year", "Fuel_Type"],
               values=[ "Kilometers_Driven"], aggfunc="sum")

# Pivot table with multiple Aggregations
pd.pivot_table(df_pivot, index=["Location", "Year", "Fuel_Type"], 
               values=["Kilometers_Driven", "Price", "Car_Age"], aggfunc=["sum", "count"], margins=True)


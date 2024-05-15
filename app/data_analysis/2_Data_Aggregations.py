import pandas as pd
from app.config.AppSettings import AppSettings

settings = AppSettings()

url_list = []
url_list.append(settings._common_account)
url_list.append(settings._repo_name)
url_list.append(settings._branch_name)
url_list.append(settings._app_root)
url_list.append(settings._data_analysis_folder)
url_list.append(settings._cleaned_files_path)
url_list.append(settings._cleaned_csv_path)

csv_url = settings._raw_data_url + "/".join(url_list)

#Reading Cleaned CSV
df = pd.read_csv(csv_url, sep=",", header=0, skipinitialspace=True)

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


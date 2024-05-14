import pandas as pd
import numpy as np
from app.config.AppSettings import AppSettings
from github import Github, Auth
from io import StringIO
from datetime import date

settings = AppSettings()

auth = Auth.Token(settings._token)
g = Github(auth=auth)

repo = g.get_repo(settings._common_url)
csv_url = settings._raw_files_path + settings._csv_path

contents = repo.get_contents(csv_url, ref="main")
decoded_csv_content = contents.decoded_content.decode()

csv_data = StringIO(decoded_csv_content)
df_cars = pd.read_csv(csv_data, sep=",", header=0, skipinitialspace=True)

#Describing the data
df_cars.head()

# Get the number of rows only
df_cars.shape[0]

# Get the number of columns only
df_cars.shape[1]

# Get the row at first position
df_cars[df_cars.index==0]

# Get the rows between 2 and 9
df_cars[df_cars.index.isin(range(2,10))]

# Get the row at mentioned positions (100, 200, 300)
df_cars.loc[[100, 200, 300]]

#Count Non Null values in each column
df_cars.count()

# Removing leading and trailing spaces from all string attributes
df_cars[["Name", "Location", "Fuel_Type", "Transmission", "Owner_Type", "Mileage", "Engine", 
         "Power", "New_Price"]].apply(lambda x: x.str.strip())
df_cars.head()

#Second transformation, Replacing all NaNs with 0 in only Numeric Columns
numeric_columns = df_cars.select_dtypes(include=["number"]).columns
df_cars[numeric_columns] = df_cars[numeric_columns].fillna(0)
df_cars[numeric_columns] = df_cars[numeric_columns].replace(np.nan, 0, regex=True)
df_cars.head()

#Splitting Engine column and converting to float for further analysis
details = df_cars["Engine"].str.split("\s").str
df_cars["Engine_New"] = details.get(0)
df_cars["Engine_New"] = df_cars["Engine_New"].fillna(0)
df_cars["Engine_New"] = df_cars["Engine_New"].replace("null", "0")
df_cars["Engine_New"] = df_cars["Engine_New"].astype(float)
df_cars["Engine"] = df_cars["Engine_New"]
df_cars.head()

#Splitting Power column and converting to float for further analysis
details_p = df_cars["Power"].str.split("\s").str
df_cars["Power_New"] = details_p.get(0)
df_cars["Power_New"] = df_cars["Power_New"].fillna(0)
df_cars["Power_New"] = df_cars["Power_New"].replace("null", "0")
df_cars["Power_New"] = df_cars["Power_New"].astype(float)
df_cars["Power"] = df_cars["Power_New"]
df_cars.head()

#Replace NA values with 0
df_cars["New_Price"] = df_cars["New_Price"].fillna(0)
df_cars.head()

# Remove unrequired columns from data
df_cars.drop(["S.No.", "Power_New", "Engine_New"], axis = 1, inplace = True)
df_cars.info()

#Add new calculated columns
df_cars["Car_Age"] = date.today().year - df_cars["Year"]
df_cars.head()

#Creating new features for further analysis
name_arr = df_cars["Name"].str.split().str
df_cars["Brand"] = name_arr.get(0)
df_cars["Model"] = name_arr.get(1)
df_cars.head()

#Writing cleaned CSV at designated path
df_cars.to_csv(settings._cleaned_files_path + settings._cleaned_csv_path, index = False)





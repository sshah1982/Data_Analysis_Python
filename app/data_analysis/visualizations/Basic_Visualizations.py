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

df.head()

#Histogram of Year column
km_column = df["Year"]
km_column.plot(kind="hist")

#Bar Chart of Fule Type Count by Location
df_grouped_location = df.groupby("Location")["Fuel_Type"].count()
df_grouped_location.plot(x="Location", y="Fuel_Type", kind="bar", rot=90, fontsize=10)

#Pie Chart of of Fule Type Count by Location
df_grouped_location.plot(x="Location", y="Fuel_Type", kind="pie", autopct="%.1f%%", 
                                      title="Fuel Type Count by Location", rot=90, fontsize=10)


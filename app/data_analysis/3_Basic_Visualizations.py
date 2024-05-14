import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
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

#Ordered Bar Chart
grouped_location_sorted = df_grouped_location.sort_values()
df_grouped_location_sorted = grouped_location_sorted.to_frame()
sb.barplot(x="Location", y="Fuel_Type", data=df_grouped_location_sorted)
plt.xticks(rotation=90)
plt.tight_layout()


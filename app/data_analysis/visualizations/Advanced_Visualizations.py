import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import squarify as sq
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

#Heatmap of Years and Kms driven
df_cols = df[["Year", "Kilometers_Driven"]]
plt.figure(figsize=(12,10), dpi= 80)
sb.heatmap(df_cols.corr(), xticklabels=df_cols.corr().columns, 
            yticklabels=df_cols.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.title('Heatmap', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

#Categorical plots by Location, Year and Fuel Type
grouped_data = df.groupby(["Location", "Year"])["Fuel_Type"].count()
grouped_data.head(500)
df_grouped = grouped_data.to_frame()
sb.catplot(
    data=df_grouped, x="Location", y="Fuel_Type", col="Year", col_wrap=2,
    kind="bar", height=4, aspect=.6
)
plt.show()

#Treemap of Years and Kilometers Driven
series = df.groupby(["Year"])["Kilometers_Driven"].sum()
series.head(100)
df_transformed = series.to_frame().reset_index()
df_transformed = df_transformed.rename(columns= {1: 'Total Kilometers'})
df_transformed.head(100)
sizes = df_transformed["Year"] # Proportions of the categories
label = df_transformed["Kilometers_Driven"]
sq.plot(sizes=sizes, label=label, alpha=0.6).set(title='Treemap of Years and Kilometers Driven')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import squarify as sq
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

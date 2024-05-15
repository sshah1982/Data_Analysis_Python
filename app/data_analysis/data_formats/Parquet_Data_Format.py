import pandas as pd
from app.config.AppSettings import AppSettings

settings = AppSettings()

url_list = []
url_list.append(settings._common_account)
url_list.append(settings._repo_name)
url_list.append(settings._branch_name)
url_list.append(settings._app_root)
url_list.append(settings._data_analysis_folder)
url_list.append(settings._raw_files_path)
url_list.append(settings._parquet_path)

parquet_url = settings._raw_data_url + "/".join(url_list)
df_parquet = pd.read_parquet(parquet_url)
print(df_parquet.head())
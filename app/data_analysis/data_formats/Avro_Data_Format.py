import pandas as pd
import pandavro as pdx
from app.config.AppSettings import AppSettings

'''def avro_df(filepath):
    # Open file stream
    with open(filepath) as fp:
        # Configure Avro reader
        reader = fastavro.reader(fp)
        # Load records in memory
        records = [r for r in reader]
        # Populate pandas.DataFrame with records
        df = pd.DataFrame.from_records(records)
        # Return created DataFrame
        return df
'''
settings = AppSettings()

url_list = []
url_list.append(settings._common_account)
url_list.append(settings._repo_name)
url_list.append(settings._branch_name)
url_list.append(settings._app_root)
url_list.append(settings._data_analysis_folder)
url_list.append(settings._raw_files_path)
url_list.append(settings._avro_path)

avro_url = settings._raw_data_url + "/".join(url_list)

df_avro = pdx.read_avro(avro_url)
print(df_avro.head())


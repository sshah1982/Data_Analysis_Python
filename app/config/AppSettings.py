import configparser
import os
from pathlib import Path

path = Path(__file__)
root_dir = path.parent.absolute()
config_path = os.path.join(root_dir, "config.properties")
config = configparser.ConfigParser()
config.read(config_path)

class AppSettings:
    _scheme= ""
    _raw_data_url = ""
    _branch_name = ""
    _common_account = ""
    _repo_name = ""
    _token = ""
    _app_root = ""
    _data_analysis_folder = ""
    _raw_files_path = ""
    _cleaned_files_path = ""
    _csv_path = ""
    _cleaned_csv_path = ""
    _json_path = ""
    _xml_path = ""
    _excel_path = ""
    _avro_path = ""
    _parquet_path = ""
    _html_path = ""


    def __init__(self):
        props = config["SCHEME"]
        self._scheme = "/".join(str(val) for key, val in props.items())
        
        props = config["RAW_DATA_URL"]
        self._raw_data_url = "/".join(str(val) for key, val in props.items())
        
        props = config["BRANCH_NAME"]
        self._branch_name = "/".join(str(val) for key, val in props.items())
        
        props = config["COMMON_ACCOUNT_NAME"]
        self._common_account = "/".join(str(val) for key, val in props.items())
        
        props = config["COMMON_REPO_NAME"]
        self._repo_name = "/".join(str(val) for key, val in props.items())
        
        props = config["TOKEN"]
        self._token = "/".join(str(val) for key, val in props.items())
        
        props = config["APP_ROOT"]
        self._app_root = "/".join(str(val) for key, val in props.items())
        
        props = config["DATA_ANALYSIS_FOLDER"]
        self._data_analysis_folder = "/".join(str(val) for key, val in props.items())
        
        props = config["RAW_FILES"]
        self._raw_files_path = "/".join(str(val) for key, val in props.items())
        
        props = config["CLEANED_FILES"]
        self._cleaned_files_path = "/".join(str(val) for key, val in props.items())
        
        props = config["CSV"]
        self._csv_path = "/".join(str(val) for key, val in props.items())
        
        props = config["CSV_CLEANED"]
        self._cleaned_csv_path = "/".join(str(val) for key, val in props.items())
        
        props = config["JSON"]
        self._json_path = "/".join(str(val) for key, val in props.items())
        
        props = config["XML"]
        self._xml_path = "/".join(str(val) for key, val in props.items())
        
        props = config["EXCEL"]
        self._excel_path = "/".join(str(val) for key, val in props.items())
        
        props = config["AVRO"]
        self._avro_path = "/".join(str(val) for key, val in props.items())
        
        props = config["PARQUET"]
        self._parquet_path = "/".join(str(val) for key, val in props.items())
        
        props = config["HTML"]
        self._html_path = "/".join(str(val) for key, val in props.items())
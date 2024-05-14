import configparser
import os
from pathlib import Path

path = Path(__file__)
root_dir = path.parent.absolute()
config_path = os.path.join(root_dir, "config.properties")
config = configparser.ConfigParser()
config.read(config_path)

class AppSettings:
    _common_url = ""
    _token = ""
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
        props = config["COMMON"]
        self._common_url = "/".join(str(val) for key, val in props.items())
        
        props = config["TOKEN"]
        self._token = "/".join(str(val) for key, val in props.items())
        
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
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

    def __init__(self):
        common_props = config["COMMON"]
        self._common_url = "/".join(str(val) for key, val in common_props.items())

    def get_common_url(self):
        return self._common_url
    
    
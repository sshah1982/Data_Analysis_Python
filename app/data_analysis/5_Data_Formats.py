import pandas as pd
import configparser
import xml.etree.ElementTree as ET
import httpx
#from fastavro import reader
from datetime import datetime
from app.config.AppSettings import AppSettings
from github import Github, Auth
from io import StringIO

settings = AppSettings()

auth = Auth.Token(settings._token)
g = Github(auth=auth)

repo = g.get_repo(settings._common_url)
json_url = settings._raw_files_path + settings._json_path

contents = repo.get_contents(json_url, ref="main")
decoded_json_content = contents.decoded_content.decode()

json_data = StringIO(decoded_json_content)

#Reading JSON
df = pd.read_json(json_data).convert_dtypes()
df.head()
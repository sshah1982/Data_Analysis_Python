import pandas as pd
import numpy as np

from app.config.AppSettings import AppSettings

settings = AppSettings()

print(settings.get_common_url())
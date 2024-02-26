from pathlib import Path
import datetime as dt

BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d'
now = dt.datetime.now()
FORMAT_TIME = now.strftime(DATETIME_FORMAT)
UTF = 'utf-8'
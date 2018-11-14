import pandas as pd 
from google.cloud import bigquery

projectid = "prefab-overview-218500"

data_frame = pd.read_gbq('SELECT * FROM test_dataset.test_table', projectid)


data_frame.to_gbq('test_dataset.test_table',projectid,if_exists='append')

data_frame = pd.read_gbq('SELECT * FROM test_dataset.test_table', projectid)

print(data_frame)
from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'test_dataset'  # replace with your dataset ID
table_id = 'test_table'  # replace with your table ID
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

rows_to_insert = [
    ('Phred Phlyntstone', 32),
    ('Wylma Phlyntstone', 29),
]

errors = client.insert_rows(table, rows_to_insert)  # API request

assert errors == []
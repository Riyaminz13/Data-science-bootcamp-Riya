from google.cloud import bigquery

# client a "client" object 
client = bigquery.Client()

#construct a reference to the "hacker_news" dataset 
dataset_ref = client.dataset("hacker_news",project = "bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# list all the tables in the hacker_news 
tables = list(client.list_table(dataset))

# print the name of tables in the dataset 
for table in tables:
    print(table.table_id)

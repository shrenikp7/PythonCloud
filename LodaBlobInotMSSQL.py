

#### Folllowing code demonstrate to load data from Zure blob storage to SQL database 
#### Code components - create_engine for mssql+pyodbc driver and connection credential
#### Using engine.connect() method, blob storage account name, blob storage account key
#### blob storage access key, container name, and blob name, target table
#### It is using BULK insert command to insert data from CSV file to MS SQL server
#### Using connection.execute to execute bulk insert into the MS SQL server. 

from sqlalchemy import create_engine

# Create an Azure SQL Database engine
engine = create_engine('mssql+pyodbc://username:password@server_name/database_name?driver=ODBC+Driver+17+for+SQL+Server')

# Establish a connection
connection = engine.connect()

# Specify the Azure Blob Storage details
blob_storage_account_name = 'storage_account_name'
blob_storage_account_key = 'storage_account_key'
container_name = 'container_name'
blob_name = 'blob_name'

# Specify the target table in Azure SQL Database
table_name = 'target_table'

# Generate the BULK INSERT command
bulk_insert_command = f"BULK INSERT {table_name} FROM 'https://{blob_storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}' " \
                      f"WITH (FORMAT = 'CSV', FIRSTROW = 2);"

# Execute the BULK INSERT command
connection.execute(bulk_insert_command)

# Close the connection
connection.close()


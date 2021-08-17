import boto3
import pandas as pd
s3_client = boto3.client('s3')

s3_client.download_file("datalake-sw-igti-edc",
                       "data/users_ago19.csv",
                       "data/teste.csv")
df = pd.read_csv("data/teste.csv",encoding = "ISO-8859-1", engine='python')
print(df)

s3_client.upload_file("data/MICRODADOS_ENEM_2019.csv",
                       "datalake-sw-igti-edc",     
                       "raw-data/MICRODADOS_ENEM_2019.csv") 


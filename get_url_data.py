import pandas as pd
from pymongo import MongoClient
import random

def read_from_url(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        print(f"Error reading CSV data from URL: {e}")
        return None

url = "https://india-crop.s3.us-east-2.amazonaws.com/crop_production.csv"
client = MongoClient("mongodb+srv://amitmalikca:kurar@datapro.fm6bnoz.mongodb.net/?retryWrites=true&w=majority")

num = random.randrange(10,50)

data = read_from_url(url)
if data is not None:
    # process the data
    print(data.head(num))
else:
    # handle the error
    print("Failed to read CSV data from URL")

db = client["cropdatabase"]
collection = db["cropindia"]


documents = data.to_dict(orient="records")

collection.insert_many(documents)



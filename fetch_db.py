import pymongo
import pandas as pd
from bson import json_util
import json
from bson.json_util import dumps
from flask import jsonify


# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://amitmalikca:kurar@datapro.fm6bnoz.mongodb.net/?retryWrites=true&w=majority")

# Access the database and collection
db = client["cropdatabase"]
collection = db["cropindia"]

def full_db():
    return collection.find()
    # for document in cursor:
    #     return document

def conditional_db():
    return

def get_dataframe():
    # Retrieve data from MongoDB
    cursor = collection.find({})
    df = pd.DataFrame(list(cursor))

    # Drop the _id column if it exists
    if "_id" in df.columns:
        df.drop("_id", axis=1, inplace=True)
    return df


def get_all_items():
    data = collection.find({}, {"_id": 0})
    # Convert the retrieved data to a list of dictionaries
    list_data = list(data)
    # Convert the list of dictionaries to a JSON array
    json_data = json.loads(json_util.dumps(list_data))
    # Return the JSON data
    return json_data


def get_item_by_id(item_id: str):
    # Get an item by its ID from the database
    item = collection.find_one({"Crop": item_id})
    if item is not None:
        item["_id"] = str(item["_id"])  # convert ObjectId to string
        return {"item": item}
    else:
        return {"error": "Item not found"}
    

print(get_all_items)

def get_json_data():
    data = list(collection.find({}, {'_id': 0}))
    
    # Convert the data to JSON format and return it
    return jsonify(data)

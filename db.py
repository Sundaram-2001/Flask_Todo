from dotenv import load_dotenv
from pymongo import MongoClient,ASCENDING
load_dotenv()
import os
db_url = os.getenv("mongodb_url")
client = MongoClient(db_url)
try:
    client.admin.command('ping')
    print("successfully connected :)")
except Exception as e:
    print("Connection Failed!")
try:
    db = client.crud        #this line is creating the DB , crud is th eDB and db here is the instance
    print("DB Created successfully!!")
except Exception as e:
    print("unexpected error!")
try:
    task_collection=db.tasks        #creating the collection , tasks is the collection and task_collection here is the instance
    print("Collection Created successfully!")
    
    
    task_collection.drop_indexes()
    print("Existing indexes dropped")
    
    
    task_collection.create_index(
        [("task", ASCENDING)],  
        unique=True
    )
    print("New unique index created on 'task' field")
except Exception as e:
    print("unexpected error occured while creating the collection!")
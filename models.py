from db import task_collection
from bson import json_util, ObjectId 
from flask import jsonify
class TaskModel:
    @staticmethod
    def add_task(task_data):
        try:
            result=task_collection.insert_one(task_data)
            return result
        except Exception as e:
            print(e)
            return None
    @staticmethod
    def getAllTasks():
        try:
            tasks=list(task_collection.find({}))
            for task in tasks:
                task['_id']=str(task['_id'])
            return {
                "tasks":tasks
            },200
        except Exception as e:
            print(e)
            return {
                "message":"error fetching tasks!"
            },500
    @staticmethod
    def get_task_by_id(task_id):
        try:
            object_id=ObjectId(task_id)
            result=task_collection.find_one({"_id":object_id})
            return result
        except Exception as e:
            print(e)
            return None
    @staticmethod 
    def update_task(task_id,update_data):
        try:
            object_id=ObjectId(task_id)
            result=task_collection.update_one(
                {"_id":object_id},
                {"$set":update_data}
            )
            if result.matched_count==0:
                response=jsonify({"message":"unexpected error!"})
                response.status_code=500
                return response
        except Exception as e:
            print(e)
            response = jsonify({"message": "Internal server error!"})
            response.status_code = 500
            return response
    def delete_task(task_id):
        try:
            object_id=ObjectId(task_id)
            result=task_collection.delete_one({"_id":object_id})
            return result
        except Exception as e:
            print(e)
            return None
from flask import Blueprint, request, jsonify
from models import TaskModel
from typing import Dict , Any,Tuple ,   Union , TypedDict
routes_blueprint=Blueprint("routes",__name__)
class TaskPayLoad(TypedDict):
    task:str
class TaskIDPayload(TypedDict):
    task_id:str
@routes_blueprint.route("/",methods={'GET'})
def home():
    return jsonify({"message":"Hello World!"})
@routes_blueprint.route("/addTask", methods=["POST"])
def add_task() -> Union[Dict[str, Any], Tuple[Dict[str, Any], int]]:
    data = Union[TaskPayLoad,None]=request.get_json()
    if data is None:
        return {"message": "Bad request"}, 400
    if "task" not in data:
        return jsonify({
            "message":"bad request!"
        }),400
    result=TaskModel.add_task(data)
    if result.acknowledged:
        return jsonify({
            "Message":"Task Inserted Successfully",
            "ID":str(result.inserted_id),
            "task":data
        })
    elif result is None:
        return  jsonify ({"message":"unexpected error!"}),500
    else:
        return jsonify ({"message":"Internal Server Error!"}),500

@routes_blueprint.route("/allTasks", methods=["GET"])  
def get_tasks():
    try:
        result=TaskModel.getAllTasks()
        return result 
    except Exception as e:
        print(e)
        return jsonify({"message":"internal server error"}),500
@routes_blueprint.route("/task/<task_id>",methods=["GET"])
def get_task(task_id) -> Union[Dict[str, Any], Tuple[Dict[str, Any], int]]:
    if not task_id:
        return jsonify({
            "message": "Task ID cannot be empty!"
        }), 400
    result=TaskModel.get_task_by_id(task_id)
    return jsonify(result)
@routes_blueprint.route("/task/<task_id>", methods=["PUT"])
def update_task(task_id: str) -> Union[Dict[str, Any], Any]:
    if not task_id:
        response=jsonify({"message":"id is required!"})
        response.status_code=400
        return response
    data=request.get_json()
    if not data:
        response=jsonify({"message":"data is required!!"})
        response.status_code=400
        return response
    try:
        result=TaskModel.update_task(task_id,data)
        print("operation performed ",result)
        if result is None:
            response=jsonify({"message":"operation performed but no response received!"})
            response.status_code=200
            return response
        return result
    except Exception as e:
        print("some exception occured!!!",e)
        response=jsonify({"something unexpected happened!"})
        response.status_code=500
        return response
@routes_blueprint.route("/deleteTask/<task_id>",methods=["DELETE"])
def delete_tasks(task_id: str) -> Union[Dict[str, Any], Tuple[Dict[str, Any], int]]:
    if task_id is None:
        return jsonify({"messsage":"task id is required !!"}),400
    result=TaskModel.delete_task(task_id)
    if result.deleted_count>0:
        return jsonify({"message":"Operation completed successfully!!"})
    elif result is None:
        return jsonify({"message":"Unexpected Error occured!!"}),500
    else:
        return jsonify({"messgae":"task not found!1"}),404
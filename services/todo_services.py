from typing import List
from exceptions.custom_exceptions import TodoNotFound
from db import fake_db as db


def get_todo():
    response = [{"id": x, "task": y} for x, y in db.todo.items()]
    return response

def add_todo(todo_task: str):
    db.todo[db.counter] = todo_task
    db.counter+=1
    return {"message": "Added successfully"}

def del_task(taskid: int):
    if taskid in db.todo:
        db.todo.pop(taskid)
        return {"message": f"Deleted todo with id :: {taskid}"}
    raise TodoNotFound("Todo not found")

def update_task(taskid: int, temp_task: str):
    if taskid in db.todo:
        db.todo[taskid] =  temp_task
        return {"message": f"Updated the task with taskid : {taskid}"}
    raise TodoNotFound("Todo not found")

def bulk_add(multiple_input: List[str]):
    for temp_task in multiple_input:
        db.todo[db.counter] = temp_task
        db.counter += 1
    return {"message": "Added successfully"}
import time
import asyncio
import datetime
from typing import List
from services import todo_services as service
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, UploadFile, File
from schemas import todo_schemas as schemas
router = APIRouter()

def timer_inject():
    start_time = time.time()
    print("Request Started..." + str(datetime.datetime.now()))
    yield "Atlab"
    end_time = time.time()
    print("Request processed successfully..."+str(datetime.datetime.now()))
    print(f"Time taken -> {end_time - start_time:.3f} seconds")

def bgTask(message : str):
    with open("log.txt" , "a") as file:
        file.write(message + "\n")

@router.post("/todos/bulk" , status_code=201)
def bulk_add(todos: List[schemas.Todolist]):
    new_list = [x.task for x in todos]
    return service.bulk_add(new_list)

@router.put("/todos/{taskid}", status_code=200)
def update_task(taskid: int, raw_task : schemas.Todolist):
    result = service.update_task(taskid, raw_task.task)

    return result

@router.delete("/todos/{taskid}", status_code=200)
def del_task(taskid: int):
    result = service.del_task(taskid)

    return result

@router.post("/todos", status_code=201)
def add_todo(raw_task: schemas.Todolist):
    return service.add_todo(raw_task.task)

counter = 1
@router.get("/todos" ,response_model = List[schemas.response], status_code=200)
async def get_todo(background_task : BackgroundTasks, result = Depends(timer_inject)):
    print(result)
    background_task.add_task(bgTask, "Response Sent Successfully")
    return service.get_todo()


@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    name , extn = file.filename.rsplit(".",1)
    filename = name+ str(time.time_ns())+"."+extn
    file_path = f"uploads/{filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return {"filename": filename}
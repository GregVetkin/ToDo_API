from fastapi import FastAPI
from datetime import datetime
from typing import Optional

from fastapi.encoders import jsonable_encoder
from model.model import Task, TaskList
#import model.taskman_json as taskman
import model.taskman_pgsql as taskman

app = FastAPI()


@app.get("/api/tasks", tags=["Tasks"])
async def get_tasks():
    """
    TODO
    Fetch the list of all tasks
    """
    return await taskman.get_tasks()


@app.get("/api/tasks/{id}", tags=["Tasks"])
async def get_task(id: int):
    """
    TODO
    Fetch the task by id
    """
    return await taskman.get_tasks(id)


@app.post("/api/tasks/create", tags=["Tasks"])
async def create_task(task: Task):
    """
    TODO
    1. Create a new task
    2. Return the details of task
    """
    id = await taskman.create_task(task)
    return await taskman.get_tasks(id)


@app.put("/api/tasks/{id}/update", tags=["Tasks"])
async def update_task(id: int, task: Task):
    """
    TODO
    1. Update the task by id
    2. Return the updated task
    """
    await taskman.update_task(id, task)
    return await taskman.get_tasks(id)


@app.delete("/api/tasks/{id}/delete", tags=["Tasks"])
async def delete_task(id: int):
    """
    TODO
    1. Delete the task by id
    2. Return a confirmation of deletion
    """
    id = await taskman.delete_task(id)
    response = {id: "Task successfully deleted"}
    return jsonable_encoder(response)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
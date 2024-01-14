from model.model_pgsql import Task
from pydantic import TypeAdapter
from typing import List, Optional


async def get_tasks(id: Optional[int] = 0):
    """
    TODO
    1. Fetch all tasks if no argument (id) provided
    2. Else fetch the task by id provided
    """
    if id == 0:
        response = {}
        tasks = Task.select().execute()
        for task in tasks:
            response[task.task_id] = {"id": task.task_id,
                                      "task": {"summary": task.summary,
                                               "priority": task.priority}
                                      }
    else:
        task = Task.get(Task.task_id == id)
        response = {"id": task.task_id,
                    "task": {"summary": task.summary,
                             "priority": task.priority}
                    }
    return response


async def create_task(new_task: Task):
    """
    TODO
    1. Create a new task and add it to the list of tasks
    2. Write the updated tasklist to file
    """
    task = Task.create(summary=new_task.summary, priority=new_task.priority)
    return task


async def delete_task(id):
    """
    TODO
    1. Delete task by id provided
    """
    Task.delete_by_id(id)
    return id


async def update_task(id: int, new_task: Task):
    """
    TODO
    1. Update the task by id based on new task details
    2. Write the updated tasklist to file
    """

    task = Task.get_by_id(id)
    task.summary = new_task.summary
    task.priority = new_task.priority if new_task.priority > 0 and new_task.task_id < 5 else 4
    task.save()
    return id


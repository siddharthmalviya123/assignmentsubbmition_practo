from .repository import save_task, get_task, delete_task
from .models import Task

def create_task(title, description=None):
    return save_task(title, description)

def retrieve_task(task_id):
    return get_task(task_id)

def remove_task(task_id):
    return delete_task(task_id)


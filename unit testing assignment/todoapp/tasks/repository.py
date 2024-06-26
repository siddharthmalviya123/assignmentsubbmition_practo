from .models import Task

def save_task(title, description=None):
    task = Task(title=title, description=description)
    task.save()
    return task

def get_task(task_id):
    return Task.objects.get(id=task_id)

def delete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()


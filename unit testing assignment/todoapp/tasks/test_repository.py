from django.test import TestCase
from tasks.models import Task
from tasks.repository import save_task, get_task, delete_task

class TaskRepositoryTests(TestCase):

    def test_save_task(self):
        task = save_task("Test Task")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, "Test Task")

    def test_get_task(self):
        task = save_task("Test Task")
        retrieved_task = get_task(task.id)
        self.assertEqual(task, retrieved_task)

    def test_delete_task(self):
        task = save_task("Test Task")
        delete_task(task.id)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task.id)


from django.test import TestCase
from tasks.service import create_task, retrieve_task, remove_task
from tasks.models import Task

class TaskServiceTests(TestCase):

    def test_create_task(self):
        task = create_task("Test Task")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, "Test Task")

    def test_retrieve_task(self):
        task = create_task("Test Task")
        retrieved_task = retrieve_task(task.id)
        self.assertEqual(task, retrieved_task)

    def test_remove_task(self):
        task = create_task("Test Task")
        remove_task(task.id)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task.id)


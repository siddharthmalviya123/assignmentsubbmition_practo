from django.test import TestCase, Client
from tasks.models import Task

class TaskControllerTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_task_view(self):
        response = self.client.post('/tasks/create/', {'title': 'Test Task'})
        self.assertEqual(response.status_code, 200)
        # Optionally, check the response content or redirect

    def test_delete_task_view(self):
        task = Task.objects.create(title='Test Task')
        response = self.client.post(f'/tasks/{task.id}/delete/')
        self.assertEqual(response.status_code, 302)
        # Ensure task is deleted or check redirection


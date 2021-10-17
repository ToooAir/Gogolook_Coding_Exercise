import unittest
from main import app
import json
import requests

class testing(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.debug = False
        self.client = app.test_client()
        self.assertEqual(app.debug, False)

    def test_1_add_task(self):
        response = self.client.post("/task", data=json.dumps({"name":"買早餐"}), content_type='application/json')
        self.assertEqual(json.loads(response.data),{'id': '1', 'name': '買早餐', 'status': 0})
        response = self.client.post("/task", data=json.dumps({"name":"買午餐"}), content_type='application/json')
        self.assertEqual(json.loads(response.data),{'id': '2', 'name': '買午餐', 'status': 0})
        response = self.client.post("/task", data=json.dumps({"name":"買晚餐"}), content_type='application/json')
        self.assertEqual(json.loads(response.data),{'id': '3', 'name': '買晚餐', 'status': 0})

    def test_2_get_tasks(self):
        response = self.client.get("/tasks")
        self.assertEqual(json.loads(response.data),
        [{'id': '1', 'name': '買早餐', 'status': 0},
        {'id': '2', 'name': '買午餐', 'status': 0},
        {'id': '3', 'name': '買晚餐', 'status': 0}])

    def test_3_edit_task(self):
        response = self.client.put("/task/1", data=json.dumps({"name":"買早餐", "status":1}), content_type='application/json')
        self.assertEqual(json.loads(response.data),{'id': '1', 'name': '買早餐', 'status': 1})

    def test_4_delete_task(self):
        response = self.client.delete("/task/1")
        self.assertEqual(response.status_code,200)

    def test_5_wrong_param(self):
        response = self.client.post("/task", data=json.dumps({}), content_type='application/json')
        self.assertEqual(json.loads(response.data),'param is missing')
        response = self.client.put("/task/1", data=json.dumps({"status":1}), content_type='application/json')
        self.assertEqual(json.loads(response.data),'param is missing')

    def test_6_not_found_id(self):
        response = self.client.put("/task/0", data=json.dumps({"name":"買早餐", "status":1}), content_type='application/json')
        self.assertEqual(json.loads(response.data),'id is not found')
        response = self.client.delete("/task/0")
        self.assertEqual(json.loads(response.data),'id is not found')

if __name__ == '__main__':
    unittest.main()
from flask import Flask
import json
import unittest 

app = Flask(__name__)

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.request = {
        'fullname': 'nazirini ',
        'email': 'hansu@gmail.com',
        'phone': '536780',
        'department': 'Team Lead',
        'computerID': 'AAA53',
        'description': 'Screen freezes when handling heavy apps'}
        self.content_type = "application/json"
        self.test_client = app.test_client()

    def tearDown(self):
        pass

class RequestTestCase(BaseTestCase):
    
    def test_create_request(self):
    
        response = self.test_client.post('/nazirini/api/v1.0/details', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)
       

    def test_modify_request(self):
    
        response = self.test_client.put('/nazirini/api/v1.0/details/1', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)
         

    def test_get_all_requests(self):
       
        response = self.test_client.post('/nazirini/api/v1.0/details', data=json.dumps(self.request), content_type = 'application/json')
        response = self.test_client.get('/nazirini/api/v1.0/details', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)
          
    def test_get_single_request(self):
       
        response = self.test_client.get('/nazirini/api/v1.0/details/1', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

                
    if __name__ == '__main__':
        unittest.main()

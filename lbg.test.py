"""
Sample unit test "testcase" for LBG API functionality
Tests key functions and API routes in isolation from client-side user interface

For full list of assertions available: https://docs.python.org/3.8/library/unittest.html
"""

import unittest
from lbg import item_builder
from flask_api import status
import requests

PORT = 8080
BASE_URL = f"http://localhost:{PORT}"

class MyLbgApiTestCase(unittest.TestCase):

    def test_item_builder_data(self):
        """
        Test to see if item_builder returns the correctly keyed dictionary object
        based on raw data passed to it
        """
        expected = {'name': 'Tool', 'description': 'Hammer', 'price': 10.5, '_id': 99}
        self.assertEqual(item_builder("Tool", "Hammer", 10.50, 99), expected)

    def test_item_builder_type(self):
        """
        Test to see if item_builder returns a dictionary object
        """
        self.assertIsInstance(item_builder("Tool", "Hammer", 10.50, 99), dict)

    def test_create_post_request_status(self):
        """
        Test to see if RESTful API returns a 201 (CREATED) status ok for a
        Create (Post) request.  Note.  API will need to be running(!)
        """
        response = requests.post(BASE_URL + '/create', json = {'name': 'Tool', 'description': 'Hammer', 'price': 10.5})

    @unittest.skip("Skip this test for now using this decorator...")
    def test_create_post_request_type(self):
        """
        Test to see if RESTful API returns an objectfor a simple
        Create (Post) request.  Note.  API will need to be running(!)
        """
        response = requests.post(BASE_URL + '/create', json = {'name': 'Vegetable', 'description': 'Leek', 'price': .7})
        self.assertIsInstance(response, object)
    
    @classmethod
    def tearDownClass(cls):
        requests.delete(BASE_URL + '/delete/1')

# module import protection
if __name__ == '__main__':
    unittest.main(verbosity=2)

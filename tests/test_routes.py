import unittest
from app import app

""" Testing / route for get and post request. If get request it done, it should return
success status code of 200. Our app does not have /post method so it should send 405 status code
for that."""

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # setting up the instance of app for testing
        self.app = app.test_client()
        self.app.testing = True
    # testing / route for get request
    def test_get_home_status_code(self):
        # send request to the / route
        response = self.app.get('/')

        # check for status code, passes the test if status_code is 200
        self.assertEqual(200, response.status_code)

    # testing / for post request, which must send status code 405
    def test_post_home_status_code(self):
        # send request to the / route
        response = self.app.post('/')

        # check for status code
        self.assertEqual(405, response.status_code)

    # testing /chat route
    def test_post_chat_status_code(self):
        # posting to the /chat should return status code of 200
        response = self.app.post('/chat', json={"prompt": "Give me info on Einstein"})

        # check for status code
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
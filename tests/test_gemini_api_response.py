import unittest

from dotenv import load_dotenv
from gemniconfig import gemini_model

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # setting up the instance of app for testing
        load_dotenv()

    # testing the model with valid prompt
    def test_valid_prompt1(self):
        prompt = "How can I setup S3 bucket?"
        response = gemini_model({prompt})

        # check for the response, the response should have s3, aws included
        self.assertIn("S3", response)
        self.assertIn("aws", response)

    # testing the model with invalid request
    def test_invalid_prompt(self):
        prompt = "Who is GOAT Messi or Ronaldo?"
        response = gemini_model({prompt})

        # check for the response, it should return "Sorry, I can only answer about AWS."
        self.assertIn("Sorry, I can only answer about AWS.", response)

if __name__ == "__main__":
    unittest.main()
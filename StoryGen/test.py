import unittest
from unittest.mock import patch
import tkinter as tk
from home_frame import HomeFrame
import openai
import openai_api


class Test(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.home_frame = HomeFrame(self.root)

    def test_new_idea(self):
        self.home_frame.no_api_key_count = 1
        self.home_frame.new_idea()
        self.assertIsNotNone(self.home_frame.no_api_key_found)
        self.assertEqual(self.home_frame.no_api_key_count, 2)

    def test_authentication_error(self):
        openai.api_key = "INVALID_API_KEY"

        try:
            response = openai.Completion.create(
                engine="text-davinci-002", prompt="Test prompt", max_tokens=5
            )
        except openai.error.AuthenticationError:
            self.assertTrue(True)
        else:
            self.fail("Expected AuthenticationError, but no exception was raised.")

    def test_check_api_key(self):
        with patch("openai_api.requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            api_key = "dummy_api_key"
            self.assertTrue(openai_api.check_api_key(api_key))
            mock_post.return_value.status_code = 401
            self.assertFalse(openai_api.check_api_key(api_key))

    def test_get_response(self):
        with patch("openai_api.openai.ChatCompletion.create") as mock_create:
            prompt = "Hello"
            response = "Hi there!"
            mock_create.return_value = {"choices": [{"message": {"content": response}}]}
            self.assertEqual(openai_api.get_response(prompt), response)

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()

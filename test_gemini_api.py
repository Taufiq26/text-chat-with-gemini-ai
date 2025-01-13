from dotenv import load_dotenv
import requests
import unittest
import os
import json

# Load environment variables at the start
load_dotenv()

class TestGeminiAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        
    def test_gemini_generate_content(self):
        headers = {
            'Content-Type': 'application/json'
        }
        
        payload = {
            "contents": [{
                "parts": [{"text": "Explain how AI works"}]
            }]
        }
        
        url = f"{self.base_url}?key={self.api_key}"
        response = requests.post(url, headers=headers, json=payload)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('candidates', response.json())

if __name__ == '__main__':
    unittest.main()

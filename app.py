import pathlib
import textwrap
import os
import logging

import google.generativeai as genai

from IPython.display import Markdown
from dotenv import load_dotenv
from absl import logging as absl_logging 

# Disable warning messages
absl_logging.set_verbosity(absl_logging.ERROR)
logging.getLogger().setLevel(logging.ERROR)

# Load environment variables at the start
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def list_models():
  for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
      print(m.name)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Define the model
model = genai.GenerativeModel('gemini-1.5-flash')
try:
  exit_program = False
  while not exit_program:
    user_input = input("Enter your question: ")
    if user_input.lower() == 'exit':
      exit_program = True
      break

    response = model.generate_content(user_input)
    print(response.text)

except Exception as e:
  print(f"Generation failed: {str(e)}")
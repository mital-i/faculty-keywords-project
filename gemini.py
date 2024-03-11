import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

from google.colab import userdata
GOOGLE_API_KEY=userdata.get('AIzaSyBwdA7n_DCssoBrlbytLK6R4SDeoeJcxQY')

genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
# the API build in two phases
# open_ai_conn.py
from openai import OpenAI

class Open_AI:
  def __init__(self, API_KEY):
    self._prompt = '''This GPT specializes in translating Arabic algorithmic instructions into Python code. It accurately replaces Arabic keywords with their Python equivalents,
    ensures variables are named in English for runnable code, and checks for syntax correctness. If a syntax error is detected,
    it provides a specific error message to help users correct the issue. The output code is provided as plain text, not in Python markdown,
    to ensure compatibility with various text editors and environments. make sure that the arabic text are still in the strings'''
    self._client = OpenAI(api_key=API_KEY)
  # make the send request
  # complete the request body (sys, role ...)

  def get_response(self, apl_code):
    self.requester = self._client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "system",
               "content": f"{self._prompt}"},
              {"role": "user", "content": f"{apl_code}"}],
    stream=False,
)
    # stream.choices[0].message.content
    return self.requester.choices[0].message.content #get the code only

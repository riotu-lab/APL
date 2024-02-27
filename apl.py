# APL.py
# 1. getting the prompt of the programming language (asa)
from open_ai_conn import Open_AI
from python_runner import PythonRunner


class APL:
  def __init__(self, API):
    ''' this object is used to to get the API object that could get the code from the user according to the APL specification
    then he can run the code '''
    self._open_ai = Open_AI(API)
    self._pyRunner = PythonRunner()


# 2. response with the python code
  def get_code(self, asa_code:str):
    ''' asa_code is a string that represents the code written in Arabic according to the APL specification (in the paper)'''
    response =  self._open_ai.get_response(asa_code)

    if "error" in response:
      raise Exception(f"check the format of the code {response}")

    return response
  def run_code(self, py_code:str):
    ''' the returned code from the `get_code` function could be run by this function
    py_code:is a python code that was returned from the `get_code`'''
    # craete a temp file

    # run the code and get output
    output = self._pyRunner.run_code(py_code)
    # return the response
    return output

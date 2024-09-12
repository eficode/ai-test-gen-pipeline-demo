from functions import *

# First initial promt to ask ChatGPT for tests
def get_tests(given_file, key):
  # Setup variables to be used
  test_file = "unit_tests.py"
  promt = '''Please provide unittests for the following python code.
If you notice that there are already provided unit tests, just make sure you don't accidentaly give same unit tests and that you don't redo what they test in your own generated tests.
However if you notice some errors in the provided unit tests, please fix them is possible. Comment the code to emphasize that the unit test is fixed.
In your awnser, please just give the code for unit tests and required comments, nothing more.

'''
  promt += "\n"+"\n".join(fail_str(file_read(given_file)))
  setup = "You are a skilled engineer assistant"

  print("Used promt:\n",promt)

  # Get code from ChatGPT and write the output to a file
  file_write(test_file, get_chatgpt(key,setup,promt).content)
  # Clean the given code, ie remove the "```python" etc from it
  file_write(test_file, clean_code(test_file,given_file))

get_tests(sys.argv[1], sys.argv[2])
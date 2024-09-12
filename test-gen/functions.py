import sys, os, unittest
from code_to_be_tested import *
from openai import OpenAI

# Exception for an error
class CorruptedFileError(Exception):
    def __init__(self, message):
        super(CorruptedFileError, self).__init__(message)

# Seperate line data and returns the line data as a list
def stripper(line, char_):
  line = line.rstrip()
  parts = line.split(char_)
  return parts

# Reads the data from given file and returns the data as a big list, where each spot is one line data in file
def file_read(filename):
    try:
        file = open(filename, "r")
        data = []
        for line in file:
            data.append(stripper(line,"\n"))
        file.close()
        return data
    except OSError:
        raise CorruptedFileError("Error while trying to read data from file")

# Write data to given file
def file_write(filename, data):
    try:
        file = open(filename, "w")
        for i in data:
          if isinstance(i,str):
            file.write(i)
          else:
            file.write(i[0])
        file.close()
    except OSError:
        raise CorruptedFileError("Error while trying to write data to file")

# Clean the file to only include the code
# Also add a line that the test file imports the original code
def clean_code(filename, tested_file):
  data = file_read(filename)
  new_data = []
  import_ = "from "+stripper(tested_file,".py")[0]+" import *"
  new_data.append(import_)
  new_data.append("\n")
  for i in data:
    if "```" not in i[0]:
      new_data.append(i)
      new_data.append("\n")
  
  return new_data

# Create a list of strings, with each string being entierly an error message
def fail_str(list_):
  out = []
  for i in list_:
    out.append("\n".join(map(str,i)))
  return out
  
# Run the tests on the given test file
# Returns a list of all the possible errors that have occured
def run_tests(test_file):
  loader = unittest.TestLoader()
  suite = loader.discover('.', pattern=test_file)
  runner = unittest.TextTestRunner()

  failures = []
  try:
    result = runner.run(suite)
    if result.failures or result.errors:
      for i in result.failures:
        failures.append(i)
      for i in result.errors:
        failures.append(i)

  except Exception as ex:
    failures.append(ex)
  
  if not result.wasSuccessful():
    failures = fail_str(failures)

  return failures

# Usage example:
# return get_chatgpt(api_key, organization, "You are a helpful assistant.", "Hello, how are you?")
def get_chatgpt(key, setup, promt):
  client = OpenAI(
      api_key=key,
  )

  response = ""
  try:
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": setup},
        {"role": "user", "content": promt}
      ]
    )
    response = completion.choices[0].message
    
  except Exception as e:
    response = e

  return response
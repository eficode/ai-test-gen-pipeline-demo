from functions import *

# Function to get new tests if previous tests have failed for whatever reason
# Repeat asking for new tests if failures are expected
# After 10 times give up, because from experience after that we won't get different awnsers from ChatGPT
def new_tests(given_file, key, error_file):
    # If there are errors in unittests, request the unittests again and tell what the given error code is
    # If this happens too many times, just give up and raise an error
    test_file = "unit_tests.py"
    #print("\n".join(fail_str(file_read(test_file))))
    #sys.exit(0)
    test_results = fail_str(file_read(error_file))
    for i in range(0,10):
        # Setup variables to be used
        setup = "You are a skilled engineer assistant"
        
        promt = "I gave you the following code and asked you to provide unittests for it:\n\n"
        promt += "\n".join(fail_str(file_read(given_file)))
        promt += "Your given unittests gave me the following errors\n\n"
        promt += "\n".join(test_results)
        promt += '''
        
Plese modify your unittests that I won't get the errors again
If you notice that there are already provided unit tests, just make sure you don't accidentaly give same unit tests and that you don't redo what they test in your own generated tests.
However if you notice some errors in the provided unit tests, please fix them is possible. Comment the code to emphasize that the unit test is fixed.
In your awnser, please just give the code for unit tests and required comments, nothing more.
As a reminder, here is the invalid code you gave:

'''       
        promt += "\n"+"\n".join(fail_str(file_read(test_file)))

        print("Used promt:\n",promt)

        # Get new unittests from chatgpt and write them to file
        file_write(test_file, get_chatgpt(key,setup,promt).content)
        # Clean the given code, ie remove the "```python" etc from it
        file_write(test_file, clean_code(test_file,given_file))

        # Run tests, and get possible errors in a list
        test_results = run_tests(test_file)
        # If no errors in list, exit
        if len(test_results) == 0:
            sys.exit(0)

    # Write possible errors in a file if tests aren't passed
    file_write(test_file, test_results)
    print("Errors can be found at:",test_file)
    sys.exit(1)

new_tests(sys.argv[1], sys.argv[2], sys.argv[3])

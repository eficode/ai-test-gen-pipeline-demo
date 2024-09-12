from functions import *

# Checks if given unittests pass, and write possible errors in another file that's given
def test_tests(test_file, error_file):
    # Run tests, and get possible errors in a list
    test_results = run_tests(test_file)
    # If no errors in list, exit
    if len(test_results) == 0:
        sys.exit(0)
    # Write possible errors in another file
    file_write(error_file, test_results)
    sys.exit(1)

test_tests(sys.argv[1], sys.argv[2])

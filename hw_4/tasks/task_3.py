"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
# stderr
'error: file not found'
# stdout
'OK'
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
import sys


def my_precious_logger(text: str):
    std_out = sys.stdout
    std_err = sys.stderr
    if text.startswith("error"):
        std_err.write(text)
    else:
        std_out.write(text)


my_precious_logger("OK")
my_precious_logger("error: file not found")

import os
import string


def def_clean_line():
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")
    with open(file_path, encoding="unicode-escape") as text:
        for line in text:
            clean_line = line.translate(str.maketrans("", "", string.punctuation)).split()
            yield clean_line

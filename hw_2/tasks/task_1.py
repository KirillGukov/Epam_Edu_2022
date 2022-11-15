"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
from typing import Dict
from hw_2.tasks.my_def import def_clean_line
import string
import os


def get_longest_diverse_words() -> List[str]:
    dict_words = {}
    for i in def_clean_line():
        for word in i:
            unique = []
            for j in word:
                if j not in unique:
                    unique.append(j)
                    dict_words[word] = len(unique)
    maximum_words = [max_word[0]for max_word in sorted(dict_words.items(), reverse=True, key=lambda a: a[1])[:10]]
    return maximum_words


def get_rarest_char() -> str:
    count_words: Dict[str, int] = {}
    for lines in def_clean_line():
        for word in lines:
            for letter in word:
                if letter in count_words:
                    count_words[letter] += 1
                else:
                    count_words[letter] = 1
    list_sorted_words = sorted(count_words.items(), key=lambda item: item[1])
    task_result = list_sorted_words[0][0]
    return task_result


def count_punctuation_chars(file_path: str) -> int:
    result = 0
    with open(file_path, encoding="unicode-escape") as text:
        for line in text:
            for symbol in line:
                if symbol in string.punctuation:
                    result += 1
        return result


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as text:
        result = 0
        for line in text:
            for word in line:
                if word not in string.printable:
                    result += 1
        return result


def get_most_common_non_ascii_char(file_path: str) -> str:
    count_words: Dict[str, int] = {}
    with open(file_path, encoding="unicode-escape") as text:
        for line in text:
            for word in line:
                if word not in string.printable and word != " ":
                    if word in count_words:
                        count_words[word] += 1
                    else:
                        count_words[word] = 1
    list_sorted_words = sorted(count_words.items(), reverse=True, key=lambda item: item[1])
    task_result = [i[0] for i in list_sorted_words if i[1] == list_sorted_words[0][1]]
    task_result = " ".join(task_result)
    return task_result


get_longest_diverse_words()
get_rarest_char()
count_punctuation_chars(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt"))
count_non_ascii_chars(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt"))
get_most_common_non_ascii_char(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt"))

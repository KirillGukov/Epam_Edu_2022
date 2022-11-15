import os
from hw_2.tasks.task_1 import get_longest_diverse_words, get_rarest_char, count_punctuation_chars,\
    count_non_ascii_chars, get_most_common_non_ascii_char
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")


def test_get_longest_diverse_words():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")
    actual_result = get_longest_diverse_words()
    assert actual_result == ['unmißverständliche', 'Bevölkerungsabschub', 'Kollektivschuldiger',
                             'Werkstättenlandschaft', 'Schicksalsfiguren', 'Selbstverständlich', 'Fingerabdrucks',
                             'Friedensabstimmung', 'außenpolitisch', 'Seinsverdichtungen']


def test_rarest_char():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")
    actual_result = get_rarest_char()
    assert actual_result == "â"


def test_punctuation_chars():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")
    actual_result = count_punctuation_chars(path)
    assert actual_result == 5305


def test_count_non_ascii_chars():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")
    actual_result = count_non_ascii_chars(path)
    assert actual_result == 2975


def test_most_common_non_ascii_char():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")
    actual_result = get_most_common_non_ascii_char(path)
    assert actual_result == "ä"

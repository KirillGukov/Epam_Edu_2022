from hw_4.tasks.task_1 import read_magic_number
import pytest


@pytest.mark.parametrize(["path", "expected_result"], [("file_name", True), ("text", False), ("else", False),
                                                         ("words", False)],)
def test_read_magic_number(path: str, expected_result: str):
    assert read_magic_number("file_name") == True
    assert read_magic_number("text") == ValueError
    assert read_magic_number("else") == ValueError
    assert read_magic_number("words") == ValueError

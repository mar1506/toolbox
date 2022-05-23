from toolbox.toolbox.functions import duplicate_count


def test_find_it():
    assert find_it (52) == 0

def test_duplicate_count():
    assert duplicate_count('aabbcde') == 2

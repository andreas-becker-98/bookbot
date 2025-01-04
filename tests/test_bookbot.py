from ..main import count_words

def test_count_words():
    assert count_words("") == 0
    assert count_words("abba") == 1
    assert count_words("abba a ear sadea\n    ea") == 5
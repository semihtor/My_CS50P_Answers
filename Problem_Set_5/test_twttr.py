from twttr import shorten

def test_only_lowercase_vowels():
    assert shorten("twitaouter") == "twttr"

def test_only_uppercase_vowels():
    assert shorten("TWITAOUTER") == "TWTTR"

def test_upper_and_lowercase_vowels():
    assert shorten("TWITAOUTER twitaouter") == "TWTTR twttr"

def test_no_vowels():
    assert shorten("GYPSY crypt") == "GYPSY crypt"

def test_no_letters():
    assert shorten("123!:%_") == "123!:%_"

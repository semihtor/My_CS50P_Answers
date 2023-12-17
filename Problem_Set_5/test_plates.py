from plates import is_valid

def test_meets_all_conditions():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("EVIL1") == True
    assert is_valid("GOOD1") == True

 # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_minimum_and_maximum_characters():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFG') == False

# “All vanity plates must start with at least two letters.”
def test_starting_with_at_least_two_letters():
    assert is_valid("50") == False
    assert is_valid("1A") == False
    assert is_valid("H1") == False
    assert is_valid("AB") == True

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def test_not_ending_with_number():
    assert is_valid("AAA11A") == False
    assert is_valid("AA11A") == False
    assert is_valid("AA1A") == False

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def test_first_number_is_zero():
    assert is_valid("AA0") == False
    assert is_valid("AA0A") == False

# “No periods, spaces, or punctuation marks are allowed.”
def test_contains_period_space_or_punctuation():
    assert is_valid("HI BYE") == False
    assert is_valid("HI_BYE") == False
    assert is_valid("HI.BYE") == False

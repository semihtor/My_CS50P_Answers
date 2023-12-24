from um import count


def test_word_containing_um():
    assert count("yummy") == 0
    assert count("human") == 0
    assert count("thumb") == 0
    assert count("mummy") == 0

def test_upper_or_lowercase():
    assert count("Um, thanks for the album.") == 1
    assert count("UM, THANKS, UM....") == 2
    assert count("um, um....") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

def test_um_starting_and_ending_spaces():
    assert count("     um") == 1
    assert count("um     ") == 1
    assert count("     um      ") == 1


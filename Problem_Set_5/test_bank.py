from bank import value

def test_return_100():
    assert value("What's happening?") == 100
    assert value("asdfghjkl") == 100

def test_return_twenty():
    assert value("Hi") == 20
    assert value("How you doing?") == 20
    assert value("Hey") == 20
    assert value("Howdy") == 20
    assert value("How are you?") == 20


def test_return_zero():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("HelLo") == 0
    assert value("HELLO Newman") == 0
    assert value("hello Jerry") == 0
    assert value("Hello Kramer") == 0

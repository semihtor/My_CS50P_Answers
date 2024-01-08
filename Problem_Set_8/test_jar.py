from jar import Jar
import pytest


def test_init():
    jar_1 = Jar()
    assert jar_1.capacity == 12
    jar_2 = Jar(6)
    assert jar_2.capacity == 6
    with pytest.raises(ValueError):
        jar_3 = Jar(-6)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(6)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(11)
    jar.deposit(11)
    jar.withdraw(5)
    assert jar.size == 6
    jar.withdraw(5)
    assert jar.size == 1

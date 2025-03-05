from numb3rs import validate
import pytest

def main():
    test_validate()
    test_validate1()
    

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.0") == True

def test_validate1():
    assert validate("275.2.3.4") == False
    assert validate("512.512.512.512") == False
    assert validate("1.555.555.555") == False
    assert validate("cat") == False


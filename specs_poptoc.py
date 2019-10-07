import pytest

from pop_toc_functions import *

def test_div3():
    assert div3(15) == True

def test_div32():
    assert div3(10) == False

def test_div5():
    assert div5(15) == True

def test_div52():
    assert div5(12) == False

def test_dev35():
    assert dev35(15) == True

def test_dev352():
    assert dev35(12) == False
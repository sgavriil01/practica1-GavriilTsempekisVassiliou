import pytest
from triangulo import checktriangle

def test_case1():
    assert checktriangle(6, 5, 10) == "Equal-sided triangle"

def test_case2():
    assert checktriangle(6, 6, 6) == "Equilateral triangle"

def test_case3():
    assert checktriangle(3, 3, 4) == "Isosceles triangle"

def test_case4():
    assert checktriangle(4, 3, 0) == "It is not a triangle"

def test_case5():
    assert checktriangle(8, 2, 4) == "It is not a triangle"

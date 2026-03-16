import pytest
from triangulo import checktriangle

def test_scalene_triangle():
    assert checktriangle(6, 5, 10) == "Scalene triangle"

def test_equilateral_triangle():
    assert checktriangle(6, 6, 6) == "Equilateral triangle"

def test_isosceles_ab():
    assert checktriangle(3, 3, 4) == "Isosceles triangle"

def test_isosceles_bc():
    assert checktriangle(4, 3, 3) == "Isosceles triangle"

def test_isosceles_ac():
    assert checktriangle(3, 4, 3) == "Isosceles triangle"

def test_not_triangle_zero():
    assert checktriangle(4, 3, 0) == "It is not a triangle"

def test_not_triangle_invalid():
    assert checktriangle(8, 2, 4) == "It is not a triangle"
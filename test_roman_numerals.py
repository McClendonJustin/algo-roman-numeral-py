from roman_numerals import to_roman, to_roman_lazy
import pytest

def test_01_a_single_number():
    assert to_roman(4) == "IV"

def test_02_odd_numerals():
    assert to_roman(150) == 'CL'

def test_03_all_edge_cases():
    assert to_roman(944) == 'CMXLIV'
    
def test_04_all_edge_cases():
    assert to_roman_lazy(4) == 'IIII'
    
def test_05_all_edge_cases():
    assert to_roman_lazy(150) == 'CL'
    
def test_06_all_edge_cases():
    assert to_roman_lazy(944) == 'DCCCCXXXXIIII'
    
# add tests to cover different edge cases

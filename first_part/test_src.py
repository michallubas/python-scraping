# Your tests here

import pytest
from first_part.src import longest_word

def test_logest_word():
    test_array_1 = ['milk', 'catalog', 'c+', 'python', 'cat', 'dog']
    test_array_1_result = 'cat'

    assert longest_word(test_array_1) == test_array_1_result

# Your tests here

import pytest
import re
from first_part.src import longest_word, run_nutrition


def test_logest_word():
    test_array_1 = ['milk', 'catalog', 'c+', 'python', 'cat', 'dog']
    test_array_1_result = 'cat'

    assert longest_word(test_array_1) == test_array_1_result


def test_matches():

    matches = run_nutrition()

    assert matches[0] == 'Vitamine C-D3 : 160'
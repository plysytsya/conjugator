# -*- coding: utf-8 -*-

import pytest
from conjugator.skeleton import fib

__author__ = "Pavlo Lysytsya"
__copyright__ = "Pavlo Lysytsya"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

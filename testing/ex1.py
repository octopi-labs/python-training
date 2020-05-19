import pytest


def test_assertions():
    assert "hello" != "Hai"  # is an assertion failure.
    assert 4 == 4  # is a successful assertion
    assert True  # is a successful assertion
    assert not False  # is an assertion failure.
import pytest

def test_file1_method4():
    x = 5
    y = 6
    with pytest.raises(AssertionError):
        assert x == y,"test failed"
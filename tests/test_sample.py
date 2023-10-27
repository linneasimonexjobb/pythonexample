"""Testing file for python project."""


from project import small_func


def test_small_func_func():
    """Test function func in file small_func."""
    assert small_func.func(3) == 4


def test_small_func_another_func():
    """Test function another_func i file small_func."""
    assert small_func.another_func(3) == 5

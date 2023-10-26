from project import small_func


def test_small_func_func():
    assert small_func.func(3) == 4


def test_small_func_another_func():
    assert small_func.another_func(3) == 5

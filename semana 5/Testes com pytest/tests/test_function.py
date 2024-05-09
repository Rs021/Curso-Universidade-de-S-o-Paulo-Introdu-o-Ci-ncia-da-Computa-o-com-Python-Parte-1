import functions as ft


def test_fac():
    assert ft.factorial(1) == 1
    assert ft.factorial(2) == 2
    assert ft.factorial(3) == 6
    assert ft.factorial(4) == 24
    assert ft.factorial(5) == 120
    assert ft.factorial(6) == 720
    assert ft.factorial(7) == 5040
    assert ft.factorial(8) == 40320
    assert ft.factorial(9) == 362880
    assert ft.factorial(10) == 3628800


def test_bin():
    assert ft.binominal(9,8) == 9
    assert ft.binominal(7,4) == 35
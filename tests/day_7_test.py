from advent.day_7 import absolute_difference, sum_natural, absolute_summed_difference

EXAMPLE = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_absolute_difference():
    assert absolute_difference(EXAMPLE, 2) == 37  # from website
    assert absolute_difference(EXAMPLE, 1) == 41
    assert absolute_difference(EXAMPLE, 10) == 71


def test_sum_natural():
    assert sum_natural(16 - 5) == 66
    assert sum_natural(5 - 1) == 10


def test_absolute_summed_difference():
    assert absolute_summed_difference(EXAMPLE, 5) == 168
    assert absolute_summed_difference(EXAMPLE, 2) == 206

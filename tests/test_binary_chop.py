import pytest

from katas.binary_chop import chop


@pytest.mark.parametrize(
    "target_value, array_of_ints, expected_output",
    [
        (3, [], -1),
        (3, [1], -1),
        (1, [1], 0),
        (1, [1, 3, 5], 0),
        (3, [1, 3, 5], 1),
        (5, [1, 3, 5], 2),
        (2, [1, 3, 5], -1),
        (4, [1, 3, 5], -1),
        (6, [1, 3, 5], -1),
        (1, [1, 3, 5, 7], 0),
        (3, [1, 3, 5, 7], 1),
        (5, [1, 3, 5, 7], 2),
        (7, [1, 3, 5, 7], 3),
        (0, [1, 3, 5, 7], -1),
        (2, [1, 3, 5, 7], -1),
        (4, [1, 3, 5, 7], -1),
        (6, [1, 3, 5, 7], -1),
        (8, [1, 3, 5, 7], -1),
    ],
)
def test_chop(target_value, array_of_ints, expected_output):
    assert chop(target_value, array_of_ints) == expected_output

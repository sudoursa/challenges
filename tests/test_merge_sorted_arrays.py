from sololearn.challenges.merge_sorted_arrays import get_user_input, merge_arrays
import sys


def test_get_user_input():
    # given
    with open("get_user_input_preprogrammed_inputs.txt") as inputs:
        sys.stdin = inputs

    # when
        array = get_user_input()

    # then
    expected = [1, 2, 3]
    assert array == expected


def test_merge_arrays():
    # given
    with open("get_user_input_preprogrammed_inputs.txt") as inputs:
        sys.stdin = inputs

    # when
        merged_array = merge_arrays(get_user_input(), get_user_input())

    # then
    expected = [1, 2, 3, 4, 5, 6]
    assert merged_array == expected

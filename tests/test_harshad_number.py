from sololearn.challenges.harshad_number import harshad_tester, bonus_range_tester
import pytest


@pytest.mark.parametrize('user_input', ['18', '1729'])
def test_harshad_tester(user_input):
    # given
    user_input = user_input

    # when
    result = harshad_tester(user_input)

    # then
    expected_result = True
    assert expected_result == result


@pytest.mark.parametrize('user_input', [18, -13, '-18', 1.5, '1.5'])
def test_harshad_tester_with_invalid_input(user_input):
    # given
    user_input = user_input

    # when and then
    with pytest.raises(Exception) as e:
        harshad_tester(user_input)


def test_bonus_range_tester():
    # given
    user_input = '18'

    # when
    result = bonus_range_tester(user_input)

    # then
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18]
    assert result == expected_result

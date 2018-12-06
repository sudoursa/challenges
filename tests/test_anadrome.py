from sololearn.challenges.anadrome import anadrome_validator, anadrome_finder
import pytest


@pytest.mark.parametrize('user_input', ["solosolo", "SoloSolo", "cattaco", ])
def test_anadrome_validator(user_input):
    # given
    user_input = user_input

    # when
    result = anadrome_validator(user_input)

    # then
    expected_result = True
    assert result == expected_result


@pytest.mark.parametrize('user_input', ["badvalue", "anotherbadentry", "wrong", ])
def test_anadrome_validator_with_bad_entries(user_input):
    # given
    user_input = user_input

    # when
    result = anadrome_validator(user_input)

    # then
    expected_result = False
    assert result == expected_result


def test_anadrome_finder():
    # given
    user_input = "solosolo"

    # when
    result = anadrome_finder(user_input)

    # then
    possible_answers = ["soolloos", "oolssloo", "olsooslo", "lsoooosl", "soloolos", "slooools"]
    assert result in possible_answers

import pytest
from reddit.challenges.challenge370 import upc_checker


@pytest.mark.parametrize('upc_input, answer', [("4210000526", "4"), ("3600029145", "2"), ("12345678910", "4"),
                                               ("1234567", "0"), ])
def test_upc_checker(upc_input, answer):
    # given
    upc_input = upc_input

    # when
    result = upc_checker(upc_input)

    # then
    expected_result = answer
    assert result == expected_result


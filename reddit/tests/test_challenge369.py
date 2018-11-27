from reddit.challenges.challenge369 import hex_converter


def test_hex_converter():
    # given
    test_input_data = [255, 99, 71]

    # when
    result = hex_converter(*test_input_data)

    # then
    expected_result = "#FF6347"
    assert result == expected_result

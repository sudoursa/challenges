from reddit.challenges.challenge369 import hex_converter, hex_combiner, avg


def test_hex_converter():
    # given
    test_input_data = [255, 99, 71]

    # when
    result = hex_converter(*test_input_data)

    # then
    expected_result = "#FF6347"
    assert result == expected_result


def test_hex_combiner():
    # given
    test_hex1 = [250, 100, 50]
    test_hex2 = [150, 200, 100]

    # when
    test_hex1 = hex_converter(*test_hex1)
    test_hex2 = hex_converter(*test_hex2)
    result = hex_combiner(test_hex1, test_hex2)

    # then
    expected_result = "#C8964B"
    assert result == expected_result


def test_avg():
    # given
    test_number_list = [200, 100]

    # when
    result = avg(test_number_list)

    # then
    expected_result = 150

    assert result == expected_result

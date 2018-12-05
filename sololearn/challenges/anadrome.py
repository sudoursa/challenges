# Anadrome
#
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
# For example, "sool" is an anagram for "solo"
#
# A palindrome is a word or phrase which reads the same backward as forward, such as "madam."
#
# An anadrome is a word or phrase if any of its anagrams form a palindrome.
#
# For example:
# Input: "solosolo"
# Output: yes ("soolloos" is an anagram of "solosolo" which also is a palindrome).
#
# Input: "3haha"
# Output: yes ("ha3ah" is an anagram of "3haha" which also is a palindrome).Exception
#
# Input: "solo"
# Output: no
#
# Write a program to check if the user input is an anadrome or not.


def convert_string_to_dict(user_input):
    letter_counter = {}
    for _ in user_input:
        if _ in letter_counter:
            letter_counter[_] += 1
        else:
            letter_counter[_] = 1
    return letter_counter


def find_if_one_odd(letter_dict):
    one_odd = None
    for _ in letter_dict:
        if letter_dict[_] % 2 == 0:
            continue
        if letter_dict[_] % 2 == 1:
            if one_odd is None:
                one_odd = True
            else:
                one_odd = False
                break
    return one_odd


def anadrome_validator(user_input):
    letter_dict = convert_string_to_dict(user_input)
    if user_input == '':
        print('Input must cannot be blank.')
        return False
    elif find_if_one_odd(letter_dict) or find_if_one_odd(letter_dict) is None:
        return True
    else:
        return False


def anadrome_finder(user_input):
    if anadrome_validator(user_input):
        anagram_start = ''
        anagram_end = ''
        anagram_mid = ''
        letter_dict = convert_string_to_dict(user_input)
        if find_if_one_odd(letter_dict) is None:
            for k, v in letter_dict.items():
                anagram_start += k * int(v / 2)
                anagram_end = k * int(v / 2) + anagram_end
        else:
            for k, v in letter_dict.items():
                if v == 1:
                    anagram_mid = k
                else:
                    anagram_start += k * int(v / 2)
                    anagram_end = k * int(v / 2) + anagram_end
        return "{}{}{}".format(anagram_start, anagram_mid, anagram_end)
    else:
        raise ValueError("The provided input failed to validate as an anadrome")

# Harshad Number
#
# A harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
#
# for example:
# input: 18
# Output: true (18 is a Harshad number because it is divisible by the sum of its digits: 18 = (1+8) * 2)
#
# Input: 1729
# output: true (1729 is a harshad number because it is divisible by the sum of its digits:
# 1729 = (1 + 7 + 2 + 9) * 91
#
# Write a program to check if the user input is a Harshad number or not
#
# Bonus: print all of the harshad numbers in a given range


def harshad_tester(user_input):
    if type(user_input) == int:
        raise TypeError("You must enter input as a string")
    list_of_numbers = [int(_) for _ in user_input]
    sum_of_numbers = sum(list_of_numbers)
    if int(user_input) % sum_of_numbers == 0:
        return True
    else:
        return False


def bonus_range_tester(user_input):
    list_of_harshad_numbers = []
    for number in range(1, int(user_input) + 1):
        if harshad_tester(str(number)):
            list_of_harshad_numbers.append(int(number))
    return list_of_harshad_numbers

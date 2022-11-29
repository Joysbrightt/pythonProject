import string


def convert_to_roman(number):
    ans = 0
    roman_numeral = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 500,
        "M": 100

    }
    for number in number:
        if number in number < roman_numeral["X"]:
            return number + roman_numeral["X"]

    return


print(convert_to_roman("XX"))

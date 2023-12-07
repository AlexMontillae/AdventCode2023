def calibration_value(value: str) -> int:
    """
    Receives a string and returns the first and the last digit of it
    """
    numbers = list(filter(lambda x: x in '0123456789' , value))
    numbers = int(numbers[0] + numbers[-1])

    return numbers

def main(list_of_values: str) -> int:
    """
    Receives a text and return the sum of all the calibration values of all the strings
    """
    value = 0
    new_list = list_of_values.split('\n')
    new_list = list(map(lambda x: calibration_value(x), new_list))

    value = sum(new_list)

    return value

with open('day1text.txt') as text:
    s = text.read()

print(main(s))
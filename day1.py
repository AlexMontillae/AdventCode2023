def calibration_value(value: str) -> int:
    """
    Receives a string and returns the first and the last digit of it
    """
    def num_in_value(value: str) -> str:
        """
        receives a string and returns another string of digits and if there is any number spelled it also returns it as a digit
        F.E:'one' == '1'
            'two' == '2'
            ....
            'nine' == '9'
            """
        str_of_numbers = ''
        for i, elem in enumerate(value):
        
            if elem in '0123456789':
                str_of_numbers += elem
            elif value[i:i+3] == 'one':
                str_of_numbers += '1'
            elif value[i:i+3] == 'two':
                str_of_numbers += '2'
            elif value[i:i+5] == 'three':
                str_of_numbers += '3'
            elif value[i:i+4] == 'four':
                str_of_numbers += '4'
            elif value[i:i+4] == 'five':
                str_of_numbers += '5'
            elif value[i:i+3] == 'six':
                str_of_numbers += '6'
            elif value[i:i+5] == 'seven':
                str_of_numbers += '7'
            elif value[i:i+5] == 'eight':
                str_of_numbers += '8'
            elif value[i:i+4] == 'nine':
                str_of_numbers += '9'

        return str_of_numbers

    numbers = num_in_value(value)
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

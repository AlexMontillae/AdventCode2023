def main(text: str) -> int:

    total = 0
    with open(text) as text1:
        s = text1.read()
        s = s.split('\n')

        for elem in s:
            numeros, win = normalize_str(elem)
            total += points_of_wins(numeros, win)
    return total



def normalize_str(cadena):

    new_str = ''
    for i,char in enumerate(cadena):
        if char == ':':
            new_str = cadena[i+2:]
            break

    new_str = new_str.split(' | ')
    first = new_str[0].split(' ')
    first = [int(x) for x in first if x != '']
    second = new_str[1].split(' ')
    second = [int(x) for x in second if x != '']
    return first, second

def points_of_wins(numbers: list[int], winners: list[int]) -> int:
    total = 0

    for elem in numbers:
        if elem in winners:
            total += 1
    
    if total != 0:
        total = 2**(total-1)

    return total

print(main('day4text.txt'))
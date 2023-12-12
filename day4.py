def main(text: str) -> int:

    total_cards = {}
    total = 0

    with open(text) as text1:
        s = text1.read()
        s = s.split('\n')

        for n in range(1,len(s)+1):
            total_cards[n] = 1


        for elem in s:
            numeros, win, id = normalize_str(elem)
            aux = points_of_wins(numeros, win, id)

            for elem in aux:
                if elem in total_cards:
                    total_cards[elem] += total_cards[id]

        for n in range(1,len(s)+1):
            total += total_cards[n]
    
    return total

def normalize_str(cadena):

    new_str = ''
    aux = None
    for i,char in enumerate(cadena):
        if char == ':':
            new_str = cadena[i+2:]
            aux = cadena[:i]
            break

    new_str = new_str.split(' | ')
    first = new_str[0].split(' ')
    first = {int(x) for x in first if x != ''}
    second = new_str[1].split(' ')
    second = {int(x) for x in second if x != ''}

    id = []
    for elem in aux[::-1]:
        if elem == ' ':
            break
        else:
            id.insert(0,elem)
    id = ''.join(id)
    return first, second, int(id)

def points_of_wins(numbers: list[int], winners: list[int], card: int) -> list:
    total = []
    aux = card

    for elem in numbers:
        if elem in set(winners):
            total.append(aux + 1)
            aux += 1

    return total

print(main('day4text.txt'))
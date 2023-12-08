

def main(text: str) -> int:
    """
    Receives a text file and returns the sum of the products of the minimum sets of cubes per game
    """
    total = 0

    new_list = text.split('\n')
    new_list = list(map(lambda x: game_info(x), new_list))    
    total = sum(new_list)

    return total

def game_info(game: str) -> int:
    """
    Receives a string of the game and return the product of the minimum sets of cubes
    """
    # normalizamos nuestra cadena para solo obtener los valores despues del ':'
    new_list = ''
    for i,char in enumerate(game):
        if char == ':':
            new_list = game[i+1:]
            break
    new_list = new_list.split(';')
    
    green = 1
    red = 1
    blue = 1

    # iteramos por cada elemento de la nueva lista
    # verificamos si el numero es mayor que la variable por color
    # si es mayor sustituimos el valor por el numero actual
    for elem in new_list:
        for play in elem.split(','):
            if 'green' in play:
                if extract_num(play) > green:
                    green = extract_num(play)
            if 'blue' in play:
                if extract_num(play) > blue:
                    blue = extract_num(play)
            if 'red' in play:
                if extract_num(play) > red:
                    red = extract_num(play)

    result = green * blue * red
    return result

def extract_num(string: str) -> int:

    number = ''
    for char in string:
        if char.isnumeric():
            number += char
    
    return int(number)

with open('day2text.txt') as text:
    s = text.read()
print(main(s))




def main(text: str) -> int:
    """
    Receives a text file and returns the sum of the ID's of the games that passed the test
    """
    total = 0

    new_list = text.split('\n')
    new_list = list(map(lambda x: game_info(x), new_list))
    for i, elem in enumerate(new_list):
        if elem == True:
            total += i +1

    return total

def game_info(game: str) -> bool:
    """
    Receives a string of the game and return a bool)
    The bool value = True if the game is possible
    The bool value = False if the game is not possible
    A game is possible if the sum of all the number of times <= 12 red, 13 green and 14 blue
    """

    # inicializamos nuestra variable
    result = False
    # normalizamos nuestra cadena para solo obtener los valores despues del ':'
    new_list = ''
    for i,char in enumerate(game):
        if char == ':':
            new_list = game[i+1:]
            break
    new_list = new_list.split(';')
    
    

    # iteramos por cada elemento de la nueva lista
    # agregamos el valor de cada jugada a las variables de colores
    for elem in new_list:

        # una vez ya normalizada, creamos las variables green, red and blue para almacenar la canditad de veces que aparecen los cubos por jugada
        green = 0
        red = 0
        blue = 0
        for play in elem.split(','):
            if 'green' in play:
                green += extract_num(play)
            if 'blue' in play:
                blue += extract_num(play)
            if 'red' in play:
                red += extract_num(play)

        # ahora vemos si la cantidad de veces que salen los cubos es posible 
        if red <= 12 and green <= 13 and blue <= 14:
            result = True
        else:
            result = False
            break
    

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


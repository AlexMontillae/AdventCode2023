def main(text: str) -> int:

    s = None
    new = 0
    with open(text) as text1:
        s = text1.read()
      
        s = s.split('\n')
        for i,elem in enumerate(s):
            for j,char in enumerate(elem):
                if char == '*':
                    new += adjacent_nums(s,i,j)
    
    return new


def adjacent_nums(list_of_str: list[str], i , j)-> int:

    total = []

    left = list_of_str[i][j-1]
    right = list_of_str[i][j+1]
    up = list_of_str[i-1][j]
    down = list_of_str[i+1][j]
    up_left = list_of_str[i-1][j-1]
    up_right = list_of_str[i-1][j+1]
    down_left = list_of_str[i+1][j-1]
    down_right = list_of_str[i+1][j+1]

    if left.isalnum():
        total.append(right_or_left('left', list_of_str[i][j-3:j]))
    if right.isalnum():
        total.append(right_or_left('right', list_of_str[i][j+1:j+4]))
    if up.isalnum() and up_left.isalnum() and not up_right.isalnum():
        total.append(right_or_left('left', list_of_str[i-1][j-2:j+1]))
    if up.isalnum() and up_right.isalnum() and not up_left.isalnum():
        total.append(right_or_left('right', list_of_str[i-1][j:j+3]))
    if up.isalnum() and up_right.isalnum() and up_left.isalnum():
        total.append(right_or_left('middle', list_of_str[i-1][j-1:j+2]))
    if up_left.isalnum() and not up.isalnum():
        total.append(right_or_left('left', list_of_str[i-1][j-3:j]))
    if up_right.isalnum() and not up.isalnum():
        total.append(right_or_left('right', list_of_str[i-1][j+1:j+4]))
    if up.isalnum() and not up_right.isalnum() and not up_left.isalnum():
        total.append(int(list_of_str[i-1][j]))
    if down.isalnum() and down_left.isalnum() and not down_right.isalnum():
        total.append(right_or_left('left',list_of_str[i+1][j-2:j+1]))
    if down.isalnum() and down_right.isalnum() and not down_left.isalnum():
        total.append(right_or_left('right', list_of_str[i+1][j:j+3]))
    if down_left.isalnum() and not down.isalnum():
        total.append(right_or_left('left', list_of_str[i+1][j-3:j]))
    if down_right.isalnum() and not down.isalnum():
        total.append(right_or_left('right', list_of_str[i+1][j+1:j+4]))
    if down.isalnum() and down_right.isalnum() and down_left.isalnum():
        total.append(right_or_left('middle', list_of_str[i+1][j-1:j+2]))
    if down.isalnum() and not down_right.isalnum() and not down_left.isalnum():
        total.append(int(list_of_str[i+1][j]))

    if len(total) == 2:
        from functools import reduce
        total = reduce(lambda x,y: x*y, total)
    else:
        total = 0

    return total

def right_or_left(decision: str, iterable:str) -> str:

    total = ''
    if decision == 'right':
        for elem in iterable:
            if elem == '.':
                break
            else:
                total += elem
    elif decision == 'left':
        total = []
        for elem in iterable[::-1]:
            if elem == '.':
                break
            else:
                total.insert(0,elem)
        total = ''.join(total)
    elif decision == 'middle':
        total = iterable

    return int(total)



print(main('day3text.txt'))

def modif(s):

    char = ''

    if s == 0:
        char = '    '
    elif s == 1:
        char = ' X '
    elif s == 2:
        char = ' O '
    else:
        char = 'F'

    return char

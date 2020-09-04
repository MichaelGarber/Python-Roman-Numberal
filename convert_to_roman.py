def convert_to_roman(num):
    input = ''
    number = [
        1,
        4,
        5,
        9,
        10,
        40,
        50,
        90,
        100,
        400,
        500,
        900,
        1000
    ]

    numeral = [
        'I',
        'IV',
        'V',
        'IX',
        'X',
        'XL',
        'L',
        'XC',
        'C',
        'CD',
        'D',
        'CM',
        'M'
    ]

    pos = len(number) - 1


    while(pos > -1):
        if number[pos] <= num:
            num -= number[pos]
            input += (numeral[pos])
        else:
            pos -= 1
    return input


def decimal_to_roman(num):
    if not isinstance(num, int) or num <= 0 or num >= 4000:
        raise ValueError("El número debe ser un entero entre 1 y 3999")
    
    val_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_num = ''
    for value, symbol in val_to_roman:
        while num >= value:
            roman_num += symbol
            num -= value
    return roman_num
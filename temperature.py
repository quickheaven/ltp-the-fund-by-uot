def convert_to_celsius(fahrenheit):
    '''(number) -> float

    Return the number of Celsius degrees from Fahrenheit.

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5 / 9

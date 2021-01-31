def entire_alpha_and_numeric(s):
    ''' (str) -> Bool

    Returns True when variable refers to str that is entirely alphabetic or entirely numeric, and that False if the str is not entirely alphabetic and not entirely numeric

    >>> entire_alpha_and_numeric('abc')
    >>> True
    >>> entire_alpha_and_numeric('123')
    >>> True
    >>> entire_alpha_and_numeric('abc123')
    >>> False
    '''
    return s.isalpha() or s.isnumeric()    
    
def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that appear at leastonce in s2. The characters in the result        will appear in the same order asthey appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abb', 'ab')
    'abb' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''

    res = ''

    for ch in s1:
        if ch in s2:
            res = res + ch
    
    return res

def happy_30th(message):
    ''' (str) -> str

    Returns Happy 30th!

    >>> happy_30th('Happy 29th!')
    >>> Happy 30th!
    '''
    new_message = ''
    for char in message:
        if char.isdigit():
            new_message = new_message + str((int(char) + 1) % 10)
        else:
            new_message = new_message + char     
        
    return new_message;
    

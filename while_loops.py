def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s) - 1
    while i >= 0:
        if s[i] in 'aeiouAEIOU':
            return s[i]
        i = i - 1
    return None


def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives a valid response. Return the answer.
    '''
    
    answer = input(prompt)

    while not (answer == 'yes' or answer  == 'no'):
        answer = input(prompt)
    return answer


def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of a s from index 0 up to but not including the first bowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''

    before_vowel = ''
    i = 0

    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1
    return before_vowel

#!/usr/bin/env python3

# ukol za 2 body
def first_odd_or_even(numbers):
    """Returns 0 if there is the same number of even numbers and odd numbers
       in the input list of ints, or there are only odd or only even numbers.
       Returns the first odd number in the input list if the list has more even
       numbers.
       Returns the first even number in the input list if the list has more odd
       numbers

    >>> first_odd_or_even([2,4,2,3,6])
    3
    >>> first_odd_or_even([3,5,4])
    4
    >>> first_odd_or_even([2,4,3,5])
    0
    >>> first_odd_or_even([2,4])
    0
    >>> first_odd_or_even([3])
    0
    """

    even_list = [x for x in numbers if not x % 2]
    odd_list = [x for x in numbers if x % 2]
    if (len(odd_list) > len(even_list)) and (len(even_list) > 0):
        return even_list[0]
    if (len(even_list) > len(odd_list)) and (len(odd_list) > 0):
        return odd_list[0]

    return 0



# ukol za 3 body
def to_pilot_alpha(word):
    """Returns a list of pilot alpha codes corresponding to the input word

    >>> to_pilot_alpha('Smrz')
    ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """

    pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
                   'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
                   'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
                   'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

    pilot_alpha_list = []

    letters = word.upper()
    for letter in letters:
        out = [x for x in pilot_alpha if x.startswith(letter)]
        pilot_alpha_list.append(out[0])
    return pilot_alpha_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
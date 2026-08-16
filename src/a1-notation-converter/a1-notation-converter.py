ASCII_A_INDEX = 65
ASCII_Z_INDEX = 90
ALPHABET_AMOUNT = 26

def int_to_a1(number : int, strating_index : int = 1) -> str:
    if (not type(number) is int):
        raise TypeError(
            f"The type of argument 'number' of function 'int_to_a1()' needs to be type 'int'.\n"
            f"Current received type of 'number': {type(number)}."
        )
    elif (number <= 0):
        raise ValueError(
            "The given value of argument 'number' of function 'int_to_a1()' cannot be <= 0.\n"
            f"Current received value of 'number': {number}."
        )
    else:
        if (number <= ALPHABET_AMOUNT):
            return chr(ASCII_A_INDEX + number - strating_index)
        else:
            remainder = number % ALPHABET_AMOUNT
            return int_to_a1((number - remainder) // ALPHABET_AMOUNT) + chr(ASCII_A_INDEX + remainder - strating_index)

def a1_to_int(a1_notation : str) -> int:
    if (not type(a1_notation) is str):
        raise TypeError(
            f"The type of argument 'a1_notation' of function 'a1_to_int()' needs to be type 'str'.\n"
            f"Current received type of 'a1_notation': {type(a1_notation)}."
        )
    else:
        number = 0
        a1_notation_len = len(a1_notation)
        a1_notation = a1_notation.upper()
        
        for character_index in range(a1_notation_len):
            character_ascii = ord(a1_notation[character_index])
            if (character_ascii < ASCII_A_INDEX or character_ascii > ASCII_Z_INDEX):
                raise ValueError(
                    f"The string argument 'a1_notation' of function 'a1_to_int()' consists of invalid character.\n"
                    f"Invalid character '{a1_notation[character_index]}' detected at index {character_index} of argument 'a1_notation'.\n"
                    f"Current received value of 'a1_notation': '{a1_notation}'.\n"
                    f"Allowed characters are within the range of a-z and A-Z."
                )
            else:
                number += (ord(a1_notation[character_index]) - ASCII_A_INDEX + 1) * ALPHABET_AMOUNT**(a1_notation_len - character_index - 1)

        return number

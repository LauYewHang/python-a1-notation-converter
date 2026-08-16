ASCII_A_INDEX = 65
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

from typing import TypedDict
import re

ASCII_A_INDEX = 65
ASCII_Z_INDEX = 90
ALPHABET_AMOUNT = 26
DEFAULT_STARTING_INDEX = 1

def int_to_a1(number : int, starting_index : int = DEFAULT_STARTING_INDEX) -> str:
    if (not type(number) is int):
        raise TypeError(
            f"The type of argument 'number' of function 'int_to_a1()' needs to be type 'int'.\n"
            f"Current received type of 'number': {type(number)}."
        )
    elif (not type(starting_index) is int):
        raise TypeError(
            f"The type of argument 'starting_index' of function 'int_to_a1()' needs to be type 'int'.\n"
            f"Current received type of 'starting_index': {type(starting_index)}"
        )
    elif (number < starting_index):
        raise ValueError(
            "The given value of argument 'number' of function 'int_to_a1()' cannot be less than argument 'starting_index'.\n"
            f"Current received value of 'number': {number}.\n"
            f"Current received value of 'starting_index': {starting_index}"
        )
    else:
        number += (DEFAULT_STARTING_INDEX - starting_index)
        if (number <= ALPHABET_AMOUNT):
            return chr(ASCII_A_INDEX + number - 1)
        else:
            remainder = ALPHABET_AMOUNT if number % ALPHABET_AMOUNT == 0 else number % ALPHABET_AMOUNT
            return int_to_a1((number - remainder) // ALPHABET_AMOUNT) + int_to_a1(remainder)

def a1_to_int(a1_notation : str, starting_index : int = DEFAULT_STARTING_INDEX) -> int:
    if (not type(a1_notation) is str):
        raise TypeError(
            f"The type of argument 'a1_notation' of function 'a1_to_int()' needs to be type 'str'.\n"
            f"Current received type of 'a1_notation': {type(a1_notation)}."
        )
    elif (not type(starting_index) is int):
        raise TypeError(
            f"The type of argument 'starting_index' of function 'a1_to_int()' needs to be type 'int'.\n"
            f"Current received type of 'starting_index': {type(starting_index)}"
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

        return number - (DEFAULT_STARTING_INDEX - starting_index)

def column_row_to_a1(column : int, row : int, inverse : bool = False) -> str:
    if (not type(column) is int or not type(row) is int):
        raise TypeError(
            f"The type of argument 'column' and 'row' of function 'column_row_to_a1()' needs to be type 'int'.\n"
            f"Current received type of 'column': {type(column)}.\n"
            f"Current received type of 'row': {type(row)}."
        )
    else:
        return f"{int_to_a1(column)}{row}" if not inverse else f"{int_to_a1(row)}{column}"

ColumnRowDict = TypedDict("ColumnRowDict", {"column" : int, "row" : int})
def a1_to_column_row(a1_notation : str) -> ColumnRowDict:
    if (not type(a1_notation) is str):
        raise TypeError(
            f"The type of argument 'a1_notation' of function 'a1_to_column_row()' needs to be type 'str'.\n"
            f"Current received type of 'a1_notation': {type(a1_notation)}."
        )
    elif (re.compile("[a-zA-Z]+[0-9]+$").match(a1_notation) == None):
        raise ValueError(
            f"The given value of argument 'a1_notation' of function 'a1_to_column_row()' does not match the regular expression '[a-zA-Z]+[0-9]+$'."
            f"Current received value of 'a1_notation': {a1_notation}."
        )
    else:
        column_value = re.compile("[a-zA-Z]+").search(a1_notation).group(0)
        row_value = re.compile("[0-9]+").search(a1_notation).group(0)
        return {"column" : a1_to_int(column_value), "row" : int(row_value)}

# Documentation

## Available functions
[int_to_a1(number, starting_index = 1)](#int_to_a1number-starting_index--1)  
Convert the given number to its A1 notation.  

[a1_to_int(a1_notation, starting_index = 1)](#a1_to_inta1_notation-starting_index--1)  
Convert the given A1 notation to its integer representation.

[column_row_to_a1(column, row, inverse = False)](#a1_to_column_rowa1_notation)  
Convert the given column and row integer to an A1 notation.

[a1_to_column_row(a1_notation)](#a1_to_column_row(a1_notation))  
Convert the given A1 notation to a dictionary with column and row keys.

## Functions details
### int_to_a1(number, starting_index = 1)  
Convert the given number to its A1 notation.  
- Arguments:
    - number: An integer, the number to be converted to A1 notation. The value of argument `number` cannot be less than the value of argument `starting_index`, else a ValueError would be raised.
    - starting_index: An integer, the value that represents the A1 notation "A", default to 1. I.e.  
        When starting_index = 0:
        ```
        0  = 'A'
        1  = 'B'
        25 = 'Z'
        26 = 'AA'
        ```
        When starting_index = 1:
        ```
        1  = 'A'
        2  = 'B'
        26 = 'Z'
        27 = 'AA'
        ```
        When satrting_index = -1:
        ```
        -1 = 'A'
         0 = 'B'
        24 = 'Z'
        25 = 'AA'
        ```
- Return:  
A string that represents the A1 notation of the given nunber.
- Example
    ```python
    int_to_a1(1)        # returns "A"
    int_to_a1(26)       # returns "Z"
    int_to_a1(27)       # returns "AA"

    int_to_a1(1, 0)     # returns "B"
    int_to_a1(26, 0)    # returns "AA"

    int_to_a1(1, -1)    # returns "C"
    int_to_a1(26, -1)   # returns "AB"

    int_to_a1(0)        # raise ValueError, number is less than starting_index (default 1)
    ```
***

### a1_to_int(a1_notation, starting_index = 1)
Convert the given A1 notation to its integer representation.
- Arguments:
    - a1_notation: A string, the A1 notation to be converted into an integer.
    - starting_index: An integer, the value that represents the A1 notation "A", default to 1.
- Return:  
An integer that represents the given A1 notation.
- Example:  
    ```python
    a1_to_int("A")      # returns 1
    a1_to_int("AA")     # returns 27

    a1_to_int("A", 0)   # returns 0
    a1_to_int("AA", 0)  # returns 26

    a1_to_int("A", -1)  # returns -1
    a1_to_int("AA", -1) # returns 25
    ```
***
### column_row_to_a1(column, row, inverse = false)
Convert the given column and row integer to an A1 notation. The value that represents A1 notation "A" is 1.
- Arguments:
    - column: An integer, represents the column's index.
    - row: An integer, represents the row's index.
    - inverse: A boolean, represents if the column and row are inverse.
- Return:  
A string that represents the A1 notation of the given column and row.
- Example:  
    ```python
    column_row_to_a1(1, 1)      # return "A1"
    column_row_to_a1(3, 26)     # return "C26"
    column_row_to_a1(53, 32)    # return "BA32"
    
    column_row_to_a1(3, 26, inverse = True)     # return "Z3"
    column_row_to_a1(32, 53, inverse = True)    # return "AF53"

    column_row_to_a1(0, 1)      # raise ValueError, value of column cannot be less than 1
    column_row_to_a1(1, 0)      # raise ValueError, value of row cannot be less than 1
    ```
***
### a1_to_column_row(a1_notation)
Convert the given A1 notation to a dictionary with column and row keys. The value that represents A1 notation "A" is 1.
- Arguments:
    - a1_notation: A string, the A1 notation to be converted.
- Return:  
A dictionary with keys ["column", "row"].
- Example:  
    ```python
    ans1 = a1_to_column_row("A3")   # return {"column" : 1, "row" : 3}
    ans1["column"]                  # return 1
    ans1["row"]                     # return 3

    ans2 = a1_to_column_row("AZ23") # return {"column" : 52, "row" : 23}
    ans2["column"]                  # return 52
    ans2["row"]                     # return 23
    ```

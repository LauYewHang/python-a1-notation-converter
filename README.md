# A1 notation converter
The A1 notation converter library allows the user to convert integer to its A1 notation form and vice versa. In this context, the [A1 notation](https://developers.google.com/workspace/sheets/api/guides/concepts#a1-notation) refer to the syntax used in spreadsheet program such as Google Sheets and Microsoft Excel to represent the index of column within the spreadhseet.  
E.g. 'G' represents 7th column, 'AZ' represents 52th column.
***

## Installation
Installation of this library can be done with Python `pip`:  
`pip install a1-notation-converter`
***

## Example
Converting integer to A1 notation:
```python
int_to_a1(1)       # return "A"
int_to_a1(27)      # return "AA"
int_to_a1(731)     # return "ABC"
```

Converting A1 notation to integer:
```python
a1_to_int("A")      # return 1
a1_to_int("AA")     # return 27
a1_to_int("CBA")    # return 2081
```
***

## Documentation
**int_to_a1( )**  
Syntax:
`int_to_a1(number : int, starting_index : int = 1) -> str`

Arguments:
- number: The integer that is going to be converted to A1 notation.
- starting_index: Specify whether the A1 notation 'A' represents the 0th column or 1st column. Default to ```starting_index = 1```.

Return:  
A string represents the A1 notation of the given integer.  

**a1_to_int( )**  
Syntax:
`a1_to_int(a1_notation : str) -> int`

Arguments:
- a1_notation: The string that is going to be converted to integer representation.

Return:  
An integer represents the number value of the given string.

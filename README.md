# A1 notation converter
The A1 notation converter library allows the user to convert integer to its A1 notation form and vice versa. In this context, the [A1 notation](https://developers.google.com/workspace/sheets/api/guides/concepts#a1-notation) refer to the syntax used in spreadsheet program such as Google Sheets and Microsoft Excel to represent the index of column within the spreadhseet.  
E.g. 'G' represents 7th column, 'AZ' represents 52th column.
***

## Version 1.1.0
- Fixed logic error when converting int to a1 notation using int_to_a1() with starting_index = 0 results in wrong answer being returned. I.e.  
```
int_to_a1(26, 0) # return "[" (should be "AA")
int_to_a1(52, 0) # return "A[" (should be "BA")
```
- Added function column_row_to_a1() to convert provided column and row into a1 notation.
- Added function a1_to_column_row() to convert provided a1 notation into dictionary that contains column and row keys.
***

## Installation
Installation of this library can be done with Python `pip`:  
`pip install a1-notation-converter`  
The package and release history can be found at [pypi.org](https://pypi.org/project/a1-notation-converter/).
***

## Example
Importing the library:
```python
from a1_notation_converter import a1_converter
```

Converting integer to A1 notation:
```python
a1_converter.int_to_a1(1)       # return "A"
a1_converter.int_to_a1(27)      # return "AA"
a1_converter.int_to_a1(731)     # return "ABC"
```

Converting A1 notation to integer:
```python
a1_converter.a1_to_int("A")      # return 1
a1_converter.a1_to_int("AA")     # return 27
a1_converter.a1_to_int("CBA")    # return 2081
```
***

## Documentation
Documentation can be found at this [GitHub repository](https://github.com/LauYewHang/python-a1-notation-converter/tree/master/docs).

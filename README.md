# A1 notation converter
The A1 notation converter library allows the user to convert integer to its A1 notation form and vice versa. In this context, the [A1 notation](https://developers.google.com/workspace/sheets/api/guides/concepts#a1-notation) refer to the syntax used in spreadsheet program such as Google Sheets and Microsoft Excel to represent the index of column within the spreadhseet.  
E.g. 'G' represents 7th column, 'AZ' represents 52th column.
***

## Latest releases
### Version 1.2.0
- Added class `A1Notation`.
```python
from a1_notation_converter.A1Notation import *

# default object instantiation
n1 = A1Notation("A12")
print(n1.a1_notation)       # print "A12"
print(n1.column)            # print 1
print(n1.row)               # print 12

n1.column = 3               # set the column value to 3 and changed the a1_notation value
print(n1.a1_notation)       # print "C12"

# object instantiation with column and row
n2 = A1Notation.from_column_row(column = 3, row = 23)
print(n2.a1_notation)       # print "C23"

# A1Notation arithmetic
n3 = A1Notation("B11")
n4 = A1Notation("D2")

n5 = n3 + n4                # add the A1Notation objects' column and row together
print(n5.a1_notation)       # print "F13"

n6 = n3 + [4, 5]            # add 4 with n3.column, and add 5 with n3.row
print(n6.a1_notation)       # print "F16"

n7 = n3 + (4, 5)            # add 4 with n3.column, and add 5 with n3.row
print(n7.a1_notation)       # print "F16"

n8 = n3 + {"column" : 4, "row" : 5}     # add dictionary's 'column' and 'row' value with A1Notation object's column and row
print(n8.a1_notation)       # print "F16"
```
***

## Installation
Installation of this library can be done with Python `pip`:  
`pip install a1-notation-converter`  
The package and release history can be found at [pypi.org](https://pypi.org/project/a1-notation-converter/).
***

## Quickstart
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

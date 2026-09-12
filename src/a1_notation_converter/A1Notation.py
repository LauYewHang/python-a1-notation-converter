from typing import overload

from a1_notation_converter.a1_converter import *

# A1Notation class
class A1Notation:
    def __init__(self, a1_notation : str):
        try:
            column_row_dict = a1_to_column_row(a1_notation)
            self._a1_notation = a1_notation
            self._column = column_row_dict["column"]
            self._row = column_row_dict["row"]
        except TypeError as e:
            raise TypeError(
                f"The type of argument 'a1_notation' of class instantiation 'A1Notation()' needs to be type 'str'.\n"
                f"Current received type of 'a1_notation': {type(a1_notation)}."
            )
        except ValueError as e:
            raise ValueError(
                f"The given value of argument 'a1_notation' of class instantiation 'A1Notation' does not match the regular expression '[a-zA-Z]+[0-9]+$'."
                f"Current received value of 'a1_notation': {a1_notation}."
            )

    @classmethod
    def from_column_row(self, column : int, row : int):
        try:
            return self(column_row_to_a1(column, row))
        except TypeError as e:
            raise TypeError(
                f"The type of argument 'column' and 'row' of class method 'A1Notation.from_column_row()' needs to be type 'int'.\n"
                f"Current received type of 'column': {type(column)}.\n"
                f"Current received type of 'row': {type(row)}."
            )
        except ValueError as e:
            raise ValueError(
                f"The value of argument 'column' and 'row' of class method 'A1Notation.from_column_row()' cannot be less than {DEFAULT_STARTING_INDEX}.\n"
                f"Current received value of 'column': {column}.\n"
                f"Current received value of 'row': {row}.\n"
            )

    @property
    def a1_notation(self):
        return self._a1_notation
    @a1_notation.setter
    def a1_notation(self, value : str):
        try:
            column_row_dict = a1_to_column_row(value)
        except TypeError as e:
            raise TypeError(
                f"The type of attribute 'a1_notation' of class 'A1Notation' needs to be type 'str'.\n"
                f"Current received setter value for attribute 'a1_notation': {type(value)}"
            )
        except ValueError as e:
            raise ValueError(
                f"The value of attribute 'a1_notation' of class 'A1Notation' needs to match the regular expression {A1_REGULAR_EXPRESSION}.\n"
                f"Current received setter value for attribute 'a1_notation': {value}."
            )

        self._a1_notation = value
        self._column = column_row_dict["column"]
        self._row = column_row_dict["row"]

    @property
    def column(self):
        return self._column
    @column.setter
    def column(self, value : int):
        try:
            self._a1_notation = column_row_to_a1(value, self._row)
        except TypeError:
            raise TypeError(
                f"The type of attribute 'column' of class 'A1Notation' needs to be type 'int'.\n"
                f"Current received setter value for attribute 'column': {type(value)}."
            )
        except ValueError:
            raise ValueError(
                f"The value of attribute 'column' of class 'A1Notation' cannot be less than {DEFAULT_STARTING_INDEX}.\n"
                f"Current received setter value for attribute 'column': {value}."
            )

        self._column = value

    @property
    def row(self):
        return self._row
    @row.setter
    def row(self, value : int):
        try:
            self._a1_notation = column_row_to_a1(self._column, value)
        except TypeError:
            raise TypeError(
                f"The type of attribute 'row' of class 'A1Notation' needs to be type 'int'.\n"
                f"Current received setter value for attribute 'row': {type(value)}."
            )
        except ValueError:
            raise ValueError(
                f"The value of attribute 'row' of class 'A1Notation' cannot be less than {DEFAULT_STARTING_INDEX}.\n"
                f"Current received setter value for attribute 'row': {value}."
            )

        self._row = value

    @overload
    def __repr__(self): ...

    def __repr__(self):
        return f"A1Notation('{self.a1_notation}')"

    @overload
    def __str__(self): ...

    def __str__(self):
        return self.a1_notation

    def __A1Notation_arithmetic(self, operation, other):
        if (isinstance(other, A1Notation)):
            try:
                other_column = other.column if operation == "addition" else -(other.column)
                other_row = other.row if operation == "addition" else -(other.row)
            except Exception as e:
                raise Exception(f"An unexpected exception occured: {e}")
        elif (type(other) is dict and all(attribute in other.keys() for attribute in ["column", "row"])):
            if (type(other["column"]) is not int or type(other["row"]) is not int):
                raise TypeError(
                    f"The type of value of keys 'column' and 'row' in the provided operand for A1Notation {operation} needs to be type 'int'.\n"
                    f"Current received type of key 'column': {type(self.column)}.\n"
                    f"Current received type of key 'row': {type(self.row)}."
                )
            try:
                other_column = other["column"] if operation == "addition" else -(other["column"])
                other_row = other["row"] if operation == "addition" else -(other["row"])
            except Exception as e:
                raise Exception(f"An unexpected exception occured: {e}")
        elif ((type(other) is list or type(other) is tuple) and len(other) >= 2):
            if (type(other[0]) is not int or type(other[1]) is not int):
                raise TypeError(
                    f"The type of values in the provided {type(other)} operand for A1Notation {operation} needs to be type 'int'.\n"
                    f"Current received type of {type(other)}[0]: {other[0]}.\n"
                    f"Current received type of {type(other)}[1]: {other[1]}.\n"
                )
            try:
                other_column = other[0] if operation == "addition" else -(other[0])
                other_row = other[1] if operation == "addition" else -(other[1])
            except Exception as e:
                raise Exception(f"An unexpected exception occured: {e}")
        else:
            raise TypeError(
                f"The operand with A1Notation {operation} needs to be type 'A1Notation', 'ColumnRowDict', 'list', or 'tuple'.\n"
                f"Current receive type of operand: {type(other)}"
            )

        return A1Notation.from_column_row(column = self.column + other_column, row = self.row + other_row)

    @overload
    def __add__(self, other): ...

    def __add__(self, other):
        return self.__A1Notation_arithmetic(operation = "addition", other = other)

    @overload
    def __sub__(self, other): ...

    def __sub__(self, other):
        return self.__A1Notation_arithmetic(operation = "subtraction", other = other)

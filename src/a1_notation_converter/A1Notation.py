from a1_notation_converter.a1_converter import *

# A1Notation class
class A1Notation:
    def __init__(self, a1_notation : str):
        try:
            columnRowDict = a1_to_column_row(a1_notation)
            self._a1_notation = a1_notation
            self._column = columnRowDict["column"]
            self._row = columnRowDict["row"]
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
            columnRowDict = a1_to_column_row(value)
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
        self._column = columnRowDict["column"]
        self._row = columnRowDict["row"]

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
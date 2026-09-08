# int_to_a1(number, starting_index = 1)
```python
def int_to_a1(number : int, starting_index : int = DEFAULT_STARTING_INDEX) -> str:
    if (not type(number) is int):   # Type check
        raise TypeError(
            f"The type of argument 'number' of function 'int_to_a1()' needs to be type 'int'.\n"
            f"Current received type of 'number': {type(number)}."
        )
    elif (not type(starting_index) is int): # Type check
        raise TypeError(
            f"The type of argument 'starting_index' of function 'int_to_a1()' needs to be type 'int'.\n"
            f"Current received type of 'starting_index': {type(starting_index)}"
        )
    elif (number < starting_index): # Value check
        raise ValueError(
            "The given value of argument 'number' of function 'int_to_a1()' cannot be less than argument 'starting_index'.\n"
            f"Current received value of 'number': {number}.\n"
            f"Current received value of 'starting_index': {starting_index}"
        )
    else:
        number += (DEFAULT_STARTING_INDEX - starting_index) # Offset by provided starting index
        if (number <= ALPHABET_AMOUNT): # Return character when less than ALPHABET_AMOUNT
            return chr(ASCII_A_INDEX + number - 1)
        else: # Return the A1 notation recursively
            remainder = ALPHABET_AMOUNT if number % ALPHABET_AMOUNT == 0 else number % ALPHABET_AMOUNT
            return int_to_a1((number - remainder) // ALPHABET_AMOUNT) + int_to_a1(remainder)
```

## Type check
Type check for argument `number` and `starting_index` to make sure they are integer, else raise a TypeError.

## Value check
Value check for argument `number`. The value of `number` cannot be less than the provided value of argument `starting_index` (default to `starting_index = 1`). The value of `starting_index` is used to represent the value of A1 notation "A" in its integer form.  
E.g.
```
# starting_index = 1
"A"  = 1
"B"  = 2
"Z"  = 26
"AA" = 27

# starting_index = 0
"A"  = 0
"B"  = 1
"Z"  = 25
"AA" = 26

# starting_index = -1
"A"  = -1
"B"  = 0
"Z"  = 24
"AA" = 25
```

## Offset by provided starting index
In a normal context, "A" would represent the 1st column, "Z" represents the 26th column, "AA" represents the 27th column. Thus, if `starting_index` is equal to `DEFAULT_STARTING_INDEX` (that is, the default `"A" = 1`), then there will be no changes for the provided value of `number` (`number += (DEFAULT_STARTING_INDEX - starting_index)` is equivalent to `number += 0`).  
However, if the value of `starting_index` is different, then we calculate how much the provided value is offset by the default value of 1. E.g. if `starting_index = 0` then we know `"A" = 0`, `"B" = 1`, `"C" = 2` and so on. The value is offset by -1 (that is, each A1 notation has its integer representation's value being 1 less than the default `"A" = 1`). Thus, we need to add back the offset value to the `number`. The equation for this is: `number += (DEFAULT_STARTING_INDEX - starting_index)` in which we add back the offset value to the `number` by calculating how much the provided value of `starting_index` is less than the value of `DEFAULT_STARTING_INDEX`.  

## Return character when less than ALPHABET_AMOUNT
In the case that the value of `number` is less than `ALPHABET_AMOUNT` (26), then we know it will just be a single character. We can directly return the character by calling the function `chr()` to convert the ASCII code (add by the value of `number`) to a string and return said string.

## Return the A1 notation recursively
When the value of `number` is more than `ALPHABET_AMOUNT` (26), then we know there will be more than one character in the A1 notation. E.g.  
```
"AA"  = 27
"ZZ"  = 702
"AAA" = 703
```
For the numeral system of A1 notation, the character in each position (starting from the rightmost) can hold up to integer representation value of 26 (starting from `"A" = 1` and end with `"Z" = 26`). And for each position, the real value is equal to `(ALPHABET_AMOUNT ** index * character_value)`, in which the `index` refers to the position starting from the rightmost (e.g. for "AZ", index 0 is "Z" and index 1 is "A"). `character_value` is the integer representation of the single character, starting with `"A" = 1`. The total value of the A1 notation is then calculated by adding all the real value of the character in each position.  
E.g.
```
"BC"

index_0 = "C"
index_1 = "B"

index_0_real_value = ALPHABET_AMOUNT ** 0 * 3 = 3
index_1_real_value = ALPHABET_AMOUNT ** 1 * 2 = 52

real_value = 52 + 3 = 55
```

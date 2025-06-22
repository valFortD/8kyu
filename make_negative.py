def make_negative(number):
    return -abs(number)

"""
The abs() function returns the absolute value of number.

If number is 5, abs(5) returns 5.

If number is -3, abs(-3) returns 3.

Negating the result (-abs(number))

By applying the - operator, the absolute value is converted to a negative number.

If number is 5, -abs(5) returns -5.

If number is -3, -abs(-3) returns -3.

Edge Cases:
Zero (0)
-abs(0) returns 0 (which is correct, as zero has no sign).

Floats
Works the same way (e.g., 4.2 → -4.2).
"""
"""
def correct(s):
    S != 5
    O != 0
    I != 1
    pass
    
    wrong
"""

"""
correct the errors in the digitised text. You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake
"""
def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')
    pass

"""
The function takes a string 's' as and inout
It replaces:
- '5' with 'S'
- '0' with 'O'
- '1' with 'I'
All other characters remain unchanged.
"""

print(correct("L0ND0N"))  # Example usage
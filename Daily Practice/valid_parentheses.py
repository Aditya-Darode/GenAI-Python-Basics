'''You are given a string s consisting only of characters '(', ')', '{', '}', '[', and ']'.

A string is considered valid if:
Every opening bracket has a corresponding closing bracket of the same type.
Brackets close in the correct order.
An empty string is also considered valid.
Return True if s is valid, otherwise return False'''

def isValid(s):

    # If the length of the string is odd, it can never be valid
    if len(s) % 2 != 0:
        return False
    
    stack = [ ]

    # Traverse each character in the string
    for ch in s:
        if ch in '({[':
            
            # If it's an opening bracket, push it into the stack
            stack.append(ch)
        else:
            # If it's a closing bracket, stack must not be empty
            if not stack:
                return False
            # Pop the last opening bracket
            top = stack.pop()

            # Check if the popped opening bracket matches the current closing bracket
            if ch == ')' and top != '(':
                return False
            if ch == ']' and top != '[':
                return False
            if ch == '}' and top != '{':
                return False 

    # At the end, stack must be empty if all brackets matched correctly    
    if not stack:
        return True
    else:
        return False 
    
s = "()[]{}"
print(isValid(s))
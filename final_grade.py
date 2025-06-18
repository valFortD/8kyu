"""
wrong

def final_grade(exam, projects):
    grade = (0, 100)
    completed_projects = 0
    
    if grade > 90 or completed_projects > 10:
        final_grade = 100
        
    if grade > 75 and completed_projects < 5:
        final_grade = 90
        
    if grade > 50 and completed_projects < 5:
        final_grade = 75
    
    else final_grade = 0
    return # final grade
"""

"""
There are several issues that need to be fixed:

The grade variable is incorrectly defined as a tuple (0, 100) instead of using the input exam parameter

The completed_projects is hardcoded to 0 instead of using the input projects parameter

The logic structure uses multiple if statements without proper elif chaining

The else statement has incorrect syntax (missing :)

The return statement is incomplete
"""

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects < 5:
        return 90
    elif exam > 50 and projects < 5:
        return 75
    else:
        return 0
    
"""
Key improvements:
Directly uses the input parameters exam and projects

Proper if-elif-else structure ensures only one condition is matched

Clear return statements for each case

More logical project thresholds (>= 5 and >= 2 instead of just < 5)
"""

print(final_grade(85, 3))  # Example usage
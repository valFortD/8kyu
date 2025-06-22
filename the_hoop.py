"""
Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message:

If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
If he doesn't get 10 hoops, return the string "Keep at it until you get it".


def hoop_count(n):
    # Good Luck!
    if n >= 10:
        print("Great, now move on to the tricks.")
    else:
        print("Keep at it until you get it.")
"""
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"
    
print(hoop_count(10))  # Example usage
print(hoop_count(5))   # Example usage

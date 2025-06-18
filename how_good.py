# Calculates the average of the class points and compares your score to it

def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    if your_points > average:
        print("You are better than average!")

"""
This function:
1. Calculates the average of the class points by summing them up and dividing by the number of points
2. Returns True if your points are higher than this average. False otherwise
"""
better_than_average([70, 80, 90], 85)  # Example usage
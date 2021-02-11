# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def get_circle_points():
    points = {"xc1":0,"yc1":0,"xc2":0,"yc2":0}
    for point in points:
        points[point] = float(input(f"Enter value of {point}: "))
    return points["xc1"], points["yc1"], points["xc2"], points["yc2"]

def calculate_distance():
    # Calculate the distance between the two circle
    xc1, yc1, xc2, yc2 = get_circle_points()
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

print('distance', calculate_distance())

# *** somewhere else in your program ***
def get_vector_points():
    points = {"xa":0,"ya":0,"xb":0,"yb":0}
    for point in points:
        points[point] = float(input(f"Enter value of {point}: "))
    return points["xa"], points["ya"], points["xb"], points["yb"]

def calculate_length():
    # calcualte the length of vector AB vector which is a vector between A and B points.
    xa, ya, xb, yb = get_vector_points()
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

print('length', calculate_length())
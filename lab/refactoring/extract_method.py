# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

def create_grade_list():
    """Generates a lits of grades for the number of students that exist"""
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    
    return grade_list

# Calculate the mean and standard deviation of the grades
def calculate_mean(grade_list):
    """Calculates the mean of the total grade list passed in"""
    sum = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum = sum + grade
    mean = sum / len(grade_list)
    return mean

def calculate_standard_deviation(grade_list):
    """Calculates the standard deviation of the total grade list passed in"""
    mean = calculate_mean(grade_list)
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd


def print_stat():
    # print out the mean and standard deviation in a nice format.
    grade_list = create_grade_list()
    print('****** Grade Statistics ******')
    print("The grades's mean is:", calculate_mean(grade_list))
    print('The population standard deviation of grades is: ', round(calculate_standard_deviation(grade_list), 3))
    print('****** END ******')

print_stat()
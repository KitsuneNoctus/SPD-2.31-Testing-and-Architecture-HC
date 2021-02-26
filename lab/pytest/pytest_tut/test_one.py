# test_one.py

def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

# def calculate_kinetic_energy(mass, velocity): 
#     """Returns kinetic energy of mass [kg] with velocity [ms]."""
#     return mass * velocity ** 2

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

# Exercise 1
# def get_average(li):
#     sum = 0
#     for num in li:
#         sum += num
#     mean = sum / len(li)
#     return mean

# def test_get_average():
#     list_of_nums = [1,2,3]
#     average = get_average(list_of_nums)
    # assert average == 2

# Exercise 2

# Exercise 3
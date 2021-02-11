
# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    """Checks if the cooking criteria satisfies well done or medium"""
    cooked_state = time * temperature * pressure * COOKED_CONSTANT
    is_well_done = cooked_state >= WELL_DONE
    is_medium = cooked_state >= MEDIUM
    if desired_state == 'well-done' and is_well_done: 
        return True
    if desired_state == 'medium' and is_medium:
        return True
    return False
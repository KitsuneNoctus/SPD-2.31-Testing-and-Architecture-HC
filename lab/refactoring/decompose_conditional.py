# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')

def make_accept_sound():
    print('made acceptance sound')

def check_if_toxin(ingredients):
    """Checks if any of the ingredients are in the list of toxic ingrediets"""
    toxic_indredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']
    return any(item in ingredients for item in toxic_indredients)

ingredients = ['sodium benzoate']
if check_if_toxin(ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
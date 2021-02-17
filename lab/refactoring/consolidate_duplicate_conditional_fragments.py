# by Kami Bigdely
# Consolidate duplicate conditional fragments

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def make_drink(drink, addons):
    mix = []
    if 'coffee' in drink:
        mix.append('coffee')
    if 'strawberry milkshake' in drink:
        mix.extend(mixer_ice_with_cream())
        mix.append('strawberry')
        
    mix.extend(addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)
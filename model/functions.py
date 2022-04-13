def update_fish(params, step, history, state, _input):
    return ('fish', state['fish'])

def update_plants(params, step, history, state, _input):
    return ('plants', state['plants'])

def update_water(params, step, history, state, _input):
    return ('water', state['water'])
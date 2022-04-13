from model.functions import *

psubs = [
    { 
        'policies': {
        },
        'states': {
            'fish': update_fish,
            'plants': update_plants,
            'water': update_water,
        }
    }
]
def move(their_history, my_history):
    return "rps"[len(my_history)%3]

move_that_beats = {
    "s":"r",
    "r":"p",
    "p":"s"
}

import random

def move(my_history, their_history):
    # beat opponents last move
    if len(their_history) > 0:
        return move_that_beats[their_history[-1]]
    # if no history, play random
    return "rps"[random.randint(0,2)]
    
def move(my_history, their_history):
    return 'rps'[len(my_history)%3]
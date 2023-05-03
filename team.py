# local version will not work because long path tensorflow

import keras
import numpy as np

move_that_beats = {
    "r":"p",
    "s":"r",
    "p":"s"
}

move_that_beats_inv = {
    "p":"r",
    "r":"s",
    "s":"p"
}

rps_val = {
    "r" : [1,0,0],
    "p" : [0,1,0],
    "s" : [0,0,1],
    " " : [0,0,0]
}
model = keras.models.load_model("updated3.h5")

def move(my_history, their_history):
    if len(their_history) > 10:
        their_history = their_history[-10:]
        my_history = my_history[-10:]

    #hist = np.array([[rps_val[x] for x in my_history.ljust(10, " ")]+[rps_val[x] for x in their_history.ljust(10, " ")]])
    hist = np.array([list(zip([rps_val[x] for x in my_history.ljust(10, " ")],[rps_val[x] for x in their_history.ljust(10, " ")]))]).reshape((1,10,6))
    their_move = 'rps'[np.argmax(model.predict(hist, verbose=0))]
    #print(their_move)
    return move_that_beats[their_move], their_move

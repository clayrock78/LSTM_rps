# train model based on opponents
import keras
import numpy as np
from opponents import opponents

move_that_beats = {
    "r":"p",
    "s":"r",
    "p":"s"
}

rps_val = {
    "r" : [1,0,0],
    "p" : [0,1,0],
    "s" : [0,0,1],
    " " : [0,0,0]
}


# the network will play games and train itself based on the results

games = 1000
epochs = 10
batch_size = 32

#model = keras.models.load_model("LSTM_RPS_bigdataset.h5")
for opponent in opponents:
    pass
    # isnt working yet
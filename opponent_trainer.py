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

model = keras.models.load_model("LSTM_RPS_bigdataset.h5")
for opponent in opponents:
    for i in range(games):
        print(i)
        # play a game
        my_history = ""
        their_history = ""
        for j in range(100):
            # get my move
            hist = np.array([[rps_val[x] for x in my_history.ljust(10, " ")]+[rps_val[x] for x in their_history.ljust(10, " ")]])
            my_move = 'rps'[np.argmax(model.predict(hist))]
            # get their move
            their_move = opponent(their_history, my_history)
            # add moves to history
            my_history += my_move
            their_history += their_move
            # get result
            if my_move == their_move:
                result = 0
            elif move_that_beats[my_move] == their_move:
                result = -1
            else:
                result = 1
            # add result to history
            #my_history += str(result)
            #their_history += str(-result)
        # train model
        for j in range(epochs):
            model.fit(np.array([[rps_val[x] for x in my_history[i:i+10]]+[rps_val[x] for x in their_history[i:i+10]] for i in range(0, len(my_history), 10)]), np.array([[rps_val[x] for x in my_history[i+10]] for i in range(0, len(my_history), 10)]), batch_size=batch_size, epochs=1)
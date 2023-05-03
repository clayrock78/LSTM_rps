# load Flask 
import flask
import keras
import numpy as np
app = flask.Flask(__name__)

model = keras.models.load_model("updated.h5")

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


# define a predict function as an endpoint 
@app.route("/predict", methods=["GET"])
def predict():
    # get the request parameters
    params = flask.request.json
    their_history = params["theirs"]
    my_history = params["mine"]
    if len(their_history) > 10:
        their_history = their_history[-10:]
        my_history = my_history[-10:]
    
    hist = np.array([list(zip([rps_val[x] for x in my_history.ljust(10, " ")],[rps_val[x] for x in their_history.ljust(10, " ")]))]).reshape((1,10,6))
    #hist = np.array([[rps_val[x] for x in my_history.ljust(5, " ")]+[rps_val[x] for x in their_history.ljust(5, " ")]])
    their_move = 'rps'[np.argmax(model.predict(hist, verbose=0))]
    return move_that_beats[their_move]



# start the flask app, allow remote connections
app.run(host='0.0.0.0', debug=True)
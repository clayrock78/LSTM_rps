import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from processor import load_data

import numpy as np


def get_model():
    inputs = layers.Input(shape=(10,6))
    hidden = layers.Dense(256, activation="tanh")(inputs)
    lstm = layers.LSTM(128, activation="tanh")(hidden)
    a = layers.Dense(64, activation="tanh")(lstm)
    a = layers.Dense(32, activation="tanh")(a)
    a = layers.Dense(16, activation="tanh")(a)
    #a = layers.Dense(100, activation="relu")(a)
    #a = layers.Dense(50, activation="relu")(a)

    outputs = layers.Dense(3)(a)
    
    model = models.Model(inputs, outputs)

    lr_schedule = optimizers.schedules.ExponentialDecay(
        initial_learning_rate=1e-2,
        decay_steps=10000,
        decay_rate=0.8
    )
    #optimizer = keras.optimizers.SGD(learning_rate=lr_schedule)
    opt = optimizers.Adam(learning_rate=lr_schedule)
    model.compile(optimizer='adam', loss='bce', metrics=["accuracy"])

    return model

tf.keras.backend.clear_session()
model = get_model()
#model = models.load_model("updated3.h5")
model.summary()
for i in range(10):
    X, Y = load_data(10)
    history = model.fit(X, Y, epochs=100, validation_split=0.2, verbose=1)
    model.save("updated_huge.h5")


    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig("test.png")
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig("test2.png")
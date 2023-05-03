

# QDEEP DONT WORK


import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Configuration paramaters for the whole setup
seed = 42
gamma = 0.99  # Discount factor for past rewards
epsilon = 1.0  # Epsilon greedy parameter
epsilon_min = 0.1  # Minimum epsilon greedy parameter
epsilon_max = 1.0  # Maximum epsilon greedy parameter
epsilon_interval = (
    epsilon_max - epsilon_min
)  # Rate at which to reduce chance of random action being taken
batch_size = 32  # Size of batch taken from replay buffer
max_steps_per_episode = 10000


"""
## Implement the Deep Q-Network

This network learns an approximation of the Q-table, which is a mapping between
the states and actions that an agent will take. For every state we'll have four
actions, that can be taken. The environment provides the state, and the action
is chosen by selecting the larger of the four Q-values predicted in the output layer.

"""

num_actions = 3


def create_q_model():
    # Network defined by the Deepmind paper
    inputs = layers.Input(
        shape=(
            10,
            2,
            3
        )
    )

    # Convolutions on the frames on the screen
    layer1 = layers.Dense(16, activation="relu")(inputs)
    layer2 = layers.Dense(32, activation="relu")(layer1)
    layer3 = layers.Dense(16, activation="relu")(layer2)

    layer4 = layers.Flatten()(layer3)

    #layer5 = layers.Dense(512, activation="relu")(layer4)
    action = layers.Dense(num_actions, activation="linear")(layer4)

    return keras.Model(inputs=inputs, outputs=action)


# The first model makes the predictions for Q-values which are used to
# make a action.
model = create_q_model()
# Build a target model for the prediction of future rewards.
# The weights of a target model get updated every 10000 steps thus when the
# loss between the Q-values is calculated the target Q-value is stable.
model_target = create_q_model()


"""
## Train
"""
# In the Deepmind paper they use RMSProp however then Adam optimizer
# improves training time
optimizer = keras.optimizers.Adam(learning_rate=0.001, clipnorm=1.0)

# Experience replay buffers
action_history = []
state_history = []
state_next_history = []
rewards_history = []
done_history = []
episode_reward_history = []
running_reward = 0
episode_count = 0
frame_count = 0
# Number of frames to take random action and observe output
epsilon_random_frames = 500
# Number of frames for exploration
epsilon_greedy_frames = 1000
# Maximum replay length
# Note: The Deepmind paper suggests 1000000 however this causes memory issues
max_memory_length = 100000
# Train the model after 4 actions
update_after_actions = 4
# How often to update the target network
update_target_network = 50
# Using huber loss for stability
loss_function = keras.losses.Huber()
loss_function = keras.losses.BinaryCrossentropy()

TURNS_PER_EPISODE = 100

action_as_rps = {
    0: 'r',
    1: 'p',
    2: 's'
}

def opponent(my_history, their_history):
    return 'r'
    # play the move that beats opponent last move
    if len(their_history) == 0:
        return 'r'
    else:
        return {'r': 'p', 'p': 's', 's': 'r'}[their_history[-1]]
    
move_that_beats = {
    'r': 'p',
    'p': 's',
    's': 'r'
}

move_as_lst = {
    'r': [1, 0, 0],
    'p': [0, 1, 0],
    's': [0, 0, 1]
}

turns_played = 0

while True:  # Run until solved
    #state = np.array(env.reset())
    # ten frames of 2x3
    state = np.full((10,2,3),[[0, 0, 0], [0,0,0]])
    episode_reward = 0

    my_history = ""
    their_history = ""

    for turn in range(TURNS_PER_EPISODE):
        # env.render(); Adding this line would show the attempts
        # of the agent in a pop up window.
        turns_played += 1 
        # Use epsilon-greedy for exploration
        if turn < epsilon_random_frames or epsilon > np.random.rand(1)[0]:
            # Take random action
            action = np.random.choice(num_actions)
        else:
            # Predict action Q-values
            # From environment state
            state_tensor = tf.convert_to_tensor(state)
            state_tensor = tf.expand_dims(state_tensor, 0)
            action_probs = model(state_tensor, training=False)
            # Take best action
            action = tf.argmax(action_probs[0]).numpy()

        # Decay probability of taking random action
        epsilon -= epsilon_interval / epsilon_greedy_frames
        epsilon = max(epsilon, epsilon_min)

        # Apply the sampled action in our environment
        move = action_as_rps[action]
        #rint(move)
        my_history += move
        their_move = opponent(their_history, my_history)
        their_history += their_move
        #print(move, their_move)
        #print(f"needed {move_that_beats[their_move]}, got {move}")
        reward = 1 if move_that_beats[their_move] == move else 0
        state_next = np.roll(state.copy(),1)
        state_next[-1][1] = move_as_lst[move]
        state_next[-1][0] = move_as_lst[their_move]
        done = turn == TURNS_PER_EPISODE
        #state_next, reward, done, _ = env.step(action)
        #state_next = np.array(state_next)

        episode_reward += reward

        # Save actions and states in replay buffer
        action_history.append(action)
        state_history.append(state)
        state_next_history.append(state_next)
        done_history.append(done)
        rewards_history.append(reward)
        state = state_next

        # Update every fourth frame and once batch size is over 32
        if turn % update_after_actions == 0 and len(done_history) > batch_size:

            # Get indices of samples for replay buffers
            indices = np.random.choice(range(len(done_history)), size=batch_size)

            # Using list comprehension to sample from replay buffer
            state_sample = np.array([state_history[i] for i in indices])
            state_next_sample = np.array([state_next_history[i] for i in indices])
            rewards_sample = [rewards_history[i] for i in indices]
            action_sample = [action_history[i] for i in indices]
            done_sample = tf.convert_to_tensor(
                [float(done_history[i]) for i in indices]
            )

            # Build the updated Q-values for the sampled future states
            # Use the target model for stability
            future_rewards = model_target.predict(state_next_sample)
            # Q value = reward + discount factor * expected future reward
            updated_q_values = rewards_sample + gamma * tf.reduce_max(
                future_rewards, axis=1
            )

            # If final frame set the last value to -1
            updated_q_values = updated_q_values * (1 - done_sample) - done_sample

            # Create a mask so we only calculate loss on the updated Q-values
            masks = tf.one_hot(action_sample, num_actions)

            with tf.GradientTape() as tape:
                # Train the model on the states and updated Q-values
                q_values = model(state_sample)

                # Apply the masks to the Q-values to get the Q-value for action taken
                q_action = tf.reduce_sum(tf.multiply(q_values, masks), axis=1)
                # Calculate loss between new Q-value and old Q-value
                loss = loss_function(updated_q_values, q_action)

            # Backpropagation
            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

        if turns_played % update_target_network == 0:
            # update the the target network with new weights
            model_target.set_weights(model.get_weights())
            # Log details
            template = "running reward: {:.2f} at episode {}, frame count {}"
            print(template.format(running_reward, episode_count, turn))

        # Limit the state and reward history
        if len(rewards_history) > max_memory_length:
            del rewards_history[:1]
            del state_history[:1]
            del state_next_history[:1]
            del action_history[:1]
            del done_history[:1]

        if done:
            break

    # Update running reward to check condition for solving
    episode_reward_history.append(episode_reward)
    if len(episode_reward_history) > 100:
        del episode_reward_history[:1]
    running_reward = np.mean(episode_reward_history)

    episode_count += 1

    if running_reward == TURNS_PER_EPISODE:  # Condition to consider the task solved
        print("Solved at episode {}!".format(episode_count))
        break
    
    print("GG BOYS")
    print(my_history)
    print(their_history)
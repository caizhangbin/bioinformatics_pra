#
# 2024 Compute Ontario Summer School
# Artificial Neural Networks
# Day 2
# Erik Spence
#
# This file, model3.py, contains a routine to generate the model for
# our MNIST Keras example, using updated activation functions.
#

#######################################################################


"""
model3.py contains a routine which generates the model for the
class' MNIST Keras example, using updated activation functions.

"""


#######################################################################


import tensorflow.keras.models as km
import tensorflow.keras.layers as kl


#######################################################################


def get_model(numnodes, input_size = 784, output_size = 10):

    """
    This function returns a simple Keras model, consisting of a
    re-implementation of the second_network.py neural network, with
    numnodes in the hidden layer, using updated activation functions.

    Inputs:
    - numnodes: int, the number of nodes in the hidden layer.

    - intput_size: int, the size of the input data, default = 784.

    - output_size: int, the number of nodes in the output layer,
      default = 10.

    Output: the constructed Keras model.

    """

    # Initialize the model.
    model = km.Sequential()

    # Add a hidden fully-connected layer.
    model.add(kl.Dense(numnodes, name = 'hidden',
                       input_dim = input_size,
                       activation = 'tanh'))

    # Add the output layer.
    model.add(kl.Dense(output_size, name = 'output',
                       activation = 'softmax'))

    # Return the model.
    return model


#######################################################################

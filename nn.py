import json
import numpy as np


data = json.load(open("layer.json", "r"))


def set_matrix(layer):
    # creating matrix for the layer
    # set empty matrix
    matrix = np.zeros((layer["size_out"], layer["size_in"]))
    # fill matrix with given weights
    for key, weights in layer["weights"].items():
        key = int(key)
        for k, w in weights.items():
            k = int(k)
            w = float(w)
            matrix[k - 1][key - 1] = w
    return matrix


def calculate_matrix(matrix, input):
    output = []
    # loop through every row of the matrix
    for row in matrix:
        # sum
        s = 0
        # save index of weight
        index = 0
        # loop through every matrix
        for weight in row:
            # add input * weight to sum
            s += input[index] * weight
            # increase index
            index += 1
        # add sum to output
        output.append(s)
    # return output
    return output


# set default input
i = np.array([1, 1, 1, 1, 1])
# loop through every layer of the matrix
for key, layer in data.items():
    # create a matrix
    matrix = set_matrix(layer)
    # calculate matrix
    i = calculate_matrix(matrix, i)
print(i)

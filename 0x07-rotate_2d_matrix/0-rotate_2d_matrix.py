#!/usr/bin/python3
""" Rotating diagonal matrix 90 degrees clockwise. """


def transpose(matrix):
    """ Transpose a matrix. """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse(matrix):
    """ Reverse a matrix. """
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]


def rotate_2d_matrix(matrix):
    """ Rotate a 2D matrix 90 degrees clockwise. """
    transpose(matrix)
    reverse(matrix)

#!/usr/bin/python3
""" Rotate 2D Matrix Module """


def rotate_2d_matrix(matrix) -> None:
    """
    Rotate 2D Matrix 90 degrees clockwise

    Args:
        matrix (2D): 2 dimensions & not empty
    """
    # First transpose the matrix
    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    # Then arrange the matrix as required
    for x in range(len(matrix)):
        matrix[x].reverse()

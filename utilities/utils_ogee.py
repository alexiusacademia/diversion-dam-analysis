from utilities.geometry import *


def reaction_p10(f_toe, f_heel, b, x1):
    # Function to solve for reaction at point 10
    # x1 = Distance from point 10 to 11
    # x2 = Distance from point 9 to 11
    if f_heel > f_toe:
        return (f_heel - f_toe) * x1 / b + f_toe
    elif f_heel < f_toe:
        return (f_toe - f_heel) * (b - x1) / b + f_heel
    else:
        return f_heel


def reaction_p9(f_toe, f_heel, b, x2):
    # Function to solve for reaction at point 9
    # x1 = Distance from point 10 to 11
    # x2 = Distance from point 9 to 11
    if f_heel > f_toe:
        return (f_heel - f_toe) * x2 / b + f_toe
    elif f_heel < f_toe:
        return (f_toe - f_heel) * (b - x2) / b + f_heel
    else:
        return f_heel


def centroid_trapezoid_y(a, b, h):
    """
    Centroid of the trapezoid from the top.
    :param a: Smaller base.
    :param b: Larger base.
    :param h: Trapezoid height.
    :return: Centroid in the y direction.
    """
    return (1.0 / 3.0) * (a ** 2 + a * b + b ** 2) / (a + b)


def centroid_trapezoid_x(a, b, h):
    """
    Centroid of the trapezoid from the left.
    :param a: Smaller base.
    :param b: Larger base.
    :param h: Trapezoid height.
    :return: Centroid in the x direction.
    """
    return (h / 3.0) * ((2 * a + b) / (a + b))


def flow_type_19(dist, ho):
    dho = 0.0
    yho = 0.0
    dho = dist / ho


def get_co(p_h):
    ph = [
        0.0, 0.025, 0.05,
        0.075, 0.10, 0.125,
        0.15, 0.175, 0.20,
        0.225, 0.25, 0.275,
        0.3, 0.325, 0.35,
        0.375, 0.4, 0.425,
        0.45, 0.475, 0.5,
        0.55, 0.6, 0.65,
        0.7, 0.75, 0.8,
        0.85, 0.9, 0.95,
        1.0, 1.1, 1.2,
        1.3, 1.4, 1.5,
        1.6, 1.8, 2.0,
        2.2, 2.4, 2.6,
        2.8, 3.0
    ]

    co = [
        3.087, 3.177, 3.257,
        3.331, 3.391, 3.441,
        3.487, 3.527, 3.561,
        3.599, 3.635, 3.663,
        3.683, 3.707, 3.725,
        3.743, 3.759, 3.771,
        3.781, 3.79, 3.798,
        3.813, 3.827, 3.841,
        3.85, 3.859, 3.867,
        3.873, 3.878, 3.883,
        3.887, 3.897, 3.903,
        3.908, 3.913, 3.917,
        3.921, 3.928, 3.935,
        3.94, 3.944, 3.946,
        3.948, 3.949
    ]

    return interpolate2(p_h, co, ph)


def percent_correction(hd_ho, hdd_ho):
    # Graph numerics for hd/H
    hd_h = [
        [0.0, 0.021, 0.039, 0.061, 0.102, 0.185, 0.3],
        [0, 0.02, 0.037, 0.06, 0.094, 0.161, 0.232, 0.32],
        [0, 0.019, 0.036, 0.058, 0.089, 0.145, 0.208, 0.27, 0.32],
        [0, 0.019, 0.035, 0.056, 0.086, 0.135, 0.185, 0.225, 0.275, 0.32],
        [0, 0.018, 0.034, 0.053, 0.081, 0.123, 0.164, 0.203, 0.232, 0.266, 0.32],
        [0, 0.017, 0.033, 0.052, 0.078, 0.113, 0.151, 0.187, 0.209, 0.23, 0.275, 0.32],
        [0, 0.016, 0.032, 0.052, 0.076, 0.108, 0.14, 0.172, 0.192, 0.211, 0.246, 0.278, 0.32],
        [0, 0.015, 0.031, 0.05, 0.072, 0.1, 0.127, 0.157, 0.174, 0.191, 0.215, 0.243, 0.271, 0.32]

    ]

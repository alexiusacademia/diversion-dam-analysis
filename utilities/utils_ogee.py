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
        [0, 0.015, 0.031, 0.05, 0.072, 0.1, 0.127, 0.157, 0.174, 0.191, 0.215, 0.243, 0.271, 0.32],
        [0, 0.015, 0.031, 0.049, 0.069, 0.094, 0.123, 0.148, 0.16, 0.177, 0.197, 0.219, 0.246, 0.28, 0.328],
        [0, 0.015, 0.03, 0.049, 0.068, 0.091, 0.118, 0.141, 0.152, 0.165, 0.183, 0.205, 0.228, 0.255, 0.293, 0.336],
        [0, 0.015, 0.03, 0.048, 0.066, 0.086, 0.113, 0.134, 0.147, 0.16, 0.175, 0.196, 0.214, 0.241, 0.271, 0.306, 0.346],
        [0, 0.015, 0.03, 0.047, 0.064, 0.083, 0.11, 0.131, 0.142, 0.164, 0.171, 0.188, 0.205, 0.23, 0.257, 0.29, 0.316, 0.356],
        [0, 0.014, 0.029, 0.045, 0.064, 0.081, 0.106, 0.126, 0.137, 0.148, 0.163, 0.179,
         0.196, 0.218, 0.243, 0.268, 0.289, 0.313, 0.378],
        [0, 0.014, 0.029, 0.045, 0.063, 0.079, 0.104, 0.123, 0.133, 0.145, 0.159, 0.174,
         0.189, 0.21, 0.231, 0.255, 0.274, 0.292, 0.332, 0.4],
        [0, 0.014, 0.029, 0.044, 0.063, 0.079, 0.103, 0.121, 0.131, 0.142, 0.156, 0.169,
         0.185, 0.204, 0.226, 0.25, 0.267, 0.285, 0.316, 0.365, 0.403],
        [0, 0.014, 0.029, 0.044, 0.062, 0.08, 0.102, 0.12, 0.129, 0.14, 0.153, 0.167,
         0.181, 0.199, 0.218, 0.237, 0.254, 0.27, 0.298, 0.333, 0.353, 0.408],
        [0, 0.014, 0.029, 0.043, 0.062, 0.081, 0.101, 0.119, 0.128, 0.139, 0.151, 0.165,
         0.178, 0.197, 0.213, 0.232, 0.249, 0.263, 0.288, 0.316, 0.336, 0.372, 0.429],
        [0, 0.014, 0.029, 0.043, 0.062, 0.081, 0.101, 0.12, 0.129, 0.139, 0.152, 0.164,
         0.176, 0.194, 0.211, 0.228, 0.244, 0.258, 0.283, 0.306, 0.323, 0.355, 0.396,
         0.449],
        [0, 0.013, 0.029, 0.043, 0.061, 0.081, 0.101, 0.12, 0.128, 0.139, 0.153, 0.165,
         0.177, 0.193, 0.21, 0.225, 0.239, 0.254, 0.276, 0.3, 0.314, 0.343, 0.377,
         0.416, 0.481],
        [0, 0.013, 0.029, 0.043, 0.061, 0.081, 0.101, 0.12, 0.129, 0.14, 0.153, 0.166,
         0.177, 0.194, 0.209, 0.225, 0.237, 0.252, 0.274, 0.294, 0.309, 0.335, 0.365,
         0.4, 0.455, 0.513],
        [0, 0.013, 0.029, 0.043, 0.061, 0.082, 0.101, 0.12, 0.129, 0.14, 0.154, 0.166,
         0.178, 0.194, 0.208, 0.224, 0.237, 0.251, 0.271, 0.29, 0.304, 0.328, 0.355,
         0.387, 0.433, 0.478, 0.537],
        [0, 0.013, 0.029, 0.042, 0.061, 0.082, 0.102, 0.121, 0.13, 0.141, 0.156, 0.167,
         0.179, 0.195, 0.208, 0.224, 0.237, 0.25, 0.268, 0.288, 0.299, 0.326, 0.352,
         0.375, 0.414, 0.458, 0.499, 0.567],
        [0, 0.013, 0.03, 0.042, 0.062, 0.083, 0.105, 0.122, 0.131, 0.143, 0.157, 0.168,
         0.18, 0.196, 0.21, 0.224, 0.237, 0.25, 0.268, 0.289, 0.301, 0.326, 0.351,
         0.374, 0.41, 0.447, 0.482, 0.527, 0.597],
        [0, 0.013, 0.03, 0.042, 0.063, 0.084, 0.106, 0.123, 0.133, 0.145, 0.157, 0.168,
         0.18, 0.197, 0.21, 0.224, 0.237, 0.25, 0.268, 0.289, 0.304, 0.328, 0.352,
         0.375, 0.41, 0.443, 0.473, 0.513, 0.561],
        [0, 0.013, 0.03, 0.042, 0.064, 0.084, 0.107, 0.123, 0.134, 0.145, 0.158, 0.169,
         0.181, 0.197, 0.211, 0.225, 0.238, 0.25, 0.27, 0.289, 0.303, 0.33, 0.535,
         0.375, 0.409, 0.443, 0.473, 0.507, 0.545],
        [0, 0.013, 0.03, 0.043, 0.064, 0.085, 0.108, 0.124, 0.134, 0.144, 0.158, 0.17,
         0.182, 0.198, 0.213, 0.227, 0.239, 0.25, 0.27, 0.289, 0.305, 0.333, 0.355,
         0.377, 0.412, 0.446, 0.472, 0.503, 0.534],
        [0, 0.014, 0.031, 0.044, 0.065, 0.086, 0.109, 0.124, 0.135, 0.145, 0.159, 0.171,
         0.182, 0.198, 0.214, 0.229, 0.24, 0.251, 0.271, 0.291, 0.307, 0.335, 0.358,
         0.381, 0.415, 0.448, 0.472, 0.5, 0.53],
        [0, 0.015, 0.031, 0.044, 0.065, 0.087, 0.11, 0.125, 0.136, 0.146, 0.16, 0.172,
         0.183, 0.199, 0.215, 0.231, 0.243, 0.254, 0.274, 0.293, 0.31, 0.339, 0.362,
         0.385, 0.418, 0.45, 0.473, 0.501, 0.53],
        [0, 0.016, 0.031, 0.044, 0.065, 0.088, 0.111, 0.127, 0.137, 0.147, 0.161, 0.173,
         0.184, 0.2, 0.217, 0.233, 0.245, 0.256, 0.275, 0.294, 0.312, 0.342, 0.366,
         0.39, 0.422, 0.455, 0.479, 0.507, 0.536],
        [0, 0.016, 0.032, 0.045, 0.066, 0.09, 0.113, 0.129, 0.14, 0.15, 0.164, 0.175,
         0.187, 0.202, 0.219, 0.236, 0.249, 0.262, 0.281, 0.3, 0.318, 0.35, 0.377,
         0.405, 0.436, 0.47, 0.497, 0.529, 0.562],
        [0, 0.016, 0.033, 0.047, 0.068, 0.091, 0.114, 0.13, 0.141, 0.152, 0.166, 0.177,
         0.189, 0.204, 0.222, 0.24, 0.254, 0.268, 0.288, 0.307, 0.326, 0.358, 0.389,
         0.419, 0.453, 0.489, 0.517, 0.553, 0.59],
        [0, 0.016, 0.033, 0.05, 0.07, 0.094, 0.117, 0.134, 0.145, 0.155, 0.169, 0.181,
         0.194, 0.21, 0.229, 0.248, 0.266, 0.284, 0.305, 0.325, 0.347, 0.381, 0.415,
         0.452, 0.493, 0.535, 0.569, 0.612, 0.66],
        [0, 0.016, 0.033, 0.051, 0.072, 0.097, 0.121, 0.137, 0.148, 0.159, 0.173,
         0.186, 0.198, 0.215, 0.234, 0.253, 0.275, 0.297, 0.321, 0.345, 0.366,
         0.403, 0.44, 0.48, 0.525, 0.575, 0.615, 0.661, 0.711],
        [0, 0.016, 0.034, 0.052, 0.074, 0.1, 0.125, 0.141, 0.152, 0.163, 0.177,
         0.189, 0.202, 0.218, 0.239, 0.26, 0.284, 0.307, 0.334, 0.36, 0.382, 0.42,
         0.462, 0.502, 0.553, 0.605, 0.647, 0.695, 0.748],
        [0, 0.016, 0.035, 0.054, 0.077, 0.103, 0.128, 0.143, 0.154, 0.164, 0.178,
         0.191, 0.203, 0.22, 0.242, 0.263, 0.289, 0.314, 0.343, 0.371, 0.394,
         0.433, 0.476, 0.52, 0.573, 0.626, 0.668, 0.718, 0.771],
        [0, 0.016, 0.036, 0.055, 0.078, 0.105, 0.131, 0.147, 0.157, 0.167, 0.18,
         0.193, 0.204, 0.22, 0.243, 0.266, 0.293, 0.321, 0.353, 0.384, 0.405,
         0.443, 0.487, 0.532, 0.587, 0.643, 0.683, 0.735, 0.788],
        [0, 0.016, 0.037, 0.056, 0.08, 0.107, 0.134, 0.15, 0.159, 0.169, 0.181,
         0.193, 0.205, 0.221, 0.245, 0.267, 0.295, 0.325, 0.361, 0.393, 0.413,
         0.448, 0.491, 0.539, 0.594, 0.65, 0.692, 0.746, 0.798],
        [0, 0.016, 0.037, 0.057, 0.081, 0.11, 0.137, 0.153, 0.162, 0.171, 0.182,
         0.195, 0.207, 0.223, 0.245, 0.268, 0.297, 0.328, 0.365, 0.399, 0.417,
         0.45, 0.496, 0.542, 0.597, 0.652, 0.695, 0.747, 0.8],
        [0, 0.016, 0.038, 0.058, 0.082, 0.111, 0.139, 0.155, 0.163, 0.172, 0.183,
         0.195, 0.207, 0.223, 0.246, 0.268, 0.299, 0.331, 0.366, 0.401, 0.419,
         0.45, 0.497, 0.542, 0.597, 0.652, 0.696, 0.747, 0.8],
        [0, 0.016, 0.038, 0.059, 0.082, 0.113, 0.14, 0.156, 0.164, 0.172, 0.183,
         0.195, 0.208, 0.224, 0.246, 0.268, 0.301, 0.333, 0.368, 0.403, 0.42,
         0.45, 0.497, 0.542, 0.597, 0.652, 0.696, 0.747, 0.8],
        [0, 0.016, 0.038, 0.06, 0.085, 0.117, 0.14, 0.159, 0.167, 0.175, 0.185,
         0.197, 0.209, 0.225, 0.246, 0.268, 0.301, 0.333, 0.369, 0.405, 0.423,
         0.454, 0.498, 0.542, 0.597, 0.652, 0.696, 0.747, 0.8]
    ]

    percentage = [
        100, 80, 60, 50, 40, 30, 23, 20, 18.5, 17,
        15, 13.5, 12, 10, 9, 8, 7, 6, 5, 4, 3.635, 3, 2.5,
        2, 1.5, 1, 0.709, 0.362, 0
    ]

    hd_d = [
        1.0, 1.028, 1.051, 1.073, 1.104, 1.132, 1.159, 1.196, 1.223, 1.251,
        1.274, 1.297, 1.337, 1.377, 1.4, 1.44, 1.469, 1.499, 1.529, 1.558,
        1.6, 1.65, 1.702, 1.75, 1.8, 1.85, 1.9, 1.95, 2.0, 2.1, 2.2, 2.4,
        2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.8
    ]

    z = 6

    if hd_ho == 0:
        PC = 100
    if hdd_ho < 1:
        PC = 0

    for a in range(40-1):
        if (hdd_ho > hd_d[a]) and (hdd_ho < hd_d[a + 1]):
            for i in range(z-1):
                if (hd_h[a, i] < hd_ho) and (hd_h[a, i+1] > hd_ho):
                    hd_ho_11 = hd_h[a, i]
                    hd_ho_12 = hd_h[a, i+1]
                    p_11 = percentage[i]
                    p_12 = percentage[i + 1]
                    x = interpolate(p_11, p_12, hd_ho_11, hd_ho, hd_ho_12)
                    break

            for j in range(z-1):
                if (hd_h[a+1, i] < hd_ho) and (hd_h[a+1, i + 1] > hd_ho):
                    hd_ho_21 = hd_h[a + 1, i]
                    hd_ho_22 = hd_h[a + 1, i + 1]
                    p_21 = percentage[i]
                    p_22 = percentage[i + 1]
                    y = interpolate(p_21, p_22, hd_ho_21, hd_ho, hd_ho_22)
                    break
            correction = interpolate(x, y, hd_d[a], hdd_ho, hd_d[a + 1])
        if a > 21:
            z = 28
        else:
            z = z + 1

    return correction

def get_co(p_h):
    ph = [
        0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225,
        0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45,
        0.475, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9,
        0.95, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2, 2.2, 2.4,
        2.6, 2.8, 3
    ]

    co = [
        3.087, 3.177, 3.257, 3.331, 3.391, 3.441, 3.487, 3.527, 3.561,
        3.599, 3.635, 3.663, 3.683, 3.707, 3.725, 3.743, 3.759, 3.771,
        3.781, 3.79, 3.798, 3.813, 3.827, 3.841, 3.85, 3.859, 3.867,
        3.873, 3.878, 3.883, 3.887, 3.897, 3.903, 3.908, 3.913, 3.917,
        3.921, 3.928, 3.935, 3.94, 3.944, 3.946, 3.948, 3.949
    ]

    for i in range(1, len(co)):
        if ph[i] == p_h:
            return co[i]
        elif ph[i] > p_h:
            return interpolate2(p_h, co, ph)
        else:
            pass

def interpolate(x1, x3, y1, y2, y3):
    """
    Linear interpolation
    :param x1:
    :param x3:
    :param y1:
    :param y2:
    :param y3:
    :return:
    """
    return (y2 - y3) / (y1 - y3) * (x1 - x3) + x3;


def interpolate2(y2, x, y):
    """
    Search and interpolate.
    :param y2: Given y
    :param x: List of x
    :param y: List of y
    :return:
    """
    for i in range(len(x) - 1):
        if (y2 >= y[i]) and (y2 <= y[i+1]):
            return interpolate(x[i], x[i+1], y[i], y2, y[i+1])

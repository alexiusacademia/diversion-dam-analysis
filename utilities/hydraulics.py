GRAVITY = 9.81


def get_velocity_head(v):
    """
    Calculates the velocity head.
    :param v: Velocity
    :return: ha - Velocity head.
    """
    return pow(v, 2) / (2 * GRAVITY)

NEW = 0
OPEN = 1
CLOSED = 2
MAX_X = 3000  # in mm
MAX_Y = 2000  # in mm
STEP = 50  # in mm, filling with squares of 5cm side
MAX_J = MAX_X // STEP
MAX_I = MAX_Y // STEP
N = MAX_I * (MAX_J + 1) + MAX_J
DIRECT_TRANSITION = 50.0
DIAGONAL_TRANSITION = 100.0
OBSTACLE_TRANSITION = 10000

STATE_CLEAR = 0
STATE_OBSTACLE = 1

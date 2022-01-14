OUTPUT_FILE = 'choreography.txt'


mandatory_positions = ['StandInit', 'Hello', 'Stand', 'Wipe-forehead', 'StandZero', 'Sit','SitRelax', 'Crouch']


BODY_POSITIONS = ['sitting', 'standing', 'crouch']
SITTING = BODY_POSITIONS[0]
STANDING = BODY_POSITIONS[1]
CROUCH = BODY_POSITIONS[2]

PRECONDITIONS = 0
POSTCONDITIONS = 1

LEGS = 2

TYPES_CONTROL = ['time', 'speed', 'legs', 'body']
TIME = TYPES_CONTROL[0]
SPEED = TYPES_CONTROL[1]
LEGS_CONTROL = TYPES_CONTROL[2]
BODY_CONTROL = TYPES_CONTROL[3]

TYPE_CONTROL = 3

MIN_TIME = 4
MAX_SPEED = 5


MOVEMENTS_DONE = 0
MIN_MOVEMENTS = 0
BARS_EXPLOITED = 1
BARS_TO_BE_EXPLOITED = 1
BODY = 2
BODY_POSITION = 0
LEGS_POSITION = 1

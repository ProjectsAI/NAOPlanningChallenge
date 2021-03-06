from constants import *

NON_MANDATORY_MOVEMENTS = {
    'tai-chi-chuan' :   [ [STANDING],           [STANDING],         False,  [TIME],                 7.8 ],
    'vanity' :          [ [STANDING],           [STANDING],         False,  [TIME],                 3.5 ],
    'clip-clap' :       [ [SITTING, STANDING],  [SITTING, STANDING],None,   [TIME, BODY_CONTROL],   1.5 ],
    'fly' :             [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'plie' :            [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'pray' :            [ [SITTING, STANDING],  [SITTING, STANDING],None,   [TIME, BODY_CONTROL],   1.5 ],
    'fever' :           [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'rush' :            [ [SITTING, STANDING],  [SITTING, STANDING],None,   [TIME, BODY_CONTROL],   1.5 ],
    'single-snap' :     [ [STANDING],           [STANDING],         False,  [TIME, BODY_CONTROL],   1.5 ],
    'snaps' :           [ [STANDING],           [STANDING],         False,  [TIME],                 3.5 ],
    'swing' :           [ [STANDING],           [STANDING],         False,  [TIME],                 3.5 ],
    'vanity' :          [ [STANDING],           [STANDING],         False,  [TIME],                 3.5 ],
    'arms-opening' :    [ [SITTING, STANDING],  [SITTING, STANDING],None,   [TIME],                 1.5 ],
    'birthday-dance-no-sound' : [ [STANDING],   [STANDING],         False,  [TIME],                 9.4 ],
    'sing-with-me' :    [ [STANDING],           [STANDING],         False,  [TIME],                 9.4 ],
    'sprinkler' :       [ [STANDING],           [STANDING],         False,  [TIME],                 9.4 ],
    'workout' :         [ [STANDING],           [STANDING],         False,  [TIME],                 9.4 ],
    'arms-dance' :      [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'dance-move' :      [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'disco'  :          [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'macarena' :        [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'the-robot' :       [ [STANDING],           [STANDING],         False,  [TIME],                 3.4 ],
    'diagonal-left' :   [ [STANDING],           [STANDING],         True,   [LEGS_CONTROL],         3.7 ],
    'diagonal-right' :  [ [STANDING],           [STANDING],         True,   [LEGS_CONTROL],         3.7 ],
    'double-movement' : [ [SITTING, STANDING],  [SITTING, STANDING],None,   [TIME],                 1.5 ],
    'move-forward' :    [ [STANDING],           [STANDING],         True,   [LEGS_CONTROL],         3.7 ],
    'move-backward' :   [ [STANDING],           [STANDING],         True,   [LEGS_CONTROL],         3.7 ],
    'right-arm' :       [ [SITTING, STANDING],  [SITTING, STANDING],None,   [TIME],                 1.5 ],
    'rotation-handgun-object' : [ [SITTING, STANDING],  [SITTING, STANDING],    None,   [TIME],     1.5 ],
    'union-arms' :      [ [SITTING, STANDING],  [SITTING, STANDING],None,   [TIME],                 1.5 ],
    'rotation-foot-l' : [ [STANDING],           [STANDING],         True,   [TIME,LEGS_CONTROL],    3.5 ],
    'rotation-foot-r' : [ [STANDING],           [STANDING],         True,   [TIME,LEGS_CONTROL],    3.5 ],
}

MANDATORY_MOVEMENTS = {
    'StandInit' :       [ [STANDING],           [STANDING],         True,   [SPEED],                0    ],
    'Hello' :           [ [STANDING],           [STANDING],         None,   [TIME],                 3.9  ],
    'Stand' :           [ [STANDING],           [STANDING],         False,  [SPEED],                0.95 ],
    'Wipe-forehead' :   [ [STANDING],           [STANDING],         None,   [TIME],                 3.9  ],
    'StandZero' :       [ [STANDING],           [STANDING],         False,  [SPEED],                1.30 ],
    'Sit' :             [ [STANDING],           [SITTING],          False,  [SPEED],                12.02],
    'SitRelax' :        [ [SITTING],            [SITTING],          False,  [SPEED],                4.7  ],
    'Crouch' :          [ [SITTING],            [CROUCH],           False,  [SPEED],                13.92],
}

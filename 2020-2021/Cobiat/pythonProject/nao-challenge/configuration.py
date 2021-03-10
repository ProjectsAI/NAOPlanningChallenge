from naoqi import ALProxy
from positions import *
import os


nao_ip = "127.0.0.1"
nao_port = 39503
music_path = os.path.abspath(os.getcwd()) + '/music.wav'

modules_list = [
    Arms_opening,  # 0
    Crouch,  # 1
    Diagonal_left,  # 2
    Diagonal_right,  # 3
    Double_movement,  # 4
    Move_backward,  # 5
    Move_forward,  # 6
    Right_arm,  # 7
    Rotation_foot_LLeg,  # 8
    Rotation_foot_RLeg,  # 9
    Rotation_handgun_object,  # 10
    Sit,  # 11
    SitRelax,  # 12
    Stand,  # 13
    StandInit,  # 14
    StandZero,  # 15
    Union_arms,  # 16
    Hello,  # 17
    Wipe_Forehead,  # 18
    Mani_sui_fianchi,  # 19
    Chitarra,  # 20
    Ballo_braccia,  # 21
    Left_sprinkler,  # 22
    Right_sprinkler,  # 23
    Happy_Birthday  # 24
]

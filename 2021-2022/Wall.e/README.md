# NAO Planning Challenge 2021

**Team Name**: WALL-E

**Members**: Vincenzo Collura, Samuele Marino

_Fundamentals of Artificial Intelligence and Knowledge Representation_

Getting Started:

1. Use the NAO Virtual Machine
2. Make sure that both Python 2 and Python 3 are installed.
3. Download the repository
   ```
   git clone https://github.com/Enzossssss/NAOdanceProject
   ```
4. Open a terminal in the project path
5. Install numpy
   ```
   pip3 install numpy
   ```
6. Change permission for script

   ```
   chmod 777 ./start.sh
   ```

7. Open Choregraphe in order to simulate NAO
8. Connect to virtual robot
9. Copy the ip and the port of NAO
10. Launch the starting script

    ```
    ./start.sh <nao_ip> <nao_port>
    ```

# Video

The full video can be seen at the following [link](https://liveunibo-my.sharepoint.com/:v:/g/personal/samuele_marino_studio_unibo_it/EfDueZiOCRVOuNOPI9_SGGQBU-3woOOdwP5SfEL9Z5nQyw?e=EniBuR)

_Only people in Alma Mater Studiorum Università di Bologna can access to the link_

The demo video is in presentation folder

# Organization Folders

```
NAOdanceProject
├── generator
│   ├── aima
│   │   ├── __init__.py
│   │   ├── search.py
│   │   └── utils.py
│   ├── choreography.py
│   └── position.py
├── player
│   ├── choreography.txt
│   ├── mille.wav
│   ├── positions
│   │   ├── AirGuitar.py
│   │   ├── Arms_opening.py
│   │   ├── Ballo_braccia.py
│   │   ├── ComeOn.py
│   │   ├── Crouch.py
│   │   ├── Dab.py
│   │   ├── DanceMove.py
│   │   ├── Diagonal_left.py
│   │   ├── Diagonal_right.py
│   │   ├── Happy_Birthday.py
│   │   ├── Hello.py
│   │   ├── __init__.py
│   │   ├── Mani_sui_fianchi.py
│   │   ├── Move_backward.py
│   │   ├── Move_forward.py
│   │   ├── PulpFiction.py
│   │   ├── Right_arm.py
│   │   ├── Right_sprinkler.py
│   │   ├── Rotation_foot_LLeg.py
│   │   ├── Rotation_foot_RLeg.py
│   │   ├── Rotation_handgun_object.py
│   │   ├── Sit.py
│   │   ├── SitRelax.py
│   │   ├── Stand_from_sit.py
│   │   ├── StandInit.py
│   │   ├── Stand.py
│   │   ├── StandZero.py
│   │   ├── TheRobot.py
│   │   ├── time.txt
│   │   ├── Union_arms.py
│   │   └── Wipe_Forehead.py
│   └── robot.py
├── presentation
│   ├── demo_wall-e_short.mp4
│   └── presentation.pdf
├── README.md
└── start.sh

```

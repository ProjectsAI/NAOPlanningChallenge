# NAO Challenge 2021
###### Master of Artificial Intelligence - Fundamentals of Artificial Intelligence and Knowledge Representation

**Team:** Don't Stop Me NAO

**Team components:**

Simona Scala - simona.scala6@studio.unibo.it - 0001033460

Sara Vorabbi - sara.vorabbi@studio.unibo.it - 0001026226

### Files
- aima = folder containing aima's library files
- moves = folder containing the file of the dance moves
- music/bee_gees_stayin_alive.waw
- NAO Challenge 2021 - presentation
- planning_choreography.py
- play_music.py
- README
- demoDon_t_Stop_Me_NAO.mp4
- choreoDon_t_Stop_Me_NAO.mp4
- requirements.txt

### Execution
- Install python2.7 and python3.7 on your NAO Virtual Machine. Set python3.7 as default version
- Open a terminal inside the project folder "Don_t_Stop_Me_NAO" 
- Prepare the virtual environment using the following command
`$ python3.7 -m venv venv `
- Activate the virtual environment on you terminal
`$ . venv/bin/activate`
- Install all the requirements found in the requirements.txt file
`$ pip3 install -r requirements.txt`
- Open Choregraphe in order to simulate NAO
- Copy the IP and the PORT of the simulated NAO
- Launch the script 
`$ python3.7 planning_choreography.py <nao_ip> <nao_port>`

#### Mandatory moves
1. Hello
2. Sit
3. SitRelax
4. Stand
5. StandZero
6. Wipe Forehead

#### Intermidiate moves
1. Rotation Feet (x2)
2. Arm Dance DX
3. Arm Dance SX
4. Birthday Dance
5. Sprinkler 1
6. Sprinkler 2

#### Optional moves
1. Blow Kisses
2. Dance Move
3. Disco
4. Thriller Clap
5. Thriller Arm Sideways
6. Thriller Snap snap
7. V On Eyes

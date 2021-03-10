# DuoNao
This work was done by Ludovico Granata and Simone Persiani
as a study project for the "Fundamentals of AI and Knowledge
Representation" course (Master Degree in Artificial Intelligence - University of Bologna).

Our team was named "DuoNao" and our goal was to win the 2020 edition of the so called NaoChallenge.
The project was submitted on December 5th 2020.

## Resources
  * [Music](https://github.com/iosonopersia/duonao/blob/main/Don't%20stop%20me%20now%20-%20Queen.mp3)
  * [Demo video](https://github.com/iosonopersia/duonao/blob/main/Don't%20stop%20me%20NAO%20(queen).mp4)
  * [Presentation slides](https://github.com/iosonopersia/duonao/blob/main/NAO%20Challenge.pdf)

## Instructions
Starting from a working instance of the "NaoUbuntu" virtual machine:
  1. Install VLC and GIT:
```bash
sudo apt-get update
sudo apt-get install vlc git
```
  2. Download the repository:
```bash
git clone https://github.com/iosonopersia/duonao
```
  3. Get the needed Python3 tools:
```bash
cd duonao
pip3 install -U pip setuptools
sudo apt-get install python3-venv
```
  4. Prepare the virtual environment:
```bash
python3 -m venv venv
```
  5. Install the Python3 dependencies:
```bash
. venv/bin/activate
pip3 install -r requirements.txt
deactivate
```
  6. Run the script inside a terminal emulator
     (let's say the virtual robot is listening on the 42135 port):
```bash
cd duonao
. venv/bin/activate
python3 main.py localhost 42135
deactivate
```

**To run the script, Choreograph must be opened with a proper virtual robot available for external connections**
**Please, remember to do the following steps before launching the script:**
  1. **open Choreograph**
  2. **go to Edit->Preferences and open the 'General' tab**
  3. **set 'Motor speed (%)' to 100**
  4. **switch to the 'Virtual Robot' tab**
  5. **select the 'NAO H25 (V40)' as the 'Robot model'**
  6. **click on the 'OK' button in the bottom right of the modal window**

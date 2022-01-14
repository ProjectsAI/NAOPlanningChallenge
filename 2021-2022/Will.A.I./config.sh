#!/bin/bash

# run this script to configure the environment to run our solution
# pass to this file the right port of the robot
# to run the solution correctly you have to go into choreographe settings
# and select edit-->preferences set motor speed to 100 and in the virtual robot tab
# set the robot model to NAO H25 V40, on the bottom of the page you also find the port
# that you have to pass to this script

sudo apt-get install vlc
pip3 install -r dependencies.txt
python3 main.py localhost $1

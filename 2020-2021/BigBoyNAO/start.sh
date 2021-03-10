#!/bin/bash
echo "Started NAO Dance!"
#/usr/bin/python3 generate_choreography.py
echo "Starting movements. Look at your NAO!"
python make_movement.py $1 $2

#!/bin/bash
if [ $# -eq 2 ]
then
	cd generator
	python3 choreography.py

	cd ../player
	python2 robot.py $1 $2
else
  echo 'parameter not valid'
fi
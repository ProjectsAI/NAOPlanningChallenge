# Import required libraries for the simulation:
import importlib
import socket
import argparse
import time
import os
from mutagen.mp3 import MP3
from pygame import mixer
from Utils import nao_project
from RobotPositions import *

# Arguments to be passed to the Command Prompt:
parser = argparse.ArgumentParser(description='Argument parser')
parser.add_argument('--port', dest='port', type=int, default=9559, help='number of the virtual robot port') 
parser.add_argument('--ip', dest='ip',type=str,default='127.0.0.1', help='ip number')
parser.add_argument('--song', dest='song', type=str, default='RockNRollRobot.mp3', help="Song's name")
parser.add_argument('--search', dest='search', type=str, default='iterdeep', 
help='Name of the search algorithm. The only possible values are depth, breadth, iterdeep')
parser.add_argument('--threshold', dest='threshold', type=float, default=0.1, help="Threshold")
args = parser.parse_args()

# Function that is executed: it searches and executes the optimal sequence of moves with respect to the song's duration 
def main(robotIP,port,song_name = 'RockNRollRobot_from_0.11.mp3',search_type = 'breadth',threshold = 0.5): #the parameters are passed through the cmd Prompt
	initial_move = ('StandInit',1.13)           # Name of the initial move and its duration
	time_initial_move = initial_move[1]
	
	# List of the possible moves to be executed, expressed as a tuple containing the name of the move and its duration
	moves = [('AirGuitar',5.24),               
	('ArmDance',11.34),                         
	('BlowKisses',4.9),
	('Bow',4.6),
	('DanceMove',6.9),
	('SprinklerL',4.1),
	('SprinklerR',4.1),
	('Dab',3.1),
	('TheRobot',6.04),
	('ComeOn',4.61),
	('StayingAlive',5.91),
	('Rhythm',3.96),
	('PulpFiction',5.6)]
	
	# List of the mandatory positions, expressed as a tuple containing the name of the move and its duration
	constr_moves = [('Stand',2.02),             
	('Sit',3.02),
	('Hello',4.02),
	('StandZero',2.02),
	('SitRelax',3.02),
	('WipeForehead',4.1),
	('Crouch',1.05)]
	
	# List in which the sequence of moves to be executed is stored
	result = [initial_move[0]]                  
	
	# Assign to file_data the song name, passed to the function as an argument, and recover the song length
	file_data = os.path.splitext(song_name)    
	if file_data[1] == '.mp3':                  
		audio = MP3("./Songs/" + song_name)
		total_length = audio.info.length
	else:
		a = mixer.Sound("./Songs/" + song_name) 
		total_length = a.get_length()

	song_length = round(total_length,2)         
	# print(song_length)
	
    # Instantiate the variable our_project as instance of nao_project.project class with attributes: 
    # The mandatory positions, the list of possible moves, the available time, the type of search
	our_project = nao_project.project(constr_moves,moves,song_length - time_initial_move,search_type,threshold)   
	
    # For each of the mandatory positions run the method A in the class project with parameters: 
    # The updated list of the moves to be executed and the next mandatory move
	start = time.time()
	for i in constr_moves:
		our_project.A(result,i)
	print('Computational time with searchtype = ' + search_type)
	print(round((time.time() - start),2))
	print(result)
	
	# Load the song and play the song
	mixer.init()                                
	mixer.music.load("./Songs/" + song_name)  
	mixer.music.play()                              
	
	
	
	# Print a table on the cmd with the move that is being executed and its cost
	start = 0
	for i,move in enumerate(result):
		if i != 0:
			if ((i-1) % 6)==0:
				print('\n' + '{0:20}  {1}'.format(result[i-1], round((time.time() - start),2)).upper() + '\n')
			else:
				print('{0:20}  {1}'.format(result[i-1], round((time.time() - start),2)))     
		start = time.time()
		importlib.import_module("." + move,"RobotPositions").main(robotIP,port)          
		if i == 0:
			print('\n{0:20}  {1}'.format('Move', 'Cost (in seconds)'))                
		
	print('\n' + '{0:20}  {1}'.format(result[-1], round((time.time() - start),2)).upper() + '\n')              
	time.sleep(2)
	#playing_time = round(mixer.music.get_pos()/1000.0,2)
	#while ((total_length - playing_time) > 0):
		#playing_time = round(mixer.music.get_pos()/1000.0,2)
	
	
if __name__ == "__main__":  

	try:
		socket.inet_aton(args.ip)
		robotIP = args.ip
	except socket.error:
		print("Not a valid ip address")
		exit(1)
	search_type = args.search
	if(search_type not in ['depth','breadth','iterdeep']):
		print('The only possible values for --search argument are depth, breadthand iterdeep')
		exit(2)
		
	port = args.port	
	song_name = args.song
	threshold = args.threshold
	
	main(robotIP, port, song_name, search_type,threshold)
	


	








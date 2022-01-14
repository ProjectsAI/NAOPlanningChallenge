import subprocess
import multiprocessing
import coreography
import time
import sys

def playSong():
    bashCommand = "play atw3min.mp3"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def dance(moves, robot_ip, robot_port):
    print("Dance!")
    for move in moves[0]:
        python2_command = f"python2 ./NaoMoves/{move}.py  {robot_ip} {robot_port}"
        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        print("Move: {}".format(move), flush=True)

def main():
    robot_ip = input("Insert Robot IP: ")
    robot_port = input("Insert Robot Port: ")
    moves = coreography.search_coreography()
    process1 = multiprocessing.Process(target=playSong, args=())
    process2 = multiprocessing.Process(target=dance, args=((moves,), robot_ip, robot_port))
    process1.start()
    process2.start()
    process1.join()
    process2.join()


if __name__ == '__main__':
    main()

NAO PLANNING - SAMUELE DI TULLIO - samuele.ditullio@studio.unibo.it - A.Y. 2020/2021

Choreographe version: 2.8.6.23

The project includes a 3 minute choreograph, planned as follow:

- Initial position: Stand Init;
- An ".ogg" file is loaded and then played with the service "ALAudioPlayer", executed in parallel with the Animation box;
- A set of positions are executed, both using the Pose Library included in the software and some Timelines;
- The series of standing positions are executed at the beginning, while the sitting ones are executed at the end, thus saving time for the transition from one pose to another;
- Final position: Crouch;

* Timelines have been written by me and consists of a series of new positions drawn using the Inspector window, with wich I specified the angular grade of each joint, and the Behaviour Layer, with wich I decided the order and the duration of each position;
** First I decided to move a single joint at a time, starting from the standing position, then to combine the movements of more joints together playing with the equilibrium of the robot, and then to move more joints together mirroring the behaviour of left and right sides;

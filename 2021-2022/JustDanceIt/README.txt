"Just Dance It"
Authors: Filippo Imboccioli, Gabriele Cialone
 
Instructions
Starting from a working instance of the "NaoUbuntu" virtual machine:

1. Update the VM

  sudo apt-get update

2. Download the files from the repository using the link: 
  https://liveunibo-my.sharepoint.com/:f:/g/personal/filippo_imboccioli_studio_unibo_it/EnnaC4TJyaBBk7WSFHUPu9IBG7rL5vxZ8AiAmg_g6FyDFQ?e=5yr5x4

3. Move the files into the project folder

  mkdir justdanceit

3. Get the needed Python3 tools:

  cd justdanceit
  pip3 install -U pip setuptools
  pip3 install virtualenv

4. Prepare the virtual environment:

  python3 -m venv nao_env

5. Install the Python3 dependencies, tools and libraries - then execute:
  (let's say the virtual robot is listening on the 37431 port):

  source nao_env/bin/activate
  sudo chmod u+x install.sh
  sudo chmod u+x start.sh
  ./install.sh
  ./start.sh 127.0.0.1 37431 Harder,Better,Faster,Stronger_DaftPunk.mp3
  deactivate

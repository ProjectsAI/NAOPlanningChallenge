# ANaoRhythm
**Nao Planning Challange - 2021**

This Progect focuses on planning a Dance Coreography given constraints on:
- the total time of the coreography 
- mandatory moves that need to be executed.

I tried implementing a Search Algorithm subsampling an infinite tree of Feasible Solutions while also trying to optimize the number of Beat matching moves (moves that start on the first beat of a 4/4 bar).

**Group Members:**
- Stefano Ciapponi

# Setup (Unix Only):

- Clone The repository:
```
git clone https://github.com/drchapman-17/anaorhythm
```

- Run the commands.sh file to install **Python3** and **Sound eXchange** (Software used to play the audio file).
```
./commands.sh
```
- Create a Python Virtual Enviroment.
```
python3 -m venv [name]
```
- Access it running the "activate" script in the Bin folder.
```
source [name]/bin/activate
```
- Use PIP to install the requirements
```
pip install -r requirements.txt
```
# To run the Code:
- Open Coreographe->Edit->Preferences and Select the **NAO H25 (V40) Robot Model**.
- Run The Code:
```
python3 main.py
```
- Write NaoRobot's IP and Port.

- Enjoy the coreography!

# Resources:

- [Daft Punk - Around The World](https://www.youtube.com/watch?v=dwDns8x3Jb4)
- [Sound eXchange](http://sox.sourceforge.net/)
- [Treelib](https://treelib.readthedocs.io/en/latest/)
- [DuoNao Repo (For The NaoMoves Folder)](https://github.com/ProjectsAI/NAO_Planning_Challenge/tree/main/2020-2021/duonao)

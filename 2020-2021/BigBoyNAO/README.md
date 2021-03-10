# NAO Planning Challenge
**Group:** You're a big boy, NAO  
**Students:**
 - Agostino Aiezzo, <agostino.aiezzo@studio.unibo.it>
 - Emmanuele Bollino, <emmanuele.bollino@studio.unibo.it>

### Files
Presentation of the project in in the file "\_PRESENTATION/Slides.pdf"  
Video demonstration of the dance is in the file "\_PRESENTATION/Video_choreography.mp4"

### Instructions
 - Use the NAO Virtual Machine
 - Make sure that both Python 2 and Python 3 are installed. Default version should be 2
 - Create a PyCharm project and add all the files in here (use PyCharm just to import NaoQi)
 - Import NaoQi from the download (Scaricati) folder, it is already in there
 - Open a terminal in the project path
 - Change permission for scripts
    ```sh
    chmod 777 ./start.sh
    chmod 777 ./install.sh
    ```
 - Install all the requirements
    ```sh
    ./install.sh
    ```
 - Open Choregraphe in order to simulate NAO
 - Copy the ip and the port of the simulated (or real) NAO
 - Launch the starting script
    ```sh
    ./start.sh <nao_ip> <nao_port>
    ```
 - Planning generation may take a while, just be patient
 - Look at NAO!

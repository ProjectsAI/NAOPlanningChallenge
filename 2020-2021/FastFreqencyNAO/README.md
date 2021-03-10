# NAOChallenge FAST-FREQUENCY
**Participants:** 
[Zarmina Ursino](https://github.com/Zarmina97) , 
[Sandeep Kumar Kushwaha](https://github.com/xandie985) , 
[Samral Tahirli](https://github.com/samraltahirli)

**OBTAIN THE CHOREGRAPHE FILE HERE:** https://drive.google.com/drive/folders/1pIRpZiDuBrvC3VIPP3ZKrkusU_yLcD5j?usp=sharing 

**Folder description:**
The folder contains the actions files
  > those starting with "m_" are mandatory ones
  >  those starting with "o_" are the optional ones that we have created
"mainFile.py" contains the code the run the action figures based on the most appropriate costs

**How it works:**
1. The action files are saved with extra lists- keyValues & finalPositionValue. 
    keyValues - contains the key positions i.e. - LshoulderPitch, LshoulderRoll, LElbowYaw, LElbowRoll, LHipYawPitch, LHipPitch, LKneePitch
    finalPositionValues - contain the final position of above parameters for each movement
    
2. The mainFile.py contains following:
    >*the action files are imported and saved into two seperate lists
    
    >*execute_performance() - runs the code the action that has been provided through the parameter; need to provide specific port address
    
    >*costDofference(val1, val2, val3) - val1 is intial mandatory position, val3 is final mandatory position, val2 is the position that needs to be picked from the availablePos[]
    
    >*findTheNextNode() - finds the most optimum movement from the optional positions with the help of costDifference function and thereby executes that particular funxtion and removes it from the list, so the optional movements is not considered later
    
    >*mainFunctionToRun() - this is main driver function that initiates the actions!
    
    >*commented code below - was used to fetcht the important list values for action files.

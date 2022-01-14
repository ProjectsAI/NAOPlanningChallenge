from NaoClass import *
import json


def main():
    # Get All states defining distance of each mandatory position with all intermediate positions */
    my_file = "movement_times.json"
    if (os.path.exists(my_file)):
        with open(my_file) as f:
            allStatesTimes = json.load(f)

    mandatoryPositions = ["StandInit", "Sit", "SitRelax", "Stand", "WipeForehead", "Hello", "StandZero", "Crouch"]
    intermediatePositions = [
        "AirGuitar",
        "ArmDance",
        "Bow",
        "ComeOn",
        "StayingAlive",
        "Dab",
        "DanceMove",
        "Clap",
        "BlowKisses",
        "Right_arm",
        "Diagonal_left",
        "Double_movement",
        "Union_arms",
        "Arms_opening",
        "Diagonal_right",
        "Double_movement",
        "Move_backward",
        "Move_forward",
        "Rotation_foot_LLeg",
        "Rotation_foot_RLeg",
        "Rotation_handgun_object",
        "Union_arms",
        "Joy",
        "Glory",
        "PulpFiction",
        "Rhythm"
    ]

    total_minutes = 4
    timeLimit = total_minutes * 60

    initialState = (
        ('movesList', ()),
        ('remainingTime', timeLimit),
        ('movesDone', 0)
    )
    finalState = (
        ('remainingTime', 0),
        ('movesDone', 7)
    )

    problemStatement = NaoClass(
        initialState,
        finalState,
        mandatoryPositions,
        intermediatePositions,
        timeLimit,
        allStatesTimes)

    result = astar_search(problemStatement)
    state = problemStatement.convert_tuple(result.state)
    optimalSolution = state["movesList"]
    f = open("GeneratedDanceMoves.txt", "w")
    for move in optimalSolution:
        f.write(str(move) + "\n")
    f.close()

    print("Generated moves dance sequence is:")
    print(optimalSolution)
    print("Total number of moves:")
    print(state["movesDone"])


if __name__ == "__main__":
    main()

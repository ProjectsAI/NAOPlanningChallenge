import aima.utils
import aima.planning
import copy
import random

def plan_positions(compatibilities, initial, final):
    knowledge_base = []
    positions = []

    # converting compatibilities into pddl knowledge base
    for p, dests in compatibilities.items():
        positions.append(p)
        for dest in dests:
            knowledge_base.append(aima.utils.expr("Compatible(" + str(p) + "," + str(dest) + ")"))

    # adding initial position to knowledge base
    knowledge_base.extend([
        aima.utils.expr("In(" + initial + ")")
    ])

    # ACTIONS
    # move action for the robot that goes from the position x to the position y
    move = aima.planning.Action('Move(x, y)',
                                precond='In(x) & Compatible(x, y)',
                                effect='In(y) & ~In(x)',
                                domain='Position(x) & Position(y)')

    # GOALS
    goals = "In(" + final + ")"

    # defining the domain of positions, conjunction of declaration of position objects
    positions_domain = ""
    for p in positions:
        positions_domain += "Position(" + str(p) + ") & "
    positions_domain = positions_domain[:len(positions_domain) - 3]

    # PROBLEM DEFINING
    problem = aima.planning.PlanningProblem(initial=knowledge_base,
                                            goals=goals,
                                            actions=[move],
                                            domain=positions_domain)

    solution = aima.planning.GraphPlan(problem).execute()
    return aima.planning.linearize(solution)


def extract_dest(move):
    #return str(move).split(" ")[-1].removesuffix(")")
    string = str(move).split(" ")[-1]
    return string[:len(string)-1]


def generate_positions(compatibilities, initial, final, min_moves):
    solution = []
    used_compatibilities = {}
    for k, v in compatibilities.items():
        used_compatibilities[k] = copy.copy(v)
    # assumption: a valid plan exists from every starting position
    # assumption: removing only one compatibility, there will always exist a valid plan
    while True:
        # random shuffle compatibilities dictionary
        comp_list = list(used_compatibilities.items())
        for item in comp_list:
            random.shuffle(item[1])
        random.shuffle(comp_list)
        used_compatibilities = dict(comp_list)

        solution.extend(plan_positions(used_compatibilities, initial=initial, final=final))

        if len(solution) >= min_moves - 1:
            break

        # for k, v in compatibilities.items():
        #    used_compatibilities[k] = copy.copy(v)

        solution.remove(solution[-1])
        if len(solution) > 0:
            second_last = extract_dest(solution[-1])
            used_compatibilities.get(second_last).remove(final)
            initial = second_last
        else:
            used_compatibilities.get(initial).remove(final)

        # artistic correction: remove looping moves
        if len(solution) >= 4:
            for i in range(len(solution) - 3):
                if solution[i] == solution[i + 2] and solution[i + 1] == solution[i + 3]:
                    first = extract_dest(solution[-1])
                    second = extract_dest(solution[-2])
                    solution = solution[:len(solution) - 2]
                    used_compatibilities.get(first).remove(second)
                    break

    return solution


def generate_full_plan(positions, compatibilities, min_moves=7):
    solution = []
    for i in range(len(positions) - 1):
        print("Generating intermediate plan from " + positions[i] + " to " + positions[i + 1])

        solution_part = generate_positions(compatibilities=compatibilities,
                                           initial=positions[i],
                                           final=positions[i + 1],
                                           min_moves=min_moves)
        solution.extend(solution_part)
        if i != len(positions) - 2:
            solution = solution[:len(solution)]

        # assumes more ways
        choreography_part = generate_choreography(solution_part)
        for j in range(len(choreography_part) - 2):
            compatibilities[choreography_part[j]].remove(choreography_part[j + 1])
        if (not choreography_part[1] in positions):
            compatibilities.pop(choreography_part[1], None)

    return solution


def generate_choreography(moves):
    choreography = [str(moves[0]).split("(")[1].split(",")[0]]
    for move in moves:
        #choreography.append(str(move).split(" ")[1].removesuffix(")"))
        string = str(move).split(" ")[-1]
        string = string[:len(string)-1]
        choreography.append(string)
    return choreography
    
def generate_choreography_file(choreography):
    f = open("choreography.txt", "w")
    for move in choreography:
        f.write(str(move)+"\n")
    f.close()
    print("Choreography exported in choreography.txt")


def main():
    compatibilities = {
        "StandInit": ["StandZero", "Stand", "Crouch", "Sit", "SitRelax", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "StandZero": ["StandInit", "Stand", "Crouch", "Sit", "SitRelax", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Stand": ["StandInit", "StandZero", "Crouch", "Sit", "SitRelax", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Crouch": ["StandInit", "StandZero", "Stand", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Sit": ["StandInit", "StandZero", "Stand", "Crouch", "WipeForehead", "Guitar", "DiagonalRight", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "SitRelax": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "Guitar", "DiagonalRight", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight"],
        "WipeForehead": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Guitar": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "DiagonalRight": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "RotationRightFoot": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "RotationLeftFoot": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "RotationHandgunObject": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "RotationRightArm": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "DoubleMovement": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "ArmsOpening": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "UnionArms": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "MoveForward": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "MoveBackward": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "DiagonalLeft": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "HappyBirthday": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Workout": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "SprinklerLeft", "SprinklerRight", "Hello"],
        "SprinklerLeft": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerRight", "Hello"],
        "SprinklerRight": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "Hello"],
        "Hello": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight"],
    }
    goals = ["StandInit", "Sit", "WipeForehead", "Hello", "SitRelax", "Stand", "StandZero", "Crouch"]
    #goals = ["StandInit", "Sit"]

    print("Finding plan")

    solution = generate_full_plan(compatibilities=compatibilities, positions=goals, min_moves=7)
    choreography = generate_choreography(solution)

    print("Plan found!")
    print("Nao moves: {0}".format(choreography))
    
    generate_choreography_file(choreography)
    


# Tell python to run main method
if __name__ == "__main__":
    main()

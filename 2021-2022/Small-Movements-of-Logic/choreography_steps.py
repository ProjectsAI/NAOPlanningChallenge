import aima.utils
import copy
import random
import aima.planning

#method to modeling the graphplan problem.
#defining PDDL modeling.
def aima_graphplan(compatibilities, initial, final):
    positions = []
    KW = []
    for j, y in compatibilities.items():
        positions.append(j)
        for i in y:
            KW.append(aima.utils.expr("Compatible(" + str(j) + "," + str(i) + ")"))

    KW.extend([aima.utils.expr("In(" + initial + ")")])
    # move action for the robot that goes from the position x to the position y
    action = aima.planning.Action('Move(x, y)',precond='In(x) & Compatible(x, y)',effect='In(y) & ~In(x)',domain='Position(x) & Position(y)')
    gl = "In("+ final +")"
    #defining the domain of positions, conjunction of declaration of position objects
    dom= ""
    for position in positions:
        dom+="Position(" + str(position) + ") & "
    dom= dom[:len(dom) - 3]
    problem = aima.planning.PlanningProblem(initial=KW,goals=gl,actions=[action],domain=dom)
    solution = aima.planning.GraphPlan(problem).execute()
    linear_sol=aima.planning.linearize(solution)
    return linear_sol



def entire_plan(final_steps, list_c, num_mv=7):
    solution = []
    for i in range(len(final_steps) - 1):
        print("implementing sub-plan between " + final_steps[i] + " and " + final_steps[i + 1])
        #solution_part = generate_positions(compatibilities=compatibilities,initial=positions[i],final=positions[i + 1],min_moves=min_moves)
        #Generation of intermediate path of 7 movements
        #search of intermediate path of 7 movements between 2 intermediate positions
        initial = final_steps[i]
        final = final_steps[i + 1]
        solution_intermediate = []
        used_compatibilities = {}
        for k, v in list_c.items():
            used_compatibilities[k] = copy.copy(v)
            # assumption: a valid plan exists from every starting position
            # assumption: removing only one compatibility, there will always exist a valid plan
        while True:
            #random shuffle
            comp_list = list(used_compatibilities.items())
            for item in comp_list:
                random.shuffle(item[1])
            random.shuffle(comp_list)
            used_compatibilities = dict(comp_list)
            #invocation of method of aima method.
            solution_intermediate.extend(aima_graphplan(used_compatibilities, initial=initial, final=final))
            if len(solution_intermediate) >= num_mv - 1:
                break
            solution_intermediate.remove(solution_intermediate[-1])
            if len(solution_intermediate) > 0:
                #(str(solution_intermediate[-1]).split(" ")[-1])[:len(string) - 1]
                #second_last = extract_dest(solution_intermediate[-1])
                sclst=str(solution_intermediate[-1]).split(" ")[-1]
                last =sclst[:len(sclst) - 1]
                used_compatibilities.get(last).remove(final)
                initial = last
            else:
                used_compatibilities.get(initial).remove(final)

        #each intermediate plan is inserted in the array
        #at end array solution contains the full plan
        solution.extend(solution_intermediate)
       
    return solution

#main method
#returns the text file of choreography
def main():
    #dictionary data structure containing all movements and their compatible movements
    mainlist = {
        "SitRelax": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "Guitar", "DiagonalRight", "MoveForward",
                     "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight"],
        "StandInit": ["StandZero", "Stand", "Crouch", "Sit", "SitRelax", "WipeForehead", "Guitar", "DiagonalRight",
                      "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                      "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                      "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Stand": ["StandInit", "StandZero", "Crouch", "Sit", "SitRelax", "WipeForehead", "Guitar", "DiagonalRight",
                  "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                  "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                  "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "StandZero": ["StandInit", "Stand", "Crouch", "Sit", "SitRelax", "WipeForehead", "Guitar", "DiagonalRight",
                      "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                      "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                      "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Crouch": ["StandInit", "StandZero", "Stand", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                   "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                   "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                   "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Sit": ["StandInit", "StandZero", "Stand", "Crouch", "WipeForehead", "Guitar", "DiagonalRight",
                "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms",
                "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft",
                "SprinklerRight", "Hello"],
        "WipeForehead": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "Guitar", "DiagonalRight",
                         "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                         "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                         "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Guitar": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "DiagonalRight",
                   "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                   "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                   "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "DiagonalRight": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar",
                          "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                          "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                          "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "RotationRightFoot": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar",
                              "DiagonalRight", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                              "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward",
                              "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "RotationHandgunObject": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar",
                                  "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationRightArm",
                                  "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward",
                                  "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight",
                                  "Hello"],
        "RotationLeftFoot": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar",
                             "DiagonalRight", "RotationRightFoot", "RotationHandgunObject", "RotationRightArm",
                             "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward",
                             "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "RotationRightArm": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar",
                             "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject",
                             "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward",
                             "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "DoubleMovement": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar",
                           "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject",
                           "RotationRightArm", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward",
                           "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "MoveBackward": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                         "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                         "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "DiagonalLeft", "HappyBirthday",
                         "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "ArmsOpening": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                        "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                        "DoubleMovement", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday",
                        "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "UnionArms": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                      "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                      "DoubleMovement", "ArmsOpening", "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday",
                      "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "MoveForward": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                        "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                        "DoubleMovement", "ArmsOpening", "UnionArms", "MoveBackward", "DiagonalLeft", "HappyBirthday",
                        "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "DiagonalLeft": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                         "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                         "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "HappyBirthday",
                         "Workout", "SprinklerLeft", "SprinklerRight", "Hello"],
        "Hello": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                  "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                  "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                  "HappyBirthday", "Workout", "SprinklerLeft", "SprinklerRight"],
        "HappyBirthday": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                          "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms",
                          "MoveForward", "MoveBackward", "DiagonalLeft", "Workout", "SprinklerLeft", "SprinklerRight",
                          "Hello"],
        "Workout": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                    "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject", "RotationRightArm",
                    "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward", "MoveBackward", "DiagonalLeft",
                    "HappyBirthday", "SprinklerLeft", "SprinklerRight", "Hello"],
        "SprinklerLeft": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar", "DiagonalRight",
                          "RotationHandgunObject", "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms",
                          "MoveForward", "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerRight",
                          "Hello"],
        "SprinklerRight": ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "WipeForehead", "Guitar",
                           "DiagonalRight", "RotationRightFoot", "RotationLeftFoot", "RotationHandgunObject",
                           "RotationRightArm", "DoubleMovement", "ArmsOpening", "UnionArms", "MoveForward",
                           "MoveBackward", "DiagonalLeft", "HappyBirthday", "Workout", "SprinklerLeft", "Hello"],
    }

    #array of possible goals positions.
    final_positions = ["StandInit", "Sit", "WipeForehead", "Hello","UnionArms", "Stand", "StandZero", "Crouch"]

    #invocation of method that returns the entire plan from initial state to one of goal state.

    sol = entire_plan(list_c=mainlist, final_steps=final_positions, num_mv=6)

    #extraction of all strings in variable solution.
    choreo = [str(sol[0]).split("(")[1].split(",")[0]]
    #for loop to iterate over all strings and append them to an array.
    for sl in sol:
        string_mov = str(sl).split(" ")[-1]
        string_movement = string_mov[:len(string_mov)-1]
        choreo.append(string_movement)

    print("Ballet found")
    print("Nao movement: {0}".format(choreo))

    #open a text file and iterate over all array containing strings of movements
    file_name = open("ballet.txt", "w")
    for step in choreo:
        #write all strings in a file text on different lines.
        file_name.write(str(step)+"\n")
    file_name.close()

    print("Final choreography printed in ballet.txt")




if __name__ == "__main__":
    main()
import math


positive_responses = ["yes", 'y']


class Force:
    def __init__(self, name, direction, magnitude, presence, defined, axis):
        self.name = name
        self.direction = direction
        self.magnitude = magnitude
        self.presence = presence
        self.defined = defined
        self.axis = axis


class Information:
    def __init__(self, mass, initial_velocity, final_velocity, acceleration, gravitational_field_strength,
                 time, work, distance, average_velocity, mew, k, compression):
        self.mass = mass
        self.initial_velocity = initial_velocity
        self.final_velocity = final_velocity
        self.acceleration = acceleration
        self.net_force = Force("Net Force", None, None, True, False, None)
        self.g = gravitational_field_strength
        self.time = time
        self.work = work
        self.distance = distance
        self.average_velocity = average_velocity
        self.mew = mew
        self.k = k
        self.compression = compression
        self.weight = Force("Weight", None, None, None, False, None)
        self.spring_force = Force("Spring Force", None, None, None, False, None)
        self.applied_force = Force("Applied Force", None, None, None, False, None)
        self.normal_force = Force("Normal Force", None, None, None, False, None)
        self.frictional_force = Force("Frictional Force", None, None, None, False, None)


def acceleration_formula_1():
    # solves for acceleration using change in velocity and time
    finished = False
    while not finished:
        try:
            if known.final_velocity is None:
                known.final_velocity = float(input("what is the final velocity (m/s)"))
            if known.time is None:
                known.time = float(input("what is the time (s)"))
            return (known.final_velocity - known.initial_velocity) / known.time
        except ValueError:
            print("inputs must be numbers")


def acceleration_formula_2():
    # solves for acceleration using change in velocity and distance
    finished = False
    while not finished:
        try:
            if known.final_velocity is None:
                known.final_velocity = float(input("what is the final velocity (m/s)"))
            if known.distance is None:
                known.distance = float(input("what is the distance (m)"))
            return (known.final_velocity ** 2 - known.initial_velocity ** 2) / (2 * known.distance)
        except ValueError:
            print("inputs must be numbers")


def acceleration_formula_3():
    # solves for acceleration with time distance and initial velocity
    finished = False
    while not finished:
        try:
            if known.time is None:
                known.time = float(input("what is the time (s)"))
            if known.distance is None:
                known.distance = float(input("what is the distance (m)"))
            return (2 * (known.distance - (known.initial_velocity * known.time))) / (known.time ** 2)
        except ValueError:
            print("inputs must be numbers")


def solve_acceleration_kinematics():
    finished = False
    while not finished:
        try:
            if known.initial_velocity is None:
                known.initial_velocity = float(input("what is the initial velocity (m/s)"))
            if known.distance is None:
                if input("is distance known").lower() in positive_responses:
                    distance_defined = True
                else:
                    distance_defined = False
            else:
                distance_defined = True
            if known.time is None:
                if input("is time known").lower() in positive_responses:
                    time_defined = True
                else:
                    time_defined = False
            else:
                time_defined = True
            if known.final_velocity is None:
                if input("is final velocity known").lower() in positive_responses:
                    final_velocity_defined = True
                else:
                    final_velocity_defined = False
            else:
                final_velocity_defined = True
            if final_velocity_defined and time_defined:
                return acceleration_formula_1()
            elif final_velocity_defined and distance_defined:
                return acceleration_formula_2()
            elif distance_defined and time_defined:
                return acceleration_formula_3()
            else:
                print("not enough information")
                finished = True
        except ValueError:
            print("inputs must be numbers")


def solve_force_net_mass_and_acceleration():
    finished = False
    while not finished:
        try:
            if known.mass is None:
                if input("Is mass known?").lower() in positive_responses:
                    known.mass = float(input("what is the mass"))
                else:
                    if input("Is weight known?").lower() in positive_responses:
                        known.mass = solve_mass_weight()
            if known.acceleration is None:
                if input("Is acceleration known?").lower() in positive_responses:
                    known.acceleration = float(input("what is the acceleration"))
                    return known.mass * known.acceleration
                else:
                    known.acceleration = solve_acceleration_kinematics()
                    return known.mass * known.acceleration
            else:
                return known.mass * known.acceleration
        except ValueError:
            print("inputs must be numbers")


def solve_acceleration_force_and_mass():
    finished = False
    while not finished:
        try:
            if known.net_force.magnitude is None:
                known.net_force.magnitude = float(input("what is the force net (N)"))
            if known.mass is None:
                known.mass = float(input("what is the mass (kg)"))
            return known.net_force.magnitude / known.mass
        except ValueError:
            print("inputs must be numbers")


def solve_mass_force_and_acceleration():
    finished = False
    while not finished:
        try:
            if known.net_force.magnitude is None:
                known.net_force.magnitude = float(input("what is the force net (N)"))
            if known.acceleration is None:
                if input("Is acceleration known").lower() in positive_responses:
                    known.acceleration = float(input("what is the acceleration"))
                else:
                    known.acceleration = solve_acceleration_kinematics()
            return known.net_force.magnitude / known.acceleration
        except ValueError:
            print("inputs must be numbers")


def solve_mass_weight():
    # uses weight and gravitational field strength (g) to find mass
    finished = False
    while not finished:
        try:
            if known.weight.magnitude is None:
                known.weight.magnitude = float(input("what is the weight (N)"))
            if known.g is None:
                if input("is the object on the earths surface").lower in positive_responses:
                    known.g = 9.8
                else:
                    if input("do you know the gravitational field strength?").lower() in positive_responses:
                        known.g = float(input("what is the gravitational field strength?"))
                    else:
                        print("we will have to find the g of the object pulling on your object")
                        known.g = solve_g_universal_gravitation()
            return known.weight.magnitude / known.g
        except ValueError:
            print("you must enter numbers as values")


def solve_g_universal_gravitation():
    finished = False
    while not finished:
        try:
            object_pulling = input("what is the object you're looking for the g of").lower()
            if object_pulling == "earth" or object_pulling == "the earth":
                mass = 5.972e24
                radius_object_pulling = 6.371e6
            elif object_pulling == "sun" or object_pulling == "the sun":
                mass = 1.989e30
                radius_object_pulling = 6.9551e8
            elif object_pulling == "mars":
                mass = 6.39e23
                radius_object_pulling = 3.3895e6
            elif object_pulling == "jupiter":
                mass = 1.898e27
                radius_object_pulling = 6.9911e7
            else:
                mass = float(input("what is the mass of the object you are looking for the g of"))
                radius_object_pulling = float(input("what is the radius of the object you are looking for the g of"))
            orbital_radius = float(input("how far from the object are you looking for the g of"))
            return (6.67e-11 * mass) / ((orbital_radius + radius_object_pulling) ** 2)
        except ValueError:
            print("you must enter numbers as values")


def solve_distance_kinematics():
    finished = False
    while not finished:
        if known.initial_velocity is not None or input("is initial velocity known").lower() in positive_responses:
            initial_velocity_defined = True
        else:
            initial_velocity_defined = False
        if known.acceleration is not None or input("is acceleration known").lower() in positive_responses:
            acceleration_defined = True
        else:
            acceleration_defined = False
        if known.time is not None or input("is time known").lower() in positive_responses:
            time_defined = True
        else:
            time_defined = False
        if known.final_velocity is not None or input("is the final velocity known").lower() in positive_responses:
            final_velocity_defined = True
        else:
            final_velocity_defined = False
        if acceleration_defined and initial_velocity_defined and time_defined:
            return distance_formula_1()
        elif acceleration_defined and initial_velocity_defined and final_velocity_defined:
            return distance_formula_2()
        else:
            print("not enough information")
            finished = True


def distance_formula_1():
    # solves for distance using initial velocity time and acceleration
    finished = False
    while not finished:
        try:
            if known.acceleration is None:
                known.acceleration = float(input("what is the acceleration"))
            if known.initial_velocity is None:
                known.initial_velocity = float(input("what is the initial velocity"))
            if known.time is None:
                known.time = float(input("what is the time"))
            finished = True
            return (known.initial_velocity * known.time) + (.5 * known.acceleration * (known.time ** 2))
        except ValueError:
            print("Values must be numbers")


def distance_formula_2():
    # solves for distance using acceleration and change in velocity
    finished = False
    while not finished:
        try:
            if known.acceleration is None:
                known.acceleration = float(input("what is the acceleration"))
            if known.initial_velocity is None:
                known.initial_velocity = float(input("what is the initial velocity"))
            if known.final_velocity is None:
                known.final_velocity = float(input("what is the final velocity"))
            finished = True
            return (known.final_velocity ** 2 - known.initial_velocity ** 2) / (2 * known.acceleration)
        except ValueError:
            print("Values must be numbers")


def solve_catch_up():
    # solves for how long it would take one object to catch up to another
    finished = False
    while not finished:
        try:
            velocity1 = float(input("What is the velocity of the object moving away"))
            velocity2 = float(input("What is the velocity of the object chasing"))
            distance = float(input("what is the distance between the two objects"))
            finished = True
            return (- distance) / (velocity1 - velocity2)
        except ValueError:
            print("Values must only be numbers")


def solve_time_kinematics():
    finished = False
    while not finished:
        try:
            if known.initial_velocity is None:
                known.initial_velocity = float(input("What it the initial velocity (m/s)"))
            if known.acceleration is None:
                known.acceleration = float(input("what is the acceleration if there is any (m/s^2) remember +/- for "
                                                 "direction"))
            if known.final_velocity is not None or input("do you know the final velocity").lower() in positive_responses:
                final_velocity_defined = True
            else:
                final_velocity_defined = False
            if known.distance is not None or input("do you know the final velocity").lower() in positive_responses:
                distance_defined = True
            else:
                distance_defined = False
            if distance_defined:
                if known.acceleration == 0:
                    return time_formula_1()
                else:
                    return time_formula_2()
            elif final_velocity_defined:
                return time_formula_3()
            else:
                print("There is not enough information known to calculate time using kinematics")
                finished = True
        except ValueError:
            print("Values must only be numbers")


def time_formula_1():
    # uses distance and a consistent velocity to solve for time
    finished = False
    while not finished:
        try:
            if known.distance is None:
                known.distance = float(input("What is the distance the object travels in the amount of time you're "
                                             "finding (m)"))
            if known.initial_velocity is None:
                known.initial_velocity = float(input("What is the object's velocity? (m/s)"))
            return known.distance / known.initial_velocity
        except ValueError:
            print("Values must be numbers")


def time_formula_2():
    # uses initial velocity, distance and acceleration to solve for time with the quadratic equation
    finished = False
    while not finished:
        try:
            if known.distance is None:
                known.distance = float(input("What distance does the object travel "
                                             "in the amount of time you are solving for (m)"))
            if known.initial_velocity is None:
                known.initial_velocity = float(input("What is the initial velocity? (m/s)"))
            root = math.sqrt(known.initial_velocity ** 2 - (4 * known.acceleration * - known.distance) / 2)
            if known.acceleration is None:
                known.acceleration = float(input("What is the objects acceleration? (m/s^2)"))
            if known.acceleration > 0:
                return (- known.initial_velocity + root) / known.acceleration
            elif known.acceleration < 0:
                return (- known.initial_velocity - root) / known.acceleration
        except ValueError:
            print("Values can only be numbers")


def time_formula_3():
    # solves for time using change in velocity and acceleration
    finished = False
    while not finished:
        try:
            if known.initial_velocity is None:
                known.initial_velocity = float(input("What is the initial velocity? (m/s)"))
            if known.acceleration is None:
                known.acceleration = float(input("What is the objects acceleration? (m/s^2)"))
            if known.final_velocity is None:
                known.final_velocity = float(input("What is the final velocity (m/s)?"))
            return (known.final_velocity - known.initial_velocity) / known.acceleration
        except ValueError:
            print("Values must be only numbers")


def solve_work_force_and_distance():
    finished = False
    while not finished:
        try:
            if known.net_force.magnitude is None:
                if input("Is the net force known?").lower() in positive_responses:
                    known.net_force.defined = True
                else:
                    known.net_force.defined = False
                if known.net_force.defined:
                    known.net_force.magnitude = float(input("What is the net force"))
                else:
                    known.net_force.magnitude = solve_force_net_mass_and_acceleration()
            if known.net_force.magnitude is not None:
                known.net_force.defined = True
                if known.distance is None:
                    if input("Is distance known?").lower() in positive_responses:
                        known.distance = float(input("What is the distance (m)"))
                    else:
                        known.distance = solve_distance_kinematics()
                return known.net_force.magnitude * known.distance
        except ValueError:
            print("Values must be numbers")


def solve_work_change_in_velocity():
    finished = False
    while not finished:
        try:
            if known.mass is None:
                if input("Is mass known").lower() in positive_responses:
                    known.mass = float(input("What is the objects mass (kg)"))
                else:
                    if known.weight is not None or input("Is weight known").lower() in positive_responses:
                        use_weight = True
                    else:
                        use_weight = False
                    if use_weight:
                        known.mass = solve_mass_weight()
                    else:
                        if (known.net_force.magnitude is not None and (known.acceleration is not None or
                                                                       (known.initial_velocity is not None and
                                                                        ((known.distance is not None and (known.time is
                                                                        not None or known.final_velocity is not None))
                                                                         or (known.final_velocity is not None and
                                                                             known.time is not None))))) \
                                or input("is force and either acceleration or time known").lower() \
                                in positive_responses:
                            known.mass = solve_mass_force_and_acceleration()
                        else:
                            print("Not enough information")
                            return None
            if known.mass is not None:
                if known.final_velocity is None:
                    if input("Is final velocity known?").lower() in positive_responses:
                        known.final_velocity = float(input("What is the final velocity? (m/s)"))
                    elif (known.acceleration is not None and known.initial_velocity is not known) or \
                            input("Are acceleration and initial velocity known").lower() in positive_responses:
                        known.final_velocity = solve_final_velocity_kinematics()
                    else:
                        print("Not enough information")
                        return None
                if known.final_velocity is not None:
                    if known.initial_velocity is None:
                        if input("Is initial velocity known?").lower() in positive_responses:
                            known.initial_velocity = float(input("what was the initial velocity"))
                        else:
                            known.initial_velocity = solve_initial_velocity_kinematics()
                    return .5 * known.mass * (known.final_velocity ** 2 - known.initial_velocity ** 2)
                else:
                    finished = True
            else:
                finished = True
        except ValueError:
            print("Values must be numbers")


def solve_final_velocity_kinematics():
    finished = False
    while not finished:
        try:
            if known.initial_velocity is None:
                known.initial_velocity = float(input("What is the initial velocity"))
            if known.acceleration is None:
                if input("is acceleration known").lower() in positive_responses:
                    known.acceleration = float(input("what is the acceleration"))
                elif (known.distance is not None and known.time is not None) or\
                        input("Are distance and time known").lower() in positive_responses:
                    known.acceleration = solve_acceleration_kinematics()
            if known.time is not None or input("Is time known").lower() in positive_responses:
                time_defined = True
            else:
                time_defined = False
            if known.distance is not None or input("is distance known").lower in positive_responses:
                distance_defined = True
            else:
                distance_defined = False
            if time_defined:
                return final_velocity_formula_1()
            if distance_defined:
                return final_velocity_formula_2()
            if not time_defined and not distance_defined and input("Is average velocity known?").lower()\
                    in positive_responses:
                return final_velocity_formula_3()
            else:
                print("Not enough information")
                return None
        except ValueError:
            print("Values must be numbers")


def final_velocity_formula_1():
    # solves for final velocity using initial velocity, acceleration and time
    finished = False
    while not finished:
        try:
            if known.initial_velocity is None:
                known.initial_velocity = float(input("What is the initial velocity (m/s)"))
            if known.acceleration is None:
                known.acceleration = float(input("What is the acceleration (m/s^2)"))
            if known.time is None:
                known.time = float(input("What is time (s)"))
            return known.initial_velocity + (known.acceleration * known.time)
        except ValueError:
            print("Values must be numbers")


def final_velocity_formula_2():
    # solves for final velocity using initial velocity, acceleration and distance
    finished = False
    while not finished:
        try:
            if known.initial_velocity is None:
                known.initial_velocity = float(input("What is the initial velocity (m/s)"))
            if known.acceleration is None:
                known.acceleration = float(input("What is the acceleration (m/s^2)"))
            if known.distance is None:
                known.distance = float(input("What is the distance (m)"))
            return math.sqrt(known.initial_velocity ** 2 + (2 * known.acceleration * known.distance))
        except ValueError:
            print("Values must be numbers")


def final_velocity_formula_3():
    # solves final velocity using average velocity and initial velocity
    if known.initial_velocity is None:
        known.initial_velocity = float(input("What is the initial velocity (m/s)"))
    if known.average_velocity is None:
        known.average_velocity = float(input("What is the average velocity (m/s)"))
    return 2 * known.average_velocity - known.initial_velocity


def solve_initial_velocity_kinematics():
    finished = False
    while not finished:
        if known.acceleration is not None or input("Is acceleration known?").lower() in positive_responses:
            acceleration_defined = True
        else:
            acceleration_defined = False
        if known.distance is not None or input("Is distance known?").lower() in positive_responses:
            distance_defined = True
        else:
            distance_defined = False
        if known.final_velocity is not None or input("Is final velocity known?") == "yes":
            final_velocity_defined = True
        else:
            final_velocity_defined = False
        if known.time is not None or input("Is time known?") == "yes":
            time_defined = True
        else:
            time_defined = False
        if acceleration_defined:
            if distance_defined and time_defined:
                return initial_velocity_formula_1()
            if distance_defined and final_velocity_defined:
                return initial_velocity_formula_2()
            if time_defined and final_velocity_defined:
                return initial_velocity_formula_3()
        else:
            if (known.average_velocity is not None or input("Is average velocity known?") == "yes") \
                    and final_velocity_defined:
                return initial_velocity_formula_4()
            else:
                print("Not enough information")
                return None


def initial_velocity_formula_1():
    # solves for initial velocity with acceleration, distance and time
    finished = False
    while not finished:
        try:
            if known.acceleration is None:
                known.acceleration = float(input("what is the acceleration (m/2^2)"))
            if known.distance is None:
                known.distance = float(input("What is the distance (m)"))
            if known.time is None:
                known.time = float(input("What is time (s)"))
            return (known.distance - .5 * known.acceleration * known.time ** 2) / known.time
        except ValueError:
            print("All values must be numbers")


def initial_velocity_formula_2():
    # solves for initial velocity with acceleration, distance and final velocity
    finished = False
    while not finished:
        try:
            if known.acceleration is None:
                known.acceleration = float(input("what is acceleration (m/s^2)"))
            if known.distance is None:
                known.distance = float(input("what is distance (m)"))
            if known.final_velocity is None:
                known.final_velocity = float(input("What is final velocity (m/s)"))
            return math.sqrt(known.final_velocity ** 2 - 2 * known.acceleration * known.distance)
        except ValueError:
            print("All values must be numbers")


def initial_velocity_formula_3():
    # solves for initial velocity using acceleration final velocity and time
    finished = False
    while not finished:
        try:
            if known.acceleration is None:
                known.acceleration = float(input("What is acceleration (m/s^2)"))
            if known.time is None:
                known.time = float(input("What is time (s)"))
            if known.final_velocity is None:
                known.final_velocity = float(input("What is final velocity (m/s)"))
            return known.final_velocity - known.acceleration * known.time
        except ValueError:
            print("All values must be numbers")


def initial_velocity_formula_4():
    # solves for initial velocity using average velocity and final velocity
    finished = False
    while not finished:
        try:
            if known.average_velocity is None:
                known.average_velocity = float(input("What is the average velocity (m/s)"))
            if known.final_velocity is None:
                known.final_velocity = float(input("What is the final velocity (m/s)"))
            return 2 * known.average_velocity - known.final_velocity
        except ValueError:
            print("All values must be numbers")


def solve_weight():
    finished = False
    while not finished:
        try:
            if known.mass is None:
                if input("Is mass known?") == "yes":
                    known.mass = float(input("What is mass (kg)"))
                elif input("Are force net and acceleration or a couple other things about the objects motion known"):
                    known.mass = solve_mass_force_and_acceleration()
                else:
                    print("Not enough information")
                    return None
            if known.g is None:
                if input("Is the object on the earth's surface") == "yes":
                    known.g = 9.8
                elif input("Is gravitational field strength known?"):
                    known.g = float(input("What is gravitational field strength"))
                else:
                    known.g = solve_g_universal_gravitation()
            return known.mass * known.g
        except ValueError:
            print("All values must be numbers")


def solve_g_weight_and_mass():
    finished = False
    while not finished:
        try:
            if known.weight.magnitude is None:
                known.weight.magnitude = float(input("What is the weight? (N)"))
            if known.mass is None:
                if (known.net_force.magnitude is not None and (known.acceleration is not None or (known.initial_velocity is not
                    None and ((known.final_velocity is not None and (known.distance is not None or known.time is not
                        None)) or (known.time is not None and known.distance is not None))))) or\
                        input("Are net force and acceleration or a couple things that could be used" 
                              "to find acceleration known") == "yes":
                    known.mass = solve_mass_force_and_acceleration()
                else:
                    return None
            return known.weight.magnitude / known.mass
        except ValueError:
            print("Values must all be numbers")


def solve_force_spring_k_and_compression():
    finished = False
    while not finished:
        try:
            if known.k is None:
                if input("Is the spring constant known?") == "yes":
                    known.k = float(input("What is the spring constant? (N/m)"))
                else:
                    print("Not enough information")
                    return None
            if known.compression is None:
                if input("Is the amount that the spring has either stretched or compressed known?"):
                    known.compression = float(input("What is the compression/expansion (m)"))
                else:
                    print("Not enough information")
                    return None
            return known.k * known.compression
        except ValueError:
            print("All values must be numbers")


def solve_k_force_spring_and_compression():
    finished = False
    while not finished:
        try:
            if known.spring_force.magnitude is None:
                if input("Is the spring force known?") == "yes":
                    known.spring_force.magnitude = float(input("What is the spring force? (N)"))
                else:
                    print("Not enough information")
                    return None
            if known.compression is None:
                if input("Is the amount of compression/expansion known") == "yes":
                    known.compression = float(input("What is the compression/expansion? (m)"))
                else:
                    print("Not enough information")
                    return None
            return known.spring_force.magnitude / known.compression
        except ValueError:
            print("All values must be numbers")


def solve_compression_force_spring_and_k():
    finished = False
    while not finished:
        try:
            if known.spring_force.magnitude is None:
                if input("Is the spring force known?") == "yes":
                    known.spring_force.magnitude = float(input("What is the spring force (N)"))
                else:
                    print("Not enough information")
                    return None
            if known.k is None:
                if input("Is the spring constant known") == "yes":
                    known.k = float(input("What is the spring constant? (N/m)"))
                else:
                    print("Not enough information")
                    return None
            return known.spring_force.magnitude / known.k
        except ValueError:
            print("All values must be numbers")


def solve_net_force_sum_of_forces():
    finished = False
    while not finished:
        try:
            if known.applied_force.presence or input("Is there an applied force") == "yes":
                known.applied_force.presence = True
                if known.applied_force.magnitude is None:
                    temp = input("What is the applied force?")
                    if temp == "?":
                        known.applied_force.defined = False
                    else:
                        known.applied_force.magnitude = float(temp)
                        known.applied_force.defined = True
                else:
                    known.applied_force.defined = True
                known.applied_force.axis = input("What axis is the force acting on? (x or y)").lower()
            if known.weight.presence or input("Is there a gravitational force on the object") ==


def main():
    solving_for = input("what do you need to solve for")
    if solving_for == "Fnet":
        print("Fnet =", str(solve_force_net_mass_and_acceleration()) + "N")
    elif solving_for == "a" or solving_for == "acceleration":
        use_force = input("are net force and mass known")
        if use_force == "yes":
            print("acceleration =", solve_acceleration_force_and_mass(), "m/s^2")
        else:
            known.acceleration = solve_acceleration_kinematics()
            if known.acceleration is not None:
                print("acceleration =", known.acceleration, "m/s^2")
    elif solving_for == "mass" or solving_for == "m":
        use_force = input("Are net force and acceleration known or do you have the net force and the information "
                          "required to find acceleration (yes or no)")
        if use_force == "yes":
            known.mass = solve_mass_force_and_acceleration()
            if known.mass is not None:
                print("mass =", known.mass, "kg")
        else:
            use_weight = input("is the weight known")
            if use_weight == "yes":
                print("mass =", solve_mass_weight(), "kg")
    elif solving_for == "distance" or solving_for == "d":
        known.distance = solve_distance_kinematics()
        print("distance =", known.distance, "meters")
    elif solving_for == "The amount of time it takes for one object to catch up with another":
        time = solve_catch_up()
        print("time =", time, "seconds")
    elif solving_for == "time" or solving_for == "t":
        use_kinematics = input("do you want to use kinematics?")
        if use_kinematics == "yes":
            known.time = solve_time_kinematics()
            if known.time is not None:
                print("time =", known.time, "seconds")
    elif solving_for == "Change in energy" or solving_for == "work" or solving_for == "W":
        use_force_and_distance = input("Do you want to use Force and distance")
        if use_force_and_distance == "yes":
            known.work = solve_work_force_and_distance()
            if known.work is not None:
                print("work =", known.work, "joules")
        else:
            use_kinetic_energy = input("Do you want to use the difference in kinetic energy")
            if use_kinetic_energy == "yes":
                known.work = solve_work_change_in_velocity()
                if known.work is not None:
                    print("work =", known.work, "joules")
    elif solving_for == "weight" or solving_for == "force of gravity" or solving_for == "Fg":
        known.weight = solve_weight()
        if known.weight is not None:
            print("Fg =", known.weight, "N")


done = False
while not done:
    do_calculations = input("would you like to do some calculations (yes or no)")
    while do_calculations == "yes":
        known = Information(None, None, None, None, None, None, None, None, None, None, None, None)
        main()
        do_calculations = input("would you like to continue (yes or no)")
    if do_calculations == "no":
        print("goodbye")
        done = True
    else:
        print("You must enter either yes or no")

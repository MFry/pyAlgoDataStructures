"""
    Difficulty: ***
    Code:       *
You are planning the amount of fuel need to complete a drone flight.
To fly higher, the drone burns 1 liter of fuel per feet. However, flying lower charges the drone with the amount of energy equivalent to 1 liter of fuel for every feet. Flying sideways takes no energy (only flying up and down takes/charges energy).

Given an array of 3D coordinates named route, find the minimal amount of fuel the drone would need to fly through this route.
Explain and code the most efficient solution possible, with the minimal number of actions and variables.

Example:
Completing the route [{x:0, y:2, z:10}, {x:3, y:5, z:0}, {x:9, y:20, z:6}, {x:10, y:12, z:15}, {x:10, y:10, z:8}] requires a minimum of 5 liters of fuel.


"""


def drone_flight_planner(route):
    """
    input: [{x:0, y:2, z:10}, {x:3, y:5, z:0}, {x:9, y:20, z:6}, {x:10, y:12, z:15}, {x:10, y:10, z:8}]
    output: 5
    """
    # You are correct
    energy = 0
    fuel = 0
    prev_elevation = route[0][2]
    for (_, _, e) in route[1:]:
        e_delta = prev_elevation - e
        # We gain extra energy
        if e_delta > 0:
            energy += e_delta
        # we lose a portion of the energy
        elif energy - e_delta > 0:
            energy -= e_delta
        # we have not enough energy left
        else:
            e_delta -= energy
            energy = 0
            fuel += e_delta
        prev_elevation = e

    return fuel


def clean_solution(route):
    start_elevation = route[0][3]
    max_elevation = max(route, key=lambda x: x[3])
    return max_elevation - start_elevation

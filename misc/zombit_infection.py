"""
Zombit infection
================

Dr. Boolean continues to perform diabolical studies on your fellow rabbit kin, and not all of it is taking place
 in the lab. Reports say the mad doctor has his eye on infecting a rabbit in a local village with a virus that
  transforms rabbits into zombits (zombie-rabbits)!

Professor Boolean is confident in the virus's ability to spread, and he will only infect a single rabbit.
Unfortunately, you and your fellow resistance agents have no idea which rabbit will be targeted.
You've been asked to predict how the infection would spread if uncontained, so you decide to create a simulation
 experiment. In this simulation, the rabbit that Dr. Boolean will initially infect will be called "Patient Z".

So far, the lab experts have discovered that all rabbits contain a property they call "Resistance", which is capable
 of fighting against the infection. The virus has a particular "Strength" which Dr. Boolean needs to make at least
  as large as the rabbits' Resistance for it to infect them.

You will be provided with the following information:
population = A 2D non-empty array of positive integers of the form population[y][x], that is, row then column.
(The dimensions of the array are not necessarily equal.) Each cell contains one rabbit, and the value of the cell
 represents that rabbit's Resistance.

x = The X-Coordinate (column) of "Patient Z" in the population array.
y = The Y-Coordinate (row) of "Patient Z" in the population array.
strength = A constant integer value representing the Strength of the virus.

Here are the rules of the simulation: First, the virus will attempt to infect Patient Z. Patient Z will only be
 infected if the infection's Strength equals or exceeds Patient Z's Resistance. From then on, any infected rabbits
  will attempt to infect any uninfected neighbors (cells that are directly - not diagonally - adjacent in the array).
   They will succeed in infecting any neighbors with a Resistance lower than or equal to the infection's Strength.
    This will continue until no further infections are possible (i.e., every uninfected rabbit adjacent to an infected
     rabbit has a Resistance greater than the infection's Strength.)

You will write a function answer(population, x, y, strength), which outputs a copy of the input array representing the
 state of the population at the end of the simulation, in which any infected cells value has been replaced with -1.
The Strength and Resistance values will be between 0 and 10000. The population grid will be at least 1x1 and no larger
 than 25x25. The x and y values will be valid indices in the population arrays, with numbering beginning from 0.

"""
import unittest


def answer(population, x, y, strength):
    """
    :param population: A 2D non-empty array of positive integers of the form population[y][x],
    that is, row then column.
    (The dimensions of the array are not necessarily equal.) Each cell contains one rabbit,
     and the value of the cell represents that rabbit's Resistance.
    :param x: The X-Coordinate (column) of "Patient Z" in the population array
    :param y: The Y-Coordinate (row) of "Patient Z" in the population array
    :param strength: A constant integer value representing the Strength of the virus
    :return: outputs a copy of the input array representing the state of the
     population at the end of the simulation, in which any infected cells value has been replaced with -1.
    """

    def check_if_valid(x, y):
        if y < 0 or y >= len(population):
            return False
        elif x < 0 or x >= len(population[y]):
            return False
        return True

    if population[y][x] > strength:
        return population
    virus_queue = [(x, y)]
    while virus_queue:
        coords = virus_queue.pop(0)
        if not check_if_valid(coords[0], coords[1]) or population[coords[1]][coords[0]] < 0 or strength < \
                population[coords[1]][coords[0]]:
            continue
        population[coords[1]][coords[0]] = -1
        # up
        virus_queue.append((coords[0], coords[1] - 1))
        # down
        virus_queue.append((coords[0], coords[1] + 1))
        # left
        virus_queue.append((coords[0] - 1, coords[1]))
        # right
        virus_queue.append((coords[0] + 1, coords[1]))
    return population


class MyTestCases(unittest.TestCase):
    def test_answer(self):
        population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
        x = 0
        y = 0
        strength = 2
        self.assertEqual(answer(population, x, y, strength), [[-1, -1, 3], [-1, 3, 4], [3, 2, 1]])
        population = [[9, 3, 4, 5, 4], [1, 6, 5, 4, 3], [2, 3, 7, 3, 2], [3, 4, 5, 8, 1], [4, 5, 4, 3, 9]]
        x = 2
        y = 1
        strength = 5
        self.assertEqual(answer(population, x, y, strength),
                         [[9, -1, -1, -1, -1], [1, 6, -1, -1, -1], [2, 3, 7, -1, -1], [3, 4, 5, 8, -1],
                          [4, 5, 4, 3, 9]])

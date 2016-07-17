import unittest
"""
 Problem 14
 Greedy
"""


def find_two_movies_for_flight(flight_length, movie_lengths):
    find_movie_pairs = {}
    for movie_length in movie_lengths:
        if movie_length in find_movie_pairs:
            return True
        else:
            find_movie_pairs[flight_length-movie_length] = True
    return False


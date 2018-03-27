import unittest
"""
 Problem 14
 Greedy
"""


def find_two_movies_for_flight(flight_length, movie_lengths):
    find_movie_pairs = set()
    for movie_length in movie_lengths:
        if flight_length-movie_length in find_movie_pairs:
            return True
        find_movie_pairs.add(movie_length)
    return False


class MyTestCases(unittest.TestCase):
    def test_find_two_movies_for_flight(self):
        movie_length = [321, 23, 76, 96, 74, 150]
        flight_len = 150
        self.assertTrue(find_two_movies_for_flight(flight_len, movie_length))

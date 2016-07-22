"""
 Problem 21
 bit operators, XOR
"""
import unittest


def find_lost_drone(delivery_confirmation_list):
    val = 0
    for id in delivery_confirmation_list:
        val ^= id
    return val


def dict_find_lost_drone(delivery_confirmation_list):
    ids_seen = {}
    for id in delivery_confirmation_list:
        if id in ids_seen:
            ids_seen.pop(id)
        else:
            ids_seen[id] = True
    return list(ids_seen.keys())[0]


class MyTestCases(unittest.TestCase):
    def test_find_lost_drone(self):
        delivery_id_confirmations = [1, 1, 1, 1, 2, 2, 1, 1, 5, 6, 7, 8, 8, 6, 7]
        self.assertEqual(find_lost_drone(delivery_id_confirmations), 5)
        delivery_id_confirmations = [2, 1, 1]
        self.assertEqual(find_lost_drone(delivery_id_confirmations), 2)

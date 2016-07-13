import unittest

"""
Problem 7
"""


class TempTracker:
    def __init__(self):
        self._max = -1
        self._min = 111
        self._sum = 0
        self._total = 0
        self._highest_recurrence = 0
        self._temperatures_mode = None
        self._temperatures_recorded = {}
        pass

    def insert(self, new_temperature):
        if new_temperature > 110 or new_temperature < 0:
            raise Exception('Inserted temperature {} is out of bounds'.format(new_temperature))
        if new_temperature > self._max:
            self._max = new_temperature
        elif new_temperature < self._min:
            self._min = new_temperature
        self._sum += new_temperature
        self._total += 1
        if new_temperature in self._temperatures_recorded:
            self._temperatures_recorded[new_temperature] += 1
        else:
            self._temperatures_recorded[new_temperature] = 1
        if self._highest_recurrence < self._temperatures_recorded[new_temperature]:
            self._highest_recurrence = self._temperatures_recorded[new_temperature]
            self._temperatures_mode = new_temperature

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def get_mean(self):
        return self._sum / self._total

    def get_mode(self):
        return self._temperatures_mode


class MyTestCases(unittest.TestCase):
    def test_insert(self):
        test_tracker = TempTracker()
        for i in range(25):
            test_tracker.insert(1)
        self.assertEqual(test_tracker.get_mode(), 1)
        self.assertEqual(test_tracker.get_mean(), 1)
        self.assertEqual(test_tracker.get_max(), 1)
        self.assertEqual(test_tracker.get_min(), 1)

import unittest
"""
Problem 4
Greedy
"""


def condense_meeting_times(start_end_times):
    start_end_times.sort(key=lambda start_end_time: start_end_time[0])
    condensed_times = []
    start_time = start_end_times[0][0]
    end_time = start_end_times[0][1]
    # Different possibilities
    # (2,3) (4,5) No overlap
    # (3,5) (3,7) Update end time
    # (1,5) (2,3) Don't update anything

    for start_end_time in start_end_times[1:]:
        if start_time <= start_end_time[0] <= end_time:
            if end_time < start_end_time[1]:
                end_time = start_end_time[1]
        else:
            condensed_times.append((start_time, end_time))
            start_time = start_end_time[0]
            end_time = start_end_time[1]
    condensed_times.append((start_time, end_time))
    return condensed_times


class MyTestCase(unittest.TestCase):
    def test_condense_meeting_times(self):
        meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        self.assertEqual(condense_meeting_times(meeting_times),
                         [(0, 1), (3, 8), (9, 12)])
        meeting_times = [(1, 2), (2, 3)]
        self.assertEqual(condense_meeting_times(meeting_times),
                         [(1, 3)])
        meeting_times = [(1, 5), (2, 3)]
        self.assertEqual(condense_meeting_times(meeting_times),
                         [(1, 5)])
        meeting_times = [(1, 10), (2, 6), (3, 5), (7, 9)]
        self.assertEqual(condense_meeting_times(meeting_times),
                         [(1, 10)])

"""
What if we did have an upper bound on the input values? Could we improve our runtime?
Would it cost us memory?

Could we do this "in-place" on the input list and save some space? What are the pros and cons of doing this in place?
    Deletions would require a linkedlist for easiest deletes. Code complexity would go up.
"""
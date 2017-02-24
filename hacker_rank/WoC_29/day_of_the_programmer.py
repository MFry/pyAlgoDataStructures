import unittest


def day_of_the_programmer(year):
    transition_year = 1918
    if year < 1700 or year > 2700:
        raise Exception("Year out of bounds error")
    if year > transition_year:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            date = '12.09.'
        else:
            date = '13.09.'
    elif year < transition_year:
        if year % 4 == 0:
            date = '12.09.'
        else:
            date = '13.09.'
    else:
        date = '27.09'
    return date + str(year)


class MyTestCases(unittest.TestCase):
    def test_day_of_the_programmer(self):
        self.assertEqual(day_of_the_programmer(2016), '12.09.2016')
        self.assertEqual(day_of_the_programmer(2017), '13.09.2017')


if __name__ == '__main__':
    y = int(input().strip())
    print(day_of_the_programmer(y))

import math


def SchoolAssembly(kids, quantity):
    bags = kids * quantity + 4 * (quantity - 1)
    bags /= 20
    bags = math.ceil(bags)

    return bags


def main():
    solution = 2
    print('Test case 1:', SchoolAssembly(1, 5) == solution)
    solution = 1
    print('Test case 2:', SchoolAssembly(1, 2) == solution)
    solution = 3
    print('Test case 3:', SchoolAssembly(5, 5) == solution)
    solution = 171
    print('Test Case 4:', SchoolAssembly(223, 15) == solution)


if __name__ == '__main__':
    main()

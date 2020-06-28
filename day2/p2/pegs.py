from fractions import Fraction

class Gear():
    def __init__(self, pos):
        self.pos = pos
        self.size = 0

#    def __str__(self):
#        return f'{str(self.pos)}, {str(self.size)}'

def solution(l):
    l = map(Fraction, l)
    if len(l) == 1:
        return -1, -1

    gear_list = []
    for pos in l:
        gear_list.append(Gear(pos))

    x1 = calculate_x1(l)

    if x1 < 2:
        return -1, -1

    # Size of first gear
    gear_list[0].size = x1

    valid, gear_list = create_gear_list(gear_list)
    if not valid:
        return -1, -1
    return gear_list[0].size.numerator, gear_list[0].size.denominator


def works(gear_list):
    total = Fraction(1,1)
    for index in range(len(gear_list)-1):
        total *= Fraction(gear_list[index].size, gear_list[index + 1].size)
    if total == 2:
        return True
    return False


def create_gear_list(gear_list):
    for index in range(len(gear_list)-1):
        length = gear_list[index + 1].pos - gear_list[index].pos
        if length - gear_list[index].size <= 1 or length <= 1:
            return False, gear_list
        gear_list[index + 1].size = length - gear_list[index].size
    return True, gear_list

def calculate_x1(l):
    if len(l) % 2 == 0:
        s = l[len(l)-1] - l[0]
    else:
        s = -l[len(l)-1] - l[0]

    for i in range(1, len(l)-1):
        s += 2 * (-1)**(i+1) * l[i]

    if len(l) % 2 == 0:
        return Fraction(2,3) * s
    else:
        return 2 * s


print(solution([4,17,50]))
print(solution([4,30,50]))

def find_difference(reading):
    differences_list = []
    for num1, num2 in zip(reading, reading[1:]):
        differences_list.append(num2 - num1)

    if len(set(differences_list)) == 1:
        return reading[-1] + differences_list[0]
    else:
        base_value = find_difference(differences_list)
        return reading[-1] + base_value


def mirage_maintenance_1(readings):
    sum = 0

    for line in readings:
        sum += find_difference(line)

    print(sum)


def mirage_maintenance_2(readings):
    sum = 0

    for line in readings:
        sum += find_difference(line[::-1])

    print(sum)


if __name__ == '__main__':
    inp_file = open("oasis", "r")

    readings = []

    for line in inp_file.readlines():
        readings.append([int(n) for n in line.strip().split()])

    mirage_maintenance_1(readings)
    mirage_maintenance_2(readings)

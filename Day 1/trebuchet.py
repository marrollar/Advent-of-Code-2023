import re

translator = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def trebuchet(word_list):
    sum = 0

    for word in word_list:
        found_nums = re.findall('\d', word)

        if len(found_nums) == 1:
            sum += int(found_nums[0], 10) * 10 + int(found_nums[0], 10)
        else:
            sum += int(found_nums[0], 10) * 10 + int(found_nums[-1], 10)

    print(sum)


def trebuchet_2(word_list):
    sum = 0

    for word in word_list:
        found_nums = re.findall('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', word)

        num1 = found_nums[0]
        num2 = found_nums[-1]

        try:
            num1 = translator[num1]
        except KeyError:
            num1 = int(num1)

        try:
            num2 = translator[num2]
        except KeyError:
            num2 = int(num2)

        sum += 10 * num1 + num2

    print(sum)


if __name__ == '__main__':
    inp_file = open("trebuchet", "r")
    inp_list = []

    for line in inp_file.readlines():
        inp_list.append(line.strip())

    # trebuchet(inp_list)
    trebuchet_2(inp_list)

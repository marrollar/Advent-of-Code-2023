from time import perf_counter


def check_adjacent(symbol_row, symbol_ind, numbers_list):
    adj_nums = set()

    for row in range(symbol_row - 1, symbol_row + 2):
        for col in range(symbol_ind - 1, symbol_ind + 2):
            for num_start, num_end, num in numbers_list[row]:
                if num_start <= col <= num_end:
                    adj_nums.add((num_start, num_end, num))

    return adj_nums


def gear_ratios_1(numbers_list, symbols_list):
    ans = 0

    for symbol_row, symbols in enumerate(symbols_list):
        for ind, symbol in symbols:
            adj_nums = check_adjacent(symbol_row, ind, numbers_list)
            for _, _, num in adj_nums:
                ans += num

    print(ans)


def gear_ratios_2(numbers_list, symbols_list):
    ans = 0

    for symbol_row, symbols in enumerate(symbols_list):
        for ind, symbol in symbols:
            if symbol == "*":
                adj_nums = check_adjacent(symbol_row, ind, numbers_list)

                ratio = 1

                if len(adj_nums) > 1:
                    for _, _, num in adj_nums:
                        ratio *= num

                if ratio != 1:
                    ans += ratio

    print(ans)


if __name__ == '__main__':
    inp_file = open("schematic", "r")

    numbers = []
    symbols = []

    for i, line in enumerate(inp_file.readlines()):

        numbers.append([])
        symbols.append([])

        reading_num = False
        current_num = ""

        for j, char in enumerate(line):
            if char.isdigit():
                current_num += char
                reading_num = True
            elif char != '.' and char != '\n':
                symbols[i].append((j, char))
                reading_num = False
            else:
                reading_num = False

            if len(current_num) > 0 and not reading_num:
                numbers[i].append((j - len(current_num), j - 1, int(current_num)))
                current_num = ""

        for start, end, num in numbers[i]:
            assert int(line[start:end + 1]) == num

        for ind, symbol in symbols[i]:
            assert line[ind] == symbol

    start = perf_counter()
    gear_ratios_1(numbers, symbols)
    print(perf_counter() - start)
    start = perf_counter()
    gear_ratios_2(numbers, symbols)
    print(perf_counter() - start)

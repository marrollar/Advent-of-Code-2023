from interval_math import *
import math


def if_you_give_a_seed_a_fertilizer_1(mappings):
    seeds = mappings["seeds"]
    seed_to_soil = mappings["seed-to-soil map"]
    soil_to_fertilizer = mappings["soil-to-fertilizer map"]
    fertilizer_to_water = mappings["fertilizer-to-water map"]
    water_to_light = mappings["water-to-light map"]
    light_to_temperature = mappings["light-to-temperature map"]
    temperature_to_humidity = mappings["temperature-to-humidity map"]
    humidity_to_location = mappings["humidity-to-location map"]

    seed_final_locations = []

    search_order = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                    temperature_to_humidity, humidity_to_location]

    for seed in seeds:
        current_loc = seed

        for current_mapping in search_order:
            for dst, src, rge in current_mapping:
                if src <= current_loc < src + rge:
                    delta = current_loc - src
                    current_loc = dst + delta
                    break

        seed_final_locations.append(current_loc)

    print(min(seed_final_locations))


def if_you_give_a_seed_a_fertilizer_2(mappings):
    seeds = mappings["seeds"]
    seed_to_soil = mappings["seed-to-soil map"]
    soil_to_fertilizer = mappings["soil-to-fertilizer map"]
    fertilizer_to_water = mappings["fertilizer-to-water map"]
    water_to_light = mappings["water-to-light map"]
    light_to_temperature = mappings["light-to-temperature map"]
    temperature_to_humidity = mappings["temperature-to-humidity map"]
    humidity_to_location = mappings["humidity-to-location map"]

    min_seed_loc = math.inf

    search_order = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                    temperature_to_humidity, humidity_to_location]

    for seed_start, seed_range in zip(seeds[0::2], seeds[1::2]):

        current_ranges = [(seed_start, seed_range)]
        new_ranges = []

        for current_mapping in search_order:

            while current_ranges:
                range_start, range_range = current_ranges.pop(0)

                for dst_start, src_start, rge in current_mapping:
                    clamped_interval, split_interval = find_split(range_start, range_range, src_start, rge)

                    if clamped_interval:
                        transformed_start = rescale(clamped_interval[0], src_start, dst_start)

                        range_start = transformed_start
                        range_range = clamped_interval[1]

                        if split_interval:
                            current_ranges.append(split_interval)

                        break

                new_ranges.append((range_start, range_range))

            current_ranges, new_ranges = new_ranges, current_ranges

        for start, interval_range in current_ranges:
            min_seed_loc = min(min_seed_loc, start)

    print(min_seed_loc)


if __name__ == '__main__':
    inp_file = open("almanac", "r")

    mappings = {}

    seed_line = inp_file.readline()
    tokens = seed_line.strip().split(":")

    mappings[tokens[0]] = [int(num) for num in tokens[1].split()]

    last_mapping = ""

    for line in inp_file.readlines():
        line = line.strip()

        if len(line) == 0:
            continue

        if line[0].isalpha():
            tokens = line.split(":")
            mappings[tokens[0]] = []
            last_mapping = tokens[0]

        else:
            mappings[last_mapping].append(tuple(int(num) for num in line.split()))

    import time

    start = time.perf_counter()
    if_you_give_a_seed_a_fertilizer_1(mappings)
    print(time.perf_counter() - start)

    start = time.perf_counter()
    if_you_give_a_seed_a_fertilizer_2(mappings)
    print(time.perf_counter() - start)

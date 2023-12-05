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


def find_split(orig_start, orig_range, src_start, src_range):
    orig_end = orig_start + orig_range
    new_end = src_start + src_range

    if new_end <= orig_end:
        remaining_range = orig_end - new_end
        split_loc = orig_start + (orig_range - remaining_range)

        split_range = split_loc - orig_start
        # orig_start

        return (orig_start, split_range), (split_loc, remaining_range)
    else:
        return (orig_start, orig_range), None


def rescale(orig_start, src_start, dst_start):
    delta = src_start - orig_start
    return dst_start + delta


def if_you_give_a_seed_a_fertilizer_2(mappings):
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

    for seed_start, seed_range in zip(seeds[0::2], seeds[1::2]):

        current_ranges = [(seed_start, seed_range)]
        new_ranges = []

        for current_mapping in search_order:

            while current_ranges:
                range_start, range_range = current_ranges.pop(0)

                for dst_start, src_start, rge in current_mapping:
                    # src_end = src_start + rge
                    #
                    # if src_start <= range_start < src_end:

                        # start_delta = range_start - src_start
                        # split_loc = range_end - src_end
                        #
                        # if split_loc >= 0:
                        #     remaining_range = range_end - split_loc
                        #
                        #     current_ranges.append((split_loc, split_loc + remaining_range))
                        # else:
                        #     new_ranges.append((
                        #         dst_start + start_delta,
                        #         dst_start + start_delta + (range_end - range_start)
                        #     ))

            current_ranges, new_ranges = new_ranges, current_ranges

            # new_ranges.append((start_delta, split_loc))

            #     delta = current_loc - src
            #     current_loc = dst + delta
            #     break

        #     current_seed_set.append(current_loc)
        #
        # seed_final_locations.append(min(current_seed_set))

    print(min(seed_final_locations))


if __name__ == '__main__':
    inp_file = open("almanac_simple", "r")

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

    if_you_give_a_seed_a_fertilizer_1(mappings)
    if_you_give_a_seed_a_fertilizer_2(mappings)

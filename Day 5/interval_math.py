def find_split(src_start, src_range, tgt_start, tgt_range):
    src_end = src_start + src_range  # exclusive
    tgt_end = tgt_start + tgt_range

    overlap_range = overlap((src_start, src_end), (tgt_start, tgt_end))

    if len(overlap_range) == 0:
        return None, None

    if src_start in overlap_range and src_end - 1 in overlap_range:
        return (src_start, src_range), None

    elif src_start < overlap_range[0] < src_end:
        updated_range = overlap_range[0] - src_start
        split_range = src_end - overlap_range[0]

        return (overlap_range[0], split_range), (src_start, updated_range)

    elif src_start <= overlap_range[-1] < src_end:
        updated_range = overlap_range[-1] - src_start + 1
        split_range = src_end - overlap_range[-1] - 1

        return (src_start, updated_range), (overlap_range[-1] + 1, split_range)


def overlap(interval_1, interval_2):
    return range(max(interval_1[0], interval_2[0]), min(interval_1[1], interval_2[1]))


def rescale(orig_start, src_start, dst_start):
    delta = orig_start - src_start
    return dst_start + delta


if __name__ == '__main__':
    print(find_split(0, 10, 9, 10))

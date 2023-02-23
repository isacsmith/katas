def chop(target_int, array_of_ints):
    if len(array_of_ints) == 0:
        return -1

    first_element = array_of_ints[0]
    last_element = array_of_ints[-1]

    if (target_int < first_element) | (target_int > last_element):
        return -1

    array_of_idx = list(range(0, len(array_of_ints)))
    while len(array_of_ints) > 1:
        array_of_ints, array_of_idx = split_list(
            target_int, array_of_ints, array_of_idx
        )

    if array_of_ints[0] == target_int:
        return array_of_idx[0]
    else:
        return -1


def split_list(target_int, array_of_ints, array_of_idx):
    # this assumes the target_int is between the first and last elements of the array_of_ints
    middle_idx = (len(array_of_ints) // 2) + (1 // 2)
    middle_element = array_of_ints[middle_idx]

    if target_int < middle_element:
        return array_of_ints[:middle_idx], array_of_idx[:middle_idx]
    else:
        return array_of_ints[middle_idx:], array_of_idx[middle_idx:]

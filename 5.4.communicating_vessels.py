def interleave(*args):
    """
    Interleave multiple iterables of possibly different lengths.

    Parameters:
    *args: any number of iterables (e.g., lists, tuples, strings)

    Returns:
    res: list containing the interleaved elements from the input iterables
    """
    max_len = max(len(lst) for lst in args)
    res = []
    for i in range(max_len):
        for lst in args:
            if i < len(lst):
                res.append(lst[i])
    return res


def interleave_generator(*args):
    """
    Interleave multiple iterables of possibly different lengths using a generator.

    Parameters:
    *args: any number of iterables (e.g., lists, tuples, strings)

    Yields:
    elements from the input iterables interleaved
    """
    max_len = max(len(lst) for lst in args)
    for i in range(max_len):
        for lst in args:
            if i < len(lst):
                yield lst[i]


if __name__ == "__main__":
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    for value in interleave_generator('abc', [1, 2, 3], ('!', '@', '#')):
        print(value)

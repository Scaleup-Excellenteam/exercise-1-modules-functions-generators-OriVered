def join(*lists, sep='-'):
    """
    Join multiple lists with an optional separator.

    Args:
        *lists: A variable number of lists to join.
        sep (str, optional): The separator to insert between lists. Defaults to '-'.

    Returns:
        list: A single list composed of all input lists with the separator inserted between them.
        None: If no lists are provided as input.
    """
    if not lists:
        return None
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(sep)
    return result


if __name__ == "__main__":
    result1 = join([1, 2], [8], [9, 5, 6], sep='@')
    print(result1)  # Output: [1, 2, '@', 8, '@', 9, 5, 6]

    result2 = join([1, 2], [8], [9, 5, 6])
    print(result2)  # Output: [1, 2, '-', 8, '-', 9, 5, 6]

    result3 = join([1])
    print(result3)  # Output: [1]

    result4 = join()
    print(result4)  # Output: None
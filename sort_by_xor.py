# v0.0.1

def sort_by_xor(*t):
    """
    Get an iterable full of strings.
    Return a sorted list by:
        - length in descending order,
        - alphabet in ascending order.
        (since the two parameters order
        in opposite directions, 'xor' seemed
        a good name.)
    """
    from collections import defaultdict
    dd = defaultdict(list)
    for string in t:
        dd[len(string)].append(string)
    result = []
    for key in sorted(dd, reverse=True):
        result.extend(sorted(dd[key]))
    return result

# testing sort_by_word_length_xor
if sort_by_xor('gray', 'green', 'brown', 'red', 'blue') == ['brown', 'green', 'blue', 'gray', 'red']:
    print("sorting has succeeded for request!")
else:
    print("please check code")

from collections.abc import Iterable as IterableClass
from collections import Counter
from typing import Any, Dict, Iterable


def f(s):
    """
    This function counts the frequency of the elements present in the iterable `s`.

    Args:
        s (iterable): This is an iterable that is provided.

    Returns:
        dict: A dict containing the elements of `s` and the frequencies as values.
    """
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r

def count_frequency(s: Iterable[Any]) -> Dict[Any, int]:
    """
    This function counts the frequency of the elements present in the iterable `s`.

    Args:
        s (iterable): This is an iterable that is provided.

    Returns:
        dict: A dict containing the elements of `s` and the frequencies as values.
    """
    if not isinstance(s, IterableClass):
        raise TypeError("Input must be an iterable")

    return Counter(s)


if __name__ == "__main__":
    print("Original------>", f("malayalam"))
    print("Modified------>", count_frequency("malayalam"))

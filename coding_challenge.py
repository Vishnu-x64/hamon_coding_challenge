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

    # return dict(Counter(s))  # simplest way

    r: Dict[Any, int] = {}
    for i in s:
        if i in r:
            r[i] += 1
            continue
        r[i] = 1
    return r


if __name__ == "__main__":
    # Things I did to improve the original function
    # 1. gave a proper name to the function for readability
    # 2. added type hints for the args and specified the return
    # 3. input type checking added
    # 4. removed the else statement to reduce the code.
    print("Original------>", f("malayalam"))
    print("Modified------>", count_frequency("malayalam"))

from collections import defaultdict
from typing import Any, Callable, Iterable, Dict
from Data.Example import Example


def argmax(f: Callable[[Any], Any], args: Iterable[Any]) -> Any:
    """
    :param f: a callable function.
    :param args: an iterable for the arguments.
    :return: the argument (in the args iterable) that returns the maximum value from the function f.
    """
    return max([(arg, f(arg)) for arg in args], key=lambda tup: tup[1])[0]


def count_attribute(examples: Iterable[Example], attribute: str) -> Dict[str, int]:
    """
    :param examples: an iterable of examples/
    :param attribute: an attribute.
    :return: a dictionary between the attribute's value and the number of examples that have this value
    """
    counter: Dict[str, int] = defaultdict(int)

    for e in examples:
        counter[e[attribute]] += 1

    return counter


def multiply(lst: Iterable[float]) -> float:
    """
    :return: Multiply elements one by on.
    """
    result = 1
    for x in lst:
        result = result * x
    return result

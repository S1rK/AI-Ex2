from collections import defaultdict
from typing import Any, Callable, Iterable, Dict
from Data.Example import Example


def argmax(f: Callable[[Any], Any], args: Iterable[Any]) -> Any:
    return max([(arg, f(arg)) for arg in args], key=lambda tup: tup[1])[0]


def count_attribute(examples: Iterable[Example], attribute: str) -> Dict[str, int]:
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

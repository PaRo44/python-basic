import enum


class FilterTypes(enum.Enum):
    EVEN = 0
    ODD = 1
    PRIME = 2


def is_prime(num: int) -> bool:
    res = True
    for d in range(2, num):
        if num % d == 0:
            res = False
            break
    return res


def filter_numbers(numbers: list[int], filter_type: FilterTypes) -> list[int]:
    if filter_type == FilterTypes.ODD:
        res = list(filter(lambda num: num % 2 == 1, numbers))
    elif filter_type == FilterTypes.EVEN:
        res = list(filter(lambda num: num % 2 == 0, numbers))
    elif filter_type == FilterTypes.PRIME:
        res = list(filter(is_prime, numbers))
    return res
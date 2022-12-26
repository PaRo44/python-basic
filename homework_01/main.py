
ODD = 1
EVEN = 0
PRIME = 2


def is_prime(num: int) -> bool:
    res = True
    for d in range(2, num):
        if num % d == 0:
            res = False
            break
    return res


def filter_numbers(numbers: list[int], filter_type) -> list[int]:
    if filter_type == ODD:
        res = list(filter(lambda num: num % 2 == 1, numbers))
    elif filter_type == EVEN:
        res = list(filter(lambda num: num % 2 == 0, numbers))
    elif filter_type == PRIME:
        res = list(filter(is_prime, numbers))
    return res

def is_armstrong(number: int) -> bool:
    num_degree = lambda a: int(a) ** len(str(number))
    sum_degree = sum(map(num_degree, str(number)))
    if sum_degree == number:
        return True
    else:
        return False
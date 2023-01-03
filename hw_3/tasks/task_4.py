def is_armstrong(number: int) -> bool:
    num_degree = lambda a: int(a) ** len(str(number))
    sum_degree = sum(map(num_degree, str(number)))
    if sum_degree == number:
        print('Is Armstrong number')
    else:
        print('Is not Armstrong number')
    return sum_degree


is_armstrong(153)
is_armstrong(12)
is_armstrong(10)
is_armstrong(9)
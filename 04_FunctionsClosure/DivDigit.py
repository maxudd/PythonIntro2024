"""
Цифроделители

Написать функцию divdigit(N), которой передаётся произвольное
натуральное число N, а в ответ функция возвращает количество
цифр этого числа, являющихся её делителями.
"""


def divdigit(num):
    numcopy = num
    counter = 0
    while numcopy:
        digit = numcopy % 10
        if digit and not num % digit:
            counter += 1
        numcopy //= 10
    return counter


print(divdigit(312345))  # --> 4

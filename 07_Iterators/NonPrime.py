"""
Непростые числа

Написать генетатор-функцию nonprime(n=0), которая будет выдавать
последовательность непростых чисел (единица и составные числа),
превосходящих целое положительное n (по умолчанию — 0).
"""

def nonprime(n=0):
    if not n: 
        yield 1
    n += 1
    while True:
        for i in range(2, int(n**0.5)+1):
            if not n % i:
                yield n
                break
        n += 1


# print(*dict(zip(nonprime(16), range(20))))
# print(*dict(zip(nonprime(), range(20))))
# print(*dict(zip(nonprime(1000), range(20))))
# print(max(dict(zip(nonprime(1000), range(1000)))))
# from itertools import takewhile
# print(max(takewhile(lambda x: x % 11111, nonprime(1000))))
# print(next(nonprime(25000)))
# print(max(takewhile(lambda x: x ^ 25000, nonprime())))
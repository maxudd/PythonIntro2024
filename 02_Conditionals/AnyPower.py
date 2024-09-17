"""
Какая-нибудь степень

Ввести небольшое натуральное число 2⩽N⩽1000000 и проверить, является ли оно
степенью натурального числа (>1). Вывести YES или NO соответственно.
"""

num = int(input())

flag = False
for i in range(2, num):
    num1 = num
    while num1 != 1:
        ost = num1 % i
        if ost and not flag:
            break
        elif ost and flag:
            num1 = num
            break
        else:
            flag = True
            num1 = num1 // i
    else:
        print('YES')
        break
else:
    print('NO')

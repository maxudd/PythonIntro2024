"""
Нечестный квайн

Написать функцию quine(), которая возвращает строку, содержащую её собственный
исходный текст на Python, то есть работает как квайн. Однако эта функция
квайном не является, потому что получает свой исходный текст с помощью
inspect.
"""


def quine():
    import inspect
    return inspect.getsource(quine)

# res = quine()
# exec(res, None, namespace := {})
# print(namespace['quine'].__code__.co_code == quine.__code__.co_code)

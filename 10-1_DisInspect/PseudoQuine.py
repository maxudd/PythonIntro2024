def quine():
    import inspect
    return inspect.getsource(quine)

# res = quine()
# exec(res, None, namespace := {})
# print(namespace['quine'].__code__.co_code == quine.__code__.co_code)
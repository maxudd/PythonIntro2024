import ast
import copy

macroses = dict()

class Trans(ast.NodeTransformer):
    subst = dict()
    def visit_Call(self, node):
        if node.func.id in macroses:
            macro_fun = copy.deepcopy(macroses[node.func.id]) 
            macro_args = [x.arg for x in macro_fun.body[0].args.args]
            # num_args = len(macro_args)
            macro_body = macro_fun.body[0].body[0].value
            # for i in range(num_args):
            # print(macro_args)
            self.subst = dict(zip(macro_args, node.args))
            new_macro_body = self.visit(macro_body)
            # print(ast.dump(macro_body, indent=2))
            # print(ast.unparse())
            return new_macro_body
        return node

    def visit_Name(self, node):
        if node.id in self.subst:
            return self.subst[node.id]
        return node


class macro:
    import inspect

    def __init__(self, *args):
        if not args: # если args нет значит мы сюда попали из @macro()
            pass 
        else: # иначе мы попали из @macro, то есть args[0] - это декорируемая функция
            macrofun = args[0]
            self.fun = macrofun
            src = self.inspect.getsource(macrofun)
            src_parsed = ast.parse(src)
            src_parsed.body[0].decorator_list = []
            # print(ast.dump(src_parsed, indent=2))
            macroses[macrofun.__name__] = src_parsed

    def __call__(self, *args):
        if args and callable(fun := args[0]): # сюда попадаем из @macro(), единственный параметр - функция
            fun = args[0]
            # self.fun = fun
            src = self.inspect.getsource(fun)
            src_parsed = ast.parse(src)
            src_parsed.body[0].decorator_list = []
            # print(ast.dump(src_parsed, indent=2))
            src_updated = Trans().visit(src_parsed)
            # src_updated.body[0].name = 'wrapper'
            # print(ast.unparse(src_updated))
            scope = dict()
            exec(ast.unparse(src_updated), scope)
            return scope['calculate']
        else: # сюда попадаем из вызова задекорированной функции
            return self.fun(*args)

# @macro
# def sum3(a, b, c):
#     return a * b + c


# @macro()
# def calculate(x, y):
#     w = x + y
#     return sum3(w + x, y, x * y)


# print(calculate(2, 3), sum3(2, 3, 4))
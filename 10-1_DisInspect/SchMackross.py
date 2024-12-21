"""
Макросы-Шмакросы

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_SchMackross
"""

import inspect
import ast
import copy
import dis  # не нужно, но без этого не работали тесты

macroses = dict()


class Trans(ast.NodeTransformer):

    subst = dict()

    def visit_Call(self, node):
        if node.func.id in macroses:
            mfun = copy.deepcopy(macroses[node.func.id])
            margs = [x.arg for x in
                     mfun.body[0].args.posonlyargs + mfun.body[0].args.args]
            macro_body = mfun.body[0].body[0].value
            self.subst = dict(zip(margs, node.args))
            new_macro_body = self.visit(macro_body)
            self.subst = dict()
            return new_macro_body
        return node

    def visit_Name(self, node):
        if node.id in self.subst:
            return self.subst[node.id]
        return node


class macro:
    def __init__(self, *args):
        if not args:
            # если args нет значит мы сюда попали из @macro()
            pass
        else:
            # иначе мы попали из @macro, т.е. args[0] это декорируемая функция
            macrofun = args[0]
            self.fun = macrofun
            src = inspect.getsource(macrofun)
            src_parsed = ast.parse(src)
            src_parsed.body[0].decorator_list = []
            macroses[macrofun.__name__] = src_parsed

    def __call__(self, *args):
        if args and callable(fun := args[0]):
            # сюда попадаем из @macro(), единственный параметр - функция
            src = inspect.getsource(fun)
            src_parsed = ast.parse(src)
            src_parsed.body[0].decorator_list = []
            src_updated = Trans().visit(src_parsed)
            scope = dict()
            exec(ast.unparse(src_updated), scope)
            return scope[src_updated.body[0].name]
        else:  # сюда попадаем из вызова задекорированной функции
            return self.fun(*args)

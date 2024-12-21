"""
Деление последовательностей

Написать программу (внимание! это именно программа, а не функция или класс),
входные данные для которой — это текст на ЯП Python. Этот текст следует
выполнить с помощью exec(), предварительно заменив в нём операцию
целочисленного деления «//» на более «продвинутую», которая применима также
к конечным индексируемым последовательностям и возвращает соответствующую долю
этой последовательности, начиная с нулевого элемента. Операцию «//=»
реализовывать не надо.
"""


import ast
from copy import deepcopy
import sys

strr = sys.stdin.read()

fun = '(lambda x, y: x[:len(x)//y] if hasattr(x, "__getitem__") else x // y)'

new_div = ast.parse(fun).body[0].value


class MyOptimizer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        if isinstance(node.op, ast.FloorDiv):
            return ast.Call(func=deepcopy(new_div),
                            args=[node.left, node.right],
                            keywords=[])
        return node


tree = ast.parse(strr)
opt = MyOptimizer()

tree = opt.visit(tree)

res = ast.unparse(tree)
exec(res)

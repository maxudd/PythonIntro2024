import ast
from copy import deepcopy
import sys

strr = sys.stdin.read()

new_div = ast.parse('(lambda x, y: x[:len(x)//y] if hasattr(x, "__getitem__") else x // y)').body[0].value

class MyOptimizer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        if isinstance(node.op, ast.FloorDiv):
            return ast.Call(func=deepcopy(new_div), args=[node.left, node.right], keywords=[])
        return node

tree = ast.parse(strr)
opt = MyOptimizer()

tree = opt.visit(tree)

res = ast.unparse(tree)
exec(res)
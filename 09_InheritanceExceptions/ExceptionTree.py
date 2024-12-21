"""
Дерево исключений

Написать класс ExceptionTree, экземпляр которого конструирует
объекты-исключения, иерархия которых соответствует двоичному дереву:

                     Exception-1
                    /           |
          Exception-2            Exception-3
          /         |           /          |
    Exception-4 Exception-5 Exception-6 Exception-7
и т. д.

Единственный параметр при вызове экземпляра — индекс исключения в этом
дереве. Индекс хранится также в самом исключении в виде поля .n.
"""


class ExceptionTree:

    tree = dict()

    def __init__(self):
        self.tree[1] = type('ex-1', (Exception,), {'n': 1})

    def _create_exception_class(self, i):
        if i not in self.tree:
            if i == 1:
                base_class = self.tree[0]
            else:
                parent_index = i // 2
                parent_class = self._create_exception_class(parent_index)
                base_class = parent_class

            new_exc = type(f"ex-{i}", (base_class, ), {'n': i})
            self.tree[i] = new_exc

        return self.tree[i]

    def __call__(self, i):
        return self._create_exception_class(i)

# etree = ExceptionTree()
# excs = [etree(i) for i in (1, 2, 5, 12, 20)]
# for Ethrow in excs:
#     print(f"Throw {Ethrow.n}", end="")
#     for Ecatch in excs:
#         if Ethrow != Ecatch:
#             try:
#                 raise Ethrow
#             except Ecatch:
#                 print(f", {Ecatch.n} caught", end="")
#             except Exception:
#                 print(f", {Ecatch.n} missed", end="")
#     print()

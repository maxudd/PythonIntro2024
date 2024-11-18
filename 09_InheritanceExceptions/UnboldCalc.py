"""Надёжный калькулятор

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_UnboldCalc
"""

import re

namespace = dict()

while line := input():
    if not line.startswith('#'):
        res = re.search(r"^(([^\s=]+)\s*=\s*)?(.+)", line)
        if not res:
            print('Syntax error')
        else:
            _, g2, g3 = res.groups()
            if g2:
                if g2.isidentifier():
                    try:
                        value = eval(g3, {'__builtins__': {}}, namespace)
                        namespace[g2] = value
                    except NameError:
                        print('Name error')
                    except SyntaxError:
                        print('Syntax error')
                    except:
                        print('Runtime error')
                else:
                    print('Assignment error')
            else:
                try:
                    value = eval(g3, {'__builtins__': {}}, namespace)
                    print(value)
                except NameError:
                    print('Name error')
                except SyntaxError:
                    print('Syntax error')
                except:
                    print('Runtime error')

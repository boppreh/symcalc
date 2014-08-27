from sympy.abc import *
from sympy.core.symbol import Symbol

while True:
    try:
        line = input('')
        print()
        if '=' in line:
            exec(line)
        else:
            _ = eval(line)
            print(_)
    except EOFError:
        continue
    except Exception as e:
        print('Error:', e)

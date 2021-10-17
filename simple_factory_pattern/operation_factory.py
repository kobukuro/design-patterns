from operation import *


# 根據傳入的符號，回傳對應的Operation instance
def create_operate(operate):
    operation = None
    if operate == '+':
        operation = OperationAdd()
    elif operate == '-':
        operation = OperationSub()
    return operation

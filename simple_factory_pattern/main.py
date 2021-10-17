from OperationFactory import *

if __name__ == '__main__':
    operation = create_operate(operate='+')
    operation.number_a = 1
    operation.number_b = 2
    print(operation.get_result())

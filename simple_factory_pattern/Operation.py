from abc import ABCMeta, abstractmethod


class Operation(metaclass=ABCMeta):
    number_a = 0
    number_b = 0

    @abstractmethod
    def get_result(self):
        result = 0
        return result


class OperationAdd(Operation):

    def get_result(self):
        result = self.number_a + self.number_b
        return result


class OperationSub(Operation):

    def get_result(self):
        result = self.number_a - self.number_b
        return result

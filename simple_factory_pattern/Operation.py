class Operation(object):
    number_a = 0
    number_b = 0

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

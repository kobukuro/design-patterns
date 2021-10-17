from strategy_pattern.strategy.strategy import Strategy
from typing import List

"""
Concrete Strategies implement the algorithm while following the base strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))

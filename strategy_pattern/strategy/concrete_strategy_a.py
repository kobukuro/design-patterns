from strategy_pattern.strategy.strategy import Strategy
from typing import List

"""
Concrete Strategies implement the algorithm while following the base strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    """
    The strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass

from abc import ABC
from abc import abstractmethod
class Step(ABC):
    def __init__(self):
        pass


class StepException(Exception):
    pass

    @abstractmethod
    def process(self, data, inputs, utils):
        pass
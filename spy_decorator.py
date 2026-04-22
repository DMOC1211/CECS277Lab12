'''
'''

from abc import ABC
from spy import Spy


class SpyDecorator(Spy, ABC):
    """
    Base decorator class for Spy objects.
    Wraps another Spy and forwards all stat methods.
    """

    def __init__(self, s: Spy):
        self._spy = s

    def description(self):
        return self._spy.description()

    def agility(self):
        return self._spy.agility()

    def stealth(self):
        return self._spy.stealth()

    def tech_ability(self):
        return self._spy.tech_ability()

'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/22/26
Group: 10
Description: Creates the class that is the base class for all spy objects
'''

from abc import ABC
from spy import Spy


class SpyDecorator(Spy, ABC):
    
    
    #Wraps another Spy and forwards all stat methods.
    

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

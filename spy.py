'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/22/26
Group: 10
Description: Creates the spy base class and returns the spy's traits after the gadgets stats are added.
'''

import abc

class Spy(abc.ABC):

    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def agility(self):
        pass

    @abc.abstractmethod
    def stealth(self):
        pass

    @abc.abstractmethod
    def tech_ability(self):
        pass


    def __str__(self):
        return f"{self.description()}:  \nAgility: {self.agility()}, Stealth: {self.stealth()}, Tech: {self.tech_ability()}"

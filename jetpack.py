'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/22/26
Group: 10
Description: Creates the jetpack gadget for the spy 
'''

from spy_decorator import SpyDecorator

class Jetpack(SpyDecorator):
    """Adds agility +3, stealth –1, tech +1"""

    def description(self):
        return self._spy.description() + " + Jetpack"

    def agility(self):
        return super().agility() + 3

    def stealth(self):
        return super().stealth() - 1

    def tech_ability(self):
        return super().tech_ability() + 1

'''
'''

from spy_decorator import SpyDecorator



class Lockpick(SpyDecorator):
    """Adds agility +1, stealth +2, tech +0"""

    def description(self):
        return self._spy.description() + " + Lockpick"

    def agility(self):
        return super().agility() + 1

    def stealth(self):
        return super().stealth() + 2

    def tech_ability(self):
        return super().tech_ability()
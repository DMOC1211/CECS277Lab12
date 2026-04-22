'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/22/26
Group: 10
Description: Creates the goggles gadget for the spy
'''


from spy_decorator import SpyDecorator


class Goggles(SpyDecorator):
    """Adds agility +0, stealth +2, tech +1"""

    def description(self):
        return self._spy.description() + " + Goggles"

    def agility(self):
        return super().agility()

    def stealth(self):
        return super().stealth() + 2

    def tech_ability(self):
        return super().tech_ability() + 1

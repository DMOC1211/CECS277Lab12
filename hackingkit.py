'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/22/26
Group: 10
Description: Creates the hacking kit gadget for the spy
'''

from spy_decorator import SpyDecorator

class HackingKit(SpyDecorator):
    """Adds agility –1, stealth –1, tech +3"""

    def description(self):
        return self._spy.description() + " + Hacking Kit"

    def agility(self):
        return super().agility() - 1

    def stealth(self):
        return super().stealth() - 1

    def tech_ability(self):
        return super().tech_ability() + 3

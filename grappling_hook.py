'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/22/26
Group: 10
Description: Creates the Grappling hook gadget made from the base of the spy_decorator class.
'''

from spy_decorator import SpyDecorator

class GrapplingHook(SpyDecorator):
    ##Adds agility +2, stealth +1, tech +0

    def description(self):
        return self._spy.description() + " + Grappling Hook"

    def agility(self):
        return super().agility() + 2

    def stealth(self):
        return super().stealth() + 1

    def tech_ability(self):
        return super().tech_ability() + 0

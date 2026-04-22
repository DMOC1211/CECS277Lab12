'''
'''

from spy_decorator import SpyDecorator


class GrapplingHook(SpyDecorator):

    def description(self):
        return self._spy.description() + " + Grappling Hook"

    def agility(self):
        return super().agility() + 2

    def stealth(self):
        return super().stealth() + 1

    def tech_ability(self):
        return super().tech_ability() + 0

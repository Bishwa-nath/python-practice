<<<<<<< HEAD
class Spell(object):
    def __init__(self, incantation, name):
        self.incantation = incantation
        self.name = name

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


def studySpell(spell):
    print(spell)


spell = Accio()
print(spell.execute())
studySpell(spell)
=======
class Spell(object):
    def __init__(self, incantation, name):
        self.incantation = incantation
        self.name = name

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


def studySpell(spell):
    print(spell)


spell = Accio()
print(spell.execute())
studySpell(spell)
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
studySpell(Confundo())
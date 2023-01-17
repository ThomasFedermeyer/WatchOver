
class Character:

    def __init__(self):
        self.number = 0
        self.UltMax = 2240
        self.currentUlt = 0
        self.gameTime = 0
        self.lastUltTime = 0
        self.Healing = 0
        self.Damage = 0

    def calcCurrentUlt(self):
        gamediff = self.gameTime - self.lastUltTime
        ultCharge = Healing + Damage+ gamediff*4
        currentUlt = ultCharge / UltMax


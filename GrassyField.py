import random
from PMIndex import PMIndex

class GrassyField(object):
    PM_LIST = PMIndex("pm.csv")

    @staticmethod
    def getRandomPocketMonster(rarity):
        if random.randint(1, 10) % 3 == 0:
            type = random.choice(PMIndex.TYPES)
            monster = random.choice(GrassyField.PM_LIST.getMonsterType(type))
            if monster.getRarity() <= rarity:
                return monster
            else:
                return None
        else:
            return None


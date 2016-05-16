waitCount = 0 #How long we've waited for enemy hero to come to us
hidingOrSeeking = "hiding"

def moveMe(x,y):
    hero.moveXY(x, y)

#Go hide behind the traps, see if we can get them to do some work for us
moveMe(58, 25)
moveMe(64, 25)
moveMe(64, 22)

#  Cleave is pointless really as strongers swords (Which 
# are needed for a decent win rate) have no cleave function
def attack(enemy):
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else if hero.distanceTo(enemyHero) < 5:
        hero.attack(enemy)
        
    if hidingOrSeeking == "hiding":
        moveMe(63, 16)

loop:
    enemyHero = hero.findNearestEnemy()    
    hero.electrocute(enemyHero)
    if enemyHero != None and hero.distanceTo(enemyHero) < 9:
        attack(enemyHero)
        waitCount = 0
    else:
        waitCount += 1
        
    #Been hiding too long, go to enemy hero
    if waitCount > 10:
        hero.moveXY(64, 25)
        loop:
            hidingOrSeeking = "seeking"
            hero.attack(enemyHero)
    else:
        hero.say("I'm waiting..." + waitCount)

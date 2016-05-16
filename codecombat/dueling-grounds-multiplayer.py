waitCount = 0 #How long we've waited for enemy hero to come to us
hidingOrSeeking = "hiding"

def moveMe(x,y):
    hero.moveXY(x, y)

moveMe(58, 25)
moveMe(64, 25)
moveMe(64, 22)

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
        
    
    #Been waiting too long, go to enemy hero
    if waitCount > 10:
        hero.moveXY(64, 25)
        loop:
            hidingOrSeeking = "seeking"
            hero.attack(enemyHero)
    else:
        hero.say("I'm waiting..." + waitCount)

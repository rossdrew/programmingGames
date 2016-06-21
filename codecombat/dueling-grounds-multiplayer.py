waitCount = 0 #How long we've waited for enemy hero to come to us
hidingOrSeeking = "hiding"

hero.moveXY(58, 25)
hero.moveXY(64, 25)
hero.moveXY(64, 22)

def attack(enemy):
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    elif hero.isReady("bash"):
        hero.bash(enemy)
    elif hero.distanceTo(enemyHero) < 5:
        if hero.isReady("bash"):
            hero.bash(enemyHero)
        else:
            hero.attack(enemy)
        
    if hidingOrSeeking == "hiding":
        hero.moveXY(63, 14)

loop:
    enemyHero = hero.findNearestEnemy()    
    #hero.electrocute(enemyHero)
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
                if hero.isReady("bash"):
                    hero.bash(enemyHero)
                else:
                    hero.attack(enemy)
        else:
            hero.say("I'm waiting..." + waitCount)

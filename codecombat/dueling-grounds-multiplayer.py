waitCount = 0 #How long we've waited for enemy hero to come to us
hidingOrSeeking = "hiding"

hero.bash(hero.findNearestEnemy())
hero.electrocute(hero.findNearestEnemy())
hero.moveXY(58, 25)
hero.moveXY(64, 25)
hero.moveXY(64, 22)

def attack(enemy):
    if hero.distanceTo(enemy) < 5:
        if hero.isReady("bash"):
            hero.bash(enemy)
            hero.electrocute(enemy)
        else:
            hero.attack(enemy)
    elif hero.distanceTo(enemy) < 30:
        if hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
        
    if hidingOrSeeking == "hiding":
        hero.moveXY(63, 14)

loop:
    enemyHero = hero.findNearestEnemy()    
    if enemyHero != None:
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
            hero.say(waitCount + " one thousand")

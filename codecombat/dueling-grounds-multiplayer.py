#TODO needs a wait timer, so if the enemy does nothing, we go get him

def move(x,y, enemy):
    if enemy != None and hero.distanceTo(enemy) < 5:
        hero.attack(enemy)
    hero.moveXY(x, y)
    
enemy = hero.findNearestEnemy()

hero.electrocute(enemy)
#move(57, 25)
move(63, 25)
move(64, 21)

loop:
    enemy = hero.findNearestEnemy()
    if enemy != None and hero.distanceTo(enemy) < 5:
        hero.attack(enemy)  
        hero.moveXY(64, 15)
    
    if hero.distanceTo(enemy) > 60:
        hero.say("Fight, Coward!")
        hero.moveXY(63, 26)
        hero.moveXY(12, 39)
        loop:
            hero.attack(enemy)

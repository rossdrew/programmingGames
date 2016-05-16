#Attack the enemy if he comes close but otherwise, collect coins
loop:
    enemy = self.findNearest(self.findEnemies())
    item = self.findNearest(self.findItems())
    
    if enemy != None:
        if self.distanceTo(enemy) < 5:
            self.attack(enemy)
        else:
            self.electrocute(enemy)
    else if item != None:
        self.moveXY(item.pos.x, item.pos.y)

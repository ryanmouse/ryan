from mcpi.minecraft import Minecraft 
import random 
import time
mc = Minecraft.create()
x,y,z, = mc.player.getTilePos()
for j in range(3):
    time.sleep(5)
    for i in range(5):
        r = random.randint(1,6)
        if r == 1:
            mc.setBlocks(x,y,z,x,y,z+4,1)
            x = x+4
        elif r == 2:
            mc.setBlocks(x,y,z,x,y,z-4,1)
            x = x-4
        elif r == 3:
            mc.setBlocks(x,y,z,x,y,z+4,1)
            z = z+4
        elif r == 4:
            mc.setBlocks(x,y,z,x,y,z-4,1)
            z = z-4
        elif r == 5:
            mc.setBlocks(x,y,z,x,y+4,z,1)
            y = y+4
        else:
            mc.setBlocks(x,y,z,x,y-4,z,1)
            y = y-4
        

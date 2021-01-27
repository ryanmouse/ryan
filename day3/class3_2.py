from mcpi.minecraft import Minecraft
import random
import time
mc =Minecraft.create()
x,y,z = mc.player.getPos()
while True:
    time.sleep(1)
    x = x+random.uniform(-20,20)  #random.randint()
    y = y+random.uniform(-20,20)
    z = z+random.uniform(-20,20)
    mc.spawnEntity(x,y,z,63)
    

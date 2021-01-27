from mcpi.minecraft import Minecraft as mc
import time
import random
time.sleep(3)
mcs = mc.create()
x,y,z = mcs.player.getTilePos()
w=6
h=6
while True:
    color = random.randint(1,15)
    time.sleep(0.2)
    mcs.setBlocks(x+8,y+20,z+8,x-8,y+20,z-8,20)
    mcs.setBlocks(x+w,y+h+21,z+w,x-w,y+21,z-w,95,color)
    mcs.setBlocks(x+w-1,y+h+21-1,z+w-1,x-w+1,y+21,z-w+1,0)
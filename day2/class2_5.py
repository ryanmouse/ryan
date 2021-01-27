from mcpi.minecraft import Minecraft as mc
import time
import random
mcs = mc.create()
while True:
    color = random.randint(1,15)
    x,y,z = mcs.player.getTilePos()
    a = mcs.getBlock(x+1,y-1,z)
    b = mcs.getBlock(x-1,y-1,z)
    c = mcs.getBlock(x,y-1,z+1)
    d = mcs.getBlock(x,y-1,z-1)
    if a == 0 or a == 0 or b == 0 or b == 0 \
    or c == 0 or c == 0 or d == 0 or d == 0:
      mcs.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,95,color)
    time.sleep(0.03)









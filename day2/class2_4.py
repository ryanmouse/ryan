from mcpi.minecraft import Minecraft as mc
import time
time.sleep(3)
mcs = mc.create()
while True:
    x,y,z=mcs.player.getPos()
    mcs.setBlock(x,y+2,z,8)
    time.sleep(3)
from mcpi.minecraft import Minecraft as mc
import time
mcs = mc.create()
x,y,z = mcs.player.getTilePos()
while True:
    x,y,z = mcs.player.getTilePos()
    mcs.postToChat("You are located on X :"+str(x)+\
                   ',Y:'+str(y)+",Z: "+str(z))
    time.sleep(0.5)
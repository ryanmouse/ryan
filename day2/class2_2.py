from mcpi.minecraft import Minecraft as mc
import time
time.sleep(3)
mcs = mc.create()
x,y,z = mcs.player.getTilePos()
s = 2
mcs.setBlocks(x+1,y+s,z+1,x-1,y+s,z-1,20)
mcs.player.setTilePos(x,y+3,z)
mcs.setBlocks(x+s,y-1,z+s,x-s,y+1,z-s,11)
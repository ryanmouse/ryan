from mcpi.minecraft import Minecraft 
from random import randint
import time
mc = Minecraft.create()
x,y,z, = mc.player.getTilePos()
com = randint(0,15)
for i in range(20):
    for j in range(20):
        color = randint(0,15)
        mc.setBlock(x+i,y-1,z+j,11,color)
        
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data == com:
            mc.postToChat("You are good")
            break 
        else:
            mc.postToChat("Try again")
            
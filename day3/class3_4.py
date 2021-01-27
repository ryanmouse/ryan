from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
def planttree(x,y,z,mc,c,t):
    mc.setBlocks(x-1,y+4,z-1,x+1,y+7,z+1,c,5)
    mc.setBlocks(x,y,z,x,y+4,z,t)
    
for i in range(5): 
    planttree(x+i*5,y,z,mc,46,11)
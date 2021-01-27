from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
print(mcs.player.getTilePos())
x = -30
y = 85
z =-21
mcs.player.setTilePos(x,y,z)



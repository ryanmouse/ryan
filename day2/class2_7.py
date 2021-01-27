from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
userName = input('What\'s your name?')
message = input("What\'s your message?") 
mcs.postToChat("[ " +userName+" ]"+message)
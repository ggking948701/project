from mcpi.minecraft import Minecraft 
import time
mc= Minecraft.create()

while True:
    x,y,z =mc.player.getTilePos()
    mc.postToChat("你好x:"+str(x)+"Y:"+str(Y)+"Z:"+str(Z))
    timesleep(1)
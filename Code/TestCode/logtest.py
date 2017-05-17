#coding:utf-8
import time

MyLogFile = "MyLog.txt"

def SENDTOLOG(PassedText):
    f = open(MyLogFile,"a") #opens file 
    WrittenText = time.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M:%S")  + " " + PassedText + "\n"
    f.write(WrittenText)
    f.close()
    return

SENDTOLOG("ooooooooooooooooooooo")
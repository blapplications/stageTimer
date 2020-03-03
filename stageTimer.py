#!/usr/bin/python
from appJar import gui
import datetime, sys, os

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
hour = int(sys.argv[1]) 
minute = int(sys.argv[2])

def runTimer():
    endT = datetime.datetime(year, month, day, hour, minute, 0, 0)    
    nowT = datetime.datetime.now()
    timeLeft = endT.replace(microsecond=0) - nowT.replace(microsecond=0)
    app.setLabel("time", timeLeft)

app = gui("Stage timer", handleArgs=False)

# Key events
def keyPress(key):
    if key == "Up":
        app.increaseFont()
    elif key == "Down":
        app.decreaseFont()
    elif key == "F1":
        os.system('systemctl poweroff')
    elif key == "Escape":
        exit()

# Window configuration
app.setSize("Fullscreen")
app.setLocation(10, 10)
app.setStretch("both")
app.setSticky("nesw")
app.setBg("black")
app.setFg("white")

# Screen layout
app.addLabel("time", "00:00:00")

# Widget design
#app.getLabelWidget("time").config(font="Times 300")
app.setFont(size=200)
# Run App
app.registerEvent(runTimer)

app.bindKey("Up", keyPress)
app.bindKey("Down", keyPress)
app.bindKey("F1", keyPress)
app.bindKey("Escape", keyPress)
app.go()



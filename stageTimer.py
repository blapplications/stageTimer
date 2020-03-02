#!/usr/bin/python
from appJar import gui
import datetime, sys

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

# Window configuration
app.setSize("Fullscreen")
app.hideTitleBar()
app.setLocation(10, 10)
app.setStretch("both")
app.setSticky("nesw")
app.setBg("black")
app.setFg("white")

# Screen layout
app.addLabel("time", "00:00:00")

# Widget design
app.getLabelWidget("time").config(font="Times 300")

# Run App
app.registerEvent(runTimer)
app.go()
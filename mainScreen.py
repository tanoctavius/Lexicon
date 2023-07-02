from cmu_graphics import *
import button

def drawMainScreen(app):
    #Initialise the background:
    drawRect(0, 0, app.width, app.height, fill = rgb(70, 75, 80))
    drawImage(app.keyboardIcon, 105, 95, width = 40, height = 20)

    #Draws the first rectangle + options
    drawCircle(app.width//2 - 350, 175, 25, fill = rgb(65, 65, 70))
    drawCircle(970, 175, 25, fill = rgb(65, 65, 70))
    drawRect(app.width//2 - 360, 150, 720, 50, fill = rgb(65, 65, 70))

    #Draws the second rectangle
    drawRect(app.secondRectangleStartingXCoord, 265, 140, 40, fill = rgb(65, 65, 70))
    drawCircle(app.secondRectangleStartingXCoord - 5, 285, 20, fill = rgb(65, 65, 70))
    drawCircle(app.secondRectangleStartingXCoord + 140, 285, 20, fill = rgb(65, 65, 70))
    drawImage(app.clockIcon, app.width//2 - 70, 275, width = 20, height = 20)
    button.Label.drawLabel(app.lineTimeLabel)
    
    #Initialising the options
    button.Label.drawLabel(app.crazyCapital)
    button.Label.drawLabel(app.crazyNumber)
    button.Label.drawLabel(app.mainPageTitle)
    button.Label.drawLabel(app.crazySpaces)
    button.Label.drawLabel(app.mixed)
    button.Label.drawLabel(app.lowercase)
    button.Label.drawLabel(app.uppercase)
    button.Label.drawLabel(app.mainPageMiniTitle)

    #Restart Icon
    drawImage(app.restartIcon, app.width//2 - app.restartIconWidth, app.height - 175, width = app.restartIconWidth, height = app.restartIconWidth)

#Checking the time label for the mouse, check whether it would light up:
def timeLabelLightUp(app):
    values = ["15", "30", "60", "90"]
    for rect in range(4):
        if rect == app.selectedTimeRectIndex:
            rectFillTimeColour = "white"
        elif rect != app.selectedTimeRectIndex:
            rectFillTimeColour = "grey"
        drawLabel(values[rect], app.timeLabelStartingPoint + 25 * rect, app.timeLabelYStartingPoint, font = 'impact', size = app.currTimeFont, align = 'center', fill = rectFillTimeColour)

#Checking whether the mouse hovers over the time
def onMouseMoveLightUp(app, mouseX, mouseY):
    timeHoverIndex = getTimeIndexFromMouseMove(app, mouseX, mouseY)
    if (timeHoverIndex == None):
        app.selectedTimeRectIndex = None 
    elif app.selectedTimeRectIndex == None: 
        app.selectedTimeRectIndex = timeHoverIndex

#CHecking whether the mouse is within the bounds
def getTimeIndexFromMouseMove(app, mouseX, mouseY):
    for rectNum in range(4): 
        if app.timeLabelStartingPoint + (25 * rectNum) <= mouseX <= app.timeLabelStartingPoint + (25 * rectNum) + 25:
            if app.timeLabelYStartingPoint <= mouseY <= app.timeLabelYStartingPoint + 20:
                return rectNum
    return None
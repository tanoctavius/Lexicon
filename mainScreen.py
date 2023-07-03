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
    
    #Initialising the titles:
    button.Label.drawLabel(app.mainPageTitle)
    button.Label.drawLabel(app.mainPageMiniTitle)

    #Restart Icon
    drawImage(app.restartIcon, app.width//2 - app.restartIconWidth, app.height - 175, width = app.restartIconWidth, height = app.restartIconWidth)
    
    #Can start to type if both time and option is selected
    if app.selectedLabelRectIndex != None and app.selectedTimeRectIndex != None:
        drawImage(app.restartIcon, 500, 500, width = app.restartIconWidth, height = app.restartIconWidth)
        

#Checking whether the options label is aligned with the mouse, will light up if clicked (reddish-yellow) or hovered over (white):
def optionsLabelLightUp(app):
    values = ["crazyCapital", "crazyNumber", "crazySpaces", "normal", "uppercase", "mixed"]
    for rect in range(6):
        if rect == app.selectedLabelRectIndex:
            rectFillTimeColour = rgb(228, 112, 61)
        elif rect == app.hoverLabelRectIndex:
            rectFillTimeColour = "white"
        elif rect != app.hoverLabelRectIndex and rect != app.selectedLabelRectIndex:
            rectFillTimeColour = "grey"
        drawLabel(values[rect], app.optionsLabelStartingPoint + 120 * rect, app.optionsLabelYStartingPoint, font = 'impact', size = app.currTimeFont, align = 'center', fill = rectFillTimeColour)

#Checking the time label for the mouse, check whether it would light up:
def timeLabelLightUp(app):
    values = ["15", "30", "60", "90"]
    for rect in range(4):
        if rect == app.selectedTimeRectIndex:
            rectFillTimeColour = rgb(228, 112, 61)
        elif rect == app.hoverTimeRectIndex:
            rectFillTimeColour = "white"
        elif rect != app.hoverTimeRectIndex and rect != app.selectedTimeRectIndex:
            rectFillTimeColour = "grey"
        drawLabel(values[rect], app.timeLabelStartingPoint + 25 * rect, app.timeLabelYStartingPoint, font = 'impact', size = app.currTimeFont, align = 'center', fill = rectFillTimeColour)

#Checking whether the mouse is within the bounds
def getTimeIndexFromMouseMove(app, mouseX, mouseY):
    for rectNum in range(4): 
        if app.timeLabelStartingPoint + (25 * rectNum) - 25//2 <= mouseX <= app.timeLabelStartingPoint + (25 * rectNum) + 25 - 25//2:
            if app.timeLabelYStartingPoint - 25//2 <= mouseY <= app.timeLabelYStartingPoint + 20 - 25//2:
                return rectNum
    return None

def getOptionsIndexFromMouseMove(app, mouseX, mouseY):
    for rectNum in range(6):
        if app.optionsLabelStartingPoint - 50 + 120 * rectNum <= mouseX <= app.optionsLabelStartingPoint + 70 + 120 * rectNum:
            if app.optionsLabelYStartingPoint - 25 <= mouseY <= app.optionsLabelYStartingPoint + 25:
                return rectNum
    return None

#Checking whether the mouse hovers over the time
def onMouseMoveLightUp(app, mouseX, mouseY):
    #For the time label
    timeHoverIndex = getTimeIndexFromMouseMove(app, mouseX, mouseY)
    app.hoverTimeRectIndex = None if (timeHoverIndex == None) else timeHoverIndex
    #For the options label
    optionsHoverIndex = getOptionsIndexFromMouseMove(app, mouseX, mouseY)
    app.hoverLabelRectIndex = None if (optionsHoverIndex == None) else optionsHoverIndex

#Checking whether the mouse presses  the time
def onMousePressLightUp(app, mouseX, mouseY):
    #For the time label
    temp1 = getTimeIndexFromMouseMove(app, mouseX, mouseY)
    if temp1 != None:
        timePressIndex = temp1
        if timePressIndex != None:
            app.selectedTimeRectIndex = timePressIndex
    #For the options label
    temp = getOptionsIndexFromMouseMove(app, mouseX, mouseY)
    if temp != None:
        optionsPressIndex = temp
        if optionsPressIndex != None: 
            app.selectedLabelRectIndex = optionsPressIndex
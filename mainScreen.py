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
    drawRect(app.width//2 - 70, 265, 140, 40, fill = rgb(65, 65, 70))
    drawCircle(app.width//2 - 75, 285, 20, fill = rgb(65, 65, 70))
    drawCircle(app.width//2 - 80 + 140 + 10, 285, 20, fill = rgb(65, 65, 70))
    drawImage(app.clockIcon, app.width//2 - 70, 275, width = 20, height = 20)
    button.Label.drawLabel(app.fifteenLabel)
    button.Label.drawLabel(app.thirtyLabel)
    button.Label.drawLabel(app.sixtyLabel)
    button.Label.drawLabel(app.ninetyLabel)
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

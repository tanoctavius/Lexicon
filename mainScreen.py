from cmu_graphics import *
import button

def drawMainScreen(app):
    #Initialise the background:
    drawRect(0, 0, app.width, app.height, fill = rgb(70, 75, 80))
    drawImage(app.keyboardIcon, 105, 95, width = 40, height = 20)
    drawCircle(app.width//2 - 350, 175, 25, fill = rgb(65, 65, 70))
    drawCircle(970, 175, 25, fill = rgb(65, 65, 70))
    drawRect(app.width//2 - 360, 150, 720, 50, fill = rgb(65, 65, 70))
    
    #Initialising the options
    button.Label.drawLabel(app.crazyCapital)
    button.Label.drawLabel(app.crazyNumber)
    button.Label.drawLabel(app.mainPageTitle)
    button.Label.drawLabel(app.crazySpaces)
    button.Label.drawLabel(app.mixed)
    button.Label.drawLabel(app.lowercase)
    button.Label.drawLabel(app.uppercase)
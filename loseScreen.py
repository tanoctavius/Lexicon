from cmu_graphics import *
import button

def drawLoseScreen(app):
    #Initialise the background:
    drawRect(0, 0, app.width, app.height, fill = rgb(70, 75, 80))
    drawImage(app.keyboardIcon, 105, 95, width = 40, height = 20)
    button.Label.drawLabel(app.mainPageTitle)
    button.Label.drawLabel(app.mainPageMiniTitle)
    
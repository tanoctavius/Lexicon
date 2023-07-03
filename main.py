from cmu_graphics import *
from PIL import Image
import button
import mainScreen
import loseScreen

#----------------Model Class--------------------------------
def onAppStart(app):
    #Initialising the size of the canvas:
    app.width = 1200
    app.height = 800

    #Initialising the screen:
    app.loseScreen = False
    app.mainScreen = True

    #Initialising Typing Text | Main Page:
    app.currText = "None"
    app.currTextColour = "Grey"
    app.mainPageTitle = button.Label("l e x i c o n", (207, 100), 25, 'impact', rgb(181, 94, 73), 'center', False)
    app.mainPageTypingText = button.Label(f"{app.currText}", (app.width//2, app.height//2), 60, 'impact', app.currTextColour, 'center', False)
    app.mainPageMiniTitle = button.Label("p r e m i e r     t y p i n g", (200, 76), 12.5, 'impact', rgb(210, 147, 128), 'center', False)
    app.secondRectangleStartingXCoord = app.width//2 - 70

    app.keyboardIcon = Image.open('images/keyboardIcon.png')
    app.keyboardIcon = CMUImage(app.keyboardIcon)
    app.clockIcon = Image.open('images/clock2.png')
    app.clockIcon = CMUImage(app.clockIcon)
    app.restartIcon = Image.open('images/restart3.png')
    app.restartIcon = CMUImage(app.restartIcon)
    app.restartIconWidth = 30
    app.timeLabelStartingPoint = 570 + 25//2
    app.timeLabelYStartingPoint = 285

    reset(app)

def reset(app):
    app.mainScreen = True
    app.loseScreen = False 

    app.currTimeLabel = "Grey"
    app.currTimeFont = 15
    app.lineTimeLabel = button.Label("|", (570 - 7, 285), 20, 'impact', app.currTimeLabel, 'center', True)
    app.hoverTimeRectIndex = None
    app.selectedTimeRectIndex = None

    app.currChoiceColour = "Gray"
    app.crazyCapital = button.Label("CrazyCapital", (240 + 120//2, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.crazyNumber = button.Label("CrazyNumber", (240 + 120//2 + 120, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.crazySpaces = button.Label("CrazySpaces", (240 + 120//2 + 240, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.uppercase = button.Label("Uppercase", (240 + 120//2 + 360, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.lowercase = button.Label("Lowercase", (240 + 120//2 + 480, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.mixed = button.Label("Mixed", (240 + 120//2 + 600, 175), 15, 'impact', app.currChoiceColour, 'center', False)

#----------------View Class--------------------------------
def redrawAll(app):
    if app.mainScreen:
        mainScreen.drawMainScreen(app)
        mainScreen.timeLabelLightUp(app)
    if app.loseScreen:
        loseScreen.drawLoseScreen(app)
    
#----------------Controller Class--------------------------------
def onMouseMove(app, mouseX, mouseY):
    if app.mainScreen:
        mainScreen.onMouseMoveLightUp(app, mouseX, mouseY)

def onMousePress(app, mouseX, mouseY):
    if app.mainScreen:
        mainScreen.onMousePressLightUp(app, mouseX, mouseY)

#-------------------------------------------------------------------------------
#Opening Images
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

runApp()

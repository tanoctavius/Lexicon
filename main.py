from cmu_graphics import *
from PIL import Image
import button
import mainScreen
import loseScreen

def onAppStart(app):
    app.width = 1200
    app.height = 800

    #Initialising Typing Text | Main Page:
    app.currText = "None"
    app.currTextColour = "Grey"
    app.mainPageTitle = button.Label("l e x i c o", (200, 100), 25, 'impact', rgb(181, 94, 73), 'center', False)
    app.mainPageTypingText = button.Label(f"{app.currText}", (app.width//2, app.height//2), 60, 'impact', app.currTextColour, 'center', False)

    app.keyboardIcon = Image.open('images/keyboardIcon.png')
    app.keyboardIcon = CMUImage(app.keyboardIcon)

    #Restarts if typing is lost
    reset(app)

def reset(app):
    app.currChoiceColour = "Gray"
    app.crazyCapital = button.Label("CrazyCapital", (240 + 120//2, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.crazyNumber = button.Label("CrazyNumber", (240 + 120//2 + 120, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.crazySpaces = button.Label("CrazySpaces", (240 + 120//2 + 240, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.uppercase = button.Label("Uppercase", (240 + 120//2 + 360, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.lowercase = button.Label("Lowercase", (240 + 120//2 + 480, 175), 15, 'impact', app.currChoiceColour, 'center', False)
    app.mixed = button.Label("Mixed", (240 + 120//2 + 600, 175), 15, 'impact', app.currChoiceColour, 'center', False)

def redrawAll(app):
    mainScreen.drawMainScreen(app)
    
#-------------------------------------------------------------------------------
#Opening Images
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

runApp()

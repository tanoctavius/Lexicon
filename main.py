from cmu_graphics import *
from PIL import Image
import view
import button

def onAppStart(app):
    app.width = 1200
    app.height = 800

    #Initialising Typing Text | Main Page:
    app.currText = "None"
    app.currTextColour = "Grey"
    app.mainPageTitle = button.Label("lexico", (100, 50), 20, 'impact', app.currTextColour, 'center', False)
    app.mainPageTypingText = button.Label(f"{app.currText}", (app.width//2, app.height//2), 60, 'impact', app.currTextColour, 'center', False)

def redrawAll(app):
    view.drawText(app)


#-------------------------------------------------------------------------------
#Opening Images
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

runApp()

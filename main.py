from cmu_graphics import *
from PIL import Image
import webbrowser
import button
import mainScreen
import loseScreen
import settingScreen
import infoScreen
import leaderboardScreen 

#----------------Model Class--------------------------------
def onAppStart(app):
    #Initialising the size of the canvas:
    app.width = 1200
    app.height = 800
    
    #Initialising Typing Text | Main Page:
    app.currText = "None"
    app.currTextColour = "Grey"
    app.mainPageTitle = button.Label("l e x i c o n", (207, 100), 25, 'impact', rgb(181, 94, 73), 'center', False)
    app.mainPageTypingText = button.Label(f"{app.currText}", (app.width//2, app.height//2), 60, 'impact', app.currTextColour, 'center', False)
    app.mainPageMiniTitle = button.Label("p r e m i e r     t y p e", (203, 76), 11.5, 'impact', rgb(210, 147, 128), 'center', False)
    app.secondRectangleStartingXCoord = app.width//2 - 70

    app.keyboardIcon = Image.open('images/keyboardIcon.png')
    app.keyboardIcon = CMUImage(app.keyboardIcon)
    app.clockIcon = Image.open('images/clock2.png')
    app.clockIcon = CMUImage(app.clockIcon)
    app.restartIcon = Image.open('images/restart3.png')
    app.restartIcon = CMUImage(app.restartIcon)
    app.infoIcon = Image.open('images/infoIcon.png')
    app.infoIcon = CMUImage(app.infoIcon)
    app.settingIcon = Image.open('images/settingIcon.png')
    app.settingIcon = CMUImage(app.settingIcon)
    app.homeIcon = Image.open('images/home.png')
    app.homeIcon = CMUImage(app.homeIcon)
    app.crownIcon = Image.open('images/crown.png')
    app.crownIcon = CMUImage(app.crownIcon)
    app.restartIconWidth = 30
    app.timeLabelStartingPoint = 570 + 25//2
    app.timeLabelYStartingPoint = 285
    app.optionsLabelStartingPoint = 240 + 120//2
    app.optionsLabelYStartingPoint = 175

    #Initialising list of all previous scores:
    app.allScores = []

    #Initialising underpage items:
    app.GitHubIcon = Image.open('images/GitHubIcon.png')
    app.GitHubIcon = CMUImage(app.GitHubIcon)
    app.linkedInIcon = Image.open('images/LinkedInIcon.png')
    app.linkedInIcon = CMUImage(app.linkedInIcon)
    app.bottomTierIconStartingX = 530
    app.bottomTierIconDimensions = 20

    reset(app)

def reset(app):
    '''Screens:'''
    app.mainScreen = False  
    app.loseScreen = False  
    app.leaderboardScreen = True
    app.settingScreen = False
    app.loseScreen = False
    app.infoScreen = False
    
    '''Time Variables:'''
    app.stepsPerSecond = 1
    app.secondsLeft = 0
    app.currTimeLabel = "Grey"
    app.currTimeFont = 15
    app.lineTimeLabel = button.Label("|", (570 - 7, 285), 20, 'impact', app.currTimeLabel, 'center', True)

    '''Typing variables:'''
    app.inputCharacters = []
    
    #Initialising values for hovering + pressing options and time ribbon
    app.hoverTimeRectIndex = None
    app.selectedTimeRectIndex = None
    app.selectedLabelRectIndex = None
    app.hoverLabelRectIndex = None

    '''Final Statistics:'''
    app.score = 0
    app.wpm = 0
    app.rawWpm = 0
    app.finalPercentage = 0
    app.accuracy = 0
    app.timeSelected = "None"
    app.modeSelected = "None"

    '''Setting Selections:'''
    app.testDifficulty = "medium"
    app.blindMode = False
    app.quickRestart = False
    app.flipColours = False
    app.showTimer = True
    app.showCapsLockWarning = True 

#----------------View Class--------------------------------
def redrawAll(app):
    if app.mainScreen:
        mainScreen.drawMainScreen(app)

        #Only once both options are selected, the options will dissapear
        if app.selectedLabelRectIndex == None or app.selectedTimeRectIndex == None:
            mainScreen.drawRectangleCircleOptions(app)
            mainScreen.timeLabelLightUp(app)
            mainScreen.optionsLabelLightUp(app)

    if app.loseScreen:
        loseScreen.drawLoseScreen(app)

    if app.infoScreen:
        infoScreen.drawInfoScreen(app)

    if app.settingScreen:
        settingScreen.drawSettingScreen(app)
        settingScreen.drawSettingScreenOptions(app)
    
    if app.leaderboardScreen:
        leaderboardScreen.drawLeaderboardScreen(app)
        leaderboardScreen.drawFinalHighScoreScreen(app)
    
#----------------Controller Class--------------------------------
def onStep(app):
    if app.mainScreen:
        if app.selectedLabelRectIndex != None and app.selectedTimeRectIndex != None and len(app.inputCharacters) != 0:
            app.secondsLeft = int(app.secondsLeft)
            if app.secondsLeft > 0:    
                app.secondsLeft = int(app.secondsLeft) - 1
            if app.secondsLeft == 0:
                app.loseScreen = True
                app.mainScreen = False 

                #Inputing the final score after losing:
                app.allScores.append((app.score, app.wpm, app.timeSelected, app.modeSelected, app.accuracy, len(app.inputCharacters)))

def onMouseMove(app, mouseX, mouseY):
    if app.mainScreen:
        mainScreen.onMouseMoveLightUp(app, mouseX, mouseY)

def onMousePress(app, mouseX, mouseY):
    if app.mainScreen:
        mainScreen.onMousePressLightUp(app, mouseX, mouseY)
        mainScreen.onMousePressIcon(app, mouseX, mouseY)
        
        #If restart icon is selected, app is restarted
        restartBounds = app.width//2 - app.restartIconWidth, app.height - 175, app.restartIconWidth, app.restartIconWidth
        if button.Button.buttonBounds(mouseX, mouseY, restartBounds):
            reset(app)
    
    if app.leaderboardScreen:
        leaderboardScreen.onMousePressIcon(app, mouseX, mouseY)
    
    if app.settingScreen:
        settingScreen.onMousePressIcon(app, mouseX, mouseY)
    
    if app.infoScreen:
        infoScreen.onMousePressIcon(app, mouseX, mouseY)
    
    if app.loseScreen:
        loseScreen.onMousePressIcon(app, mouseX, mouseY)

        #If restart icon is selected, app is restarted
        restartBounds = app.width//2 - app.restartIconWidth, app.height - 175, app.restartIconWidth, app.restartIconWidth
        if button.Button.buttonBounds(mouseX, mouseY, restartBounds):
            reset(app)

def onKeyPress(app, key):
    if app.selectedLabelRectIndex != None and app.selectedTimeRectIndex != None:
        #Only once typing mode is activated, typing will trigger the start of the timer 
        app.inputCharacters.append(key)

#-------------------------------------------------------------------------------
#Opening Images
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

runApp()
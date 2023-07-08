from cmu_graphics import *
import button

def drawLoseScreenStatistics(app):
    drawLabel('wpm', 95, 200, size = 30, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.wpm}', 95, 255, size = 70, font = 'impact', align = 'left', fill = rgb(228, 112, 61))
    drawLabel('final %', 95, 325, size = 30, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.finalPercentage}', 95, 380, size = 70, font = 'impact', align = 'left', fill = rgb(228, 112, 61))
    drawLabel('accuracy', 95, 445, size = 22, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.accuracy}%', 95, 475, size = 22, font = 'impact', fill = rgb(228, 112, 61), align = 'left')

    #Graph Details:
    drawRect(200, 185, 905, 230)
    drawLabel('Words Per Minute (wpm)', 215, 295, size = 16, font = 'impact', rotateAngle = 270, fill = rgb(150, 150, 150), align = 'center')
    drawLabel('Time (s)', 652.5, 400, size = 16, font = 'impact', fill = rgb(150, 150, 150))
    

def drawLoseScreen(app):
    #Initialise the background:
    drawRect(0, 0, app.width, app.height, fill = rgb(70, 75, 80))
    drawImage(app.keyboardIcon, 95, 80, width = 50, height = 30)
    
    #Initialising the titles:
    button.Label.drawLabel(app.mainPageTitle)
    button.Label.drawLabel(app.mainPageMiniTitle)

    #Icon:
    drawImage(app.homeIcon, 275, 93, width = 30, height = 20)
    drawImage(app.settingIcon, 320, 93, width = 20, height = 20)
    drawImage(app.infoIcon, 355, 93, width = 20, height = 20)
    drawImage(app.crownIcon, 390, 93, width = 20, height = 20)

    drawLoseScreenStatistics(app)

def onMousePressIcon(app, mouseX, mouseY):
    mainScreenBounds = 275, 93, 30, 20
    if button.Button.buttonBounds(mouseX, mouseY, mainScreenBounds):
        app.mainScreen = True 
        app.loseScreen = False

    infoScreenBounds = 335, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, infoScreenBounds):
        app.infoScreen = True
        app.loseScreen = False

    settingBounds = 320, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, settingBounds):
        app.loseScreen = False 
        app.settingScreen = True 

    leaderboardBounds = 390, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, leaderboardBounds):
        app.loseScreen = False
        app.leaderboardScreen = True 
    
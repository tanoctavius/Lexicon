from cmu_graphics import *
import button
import webbrowser
import math 

def getFinalWpmScore(app):
    app.words = []
    temp = ""
    for i in app.inputCharacters:
        if i != "space":
            temp += i
        else: 
            app.words.append(temp)
            temp = ""
    return int((len(app.words)/int(app.timeSelected)) * 60)

def drawFinalGraphStatistics(app):
    #Drawing the x-axis:
    for i in range(6):
        drawLabel(f'{i * int(app.timeSelected)//5}', 260 + 169 * i, 405, font = 'impact', size = 14.5, fill = rgb(150, 150, 150))
    #Drawing the y-axis: 
    bestWpmSpeed = 50 * math.ceil(app.wpm / 50)
    for i in range(6):
        drawLabel(f'{bestWpmSpeed//5 * i}', 247, 390 - 37 * i, font = 'impact', size = 14.5, fill = rgb(150, 150, 150))
    #Drawing the average line: 
    averageYLine = 390 - (app.wpm/bestWpmSpeed * (390-205))
    drawLine(260, averageYLine, 1105, averageYLine, fill = rgb(228, 112, 61))
    #Drawing the points:

def drawLoseScreenStatistics(app):
    #Drawing the statistics after completion 
    drawLabel('wpm', 95, 220, size = 30, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.wpm}', 95, 275, size = 70, font = 'impact', align = 'left', fill = rgb(228, 112, 61))
    drawLabel('final %', 95, 345, size = 30, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.score}', 95, 400, size = 70, font = 'impact', align = 'left', fill = rgb(228, 112, 61))
    drawLabel('accuracy', 95, 465, size = 22, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.accuracy}%', 95, 495, size = 22, font = 'impact', fill = rgb(228, 112, 61), align = 'left')
    drawLabel('raw Wpm', 310, 465, size = 22, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.rawWpm}', 310, 495, size = 22, font = 'impact', fill = rgb(228, 112, 61), align = 'left')
    drawLabel('time', 540, 465, size = 22, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.timeSelected}', 540, 495, size = 22, font = 'impact', fill = rgb(228, 112, 61), align = 'left')
    drawLabel('mode', 760, 465, size = 22, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.currMode}', 760, 495, size = 22, font = 'impact', fill = rgb(228, 112, 61), align = 'left')
    drawLabel('characters', 1000, 465, size = 22, font = 'impact', fill = rgb(150, 150, 150), align = 'left')
    drawLabel(f'{app.numberOfChar}', 1000, 495, size = 22, font = 'impact', fill = rgb(228, 112, 61), align = 'left')

    #Graph Details:
    # drawRect(200, 185, 905, 230)
    drawLabel('Words Per Minute (wpm)', 215, 300, size = 16, font = 'impact', rotateAngle = 270, fill = rgb(150, 150, 150), align = 'center')
    drawLabel('Time (s)', 652.5, 420, size = 16, font = 'impact', fill = rgb(150, 150, 150))
    drawLine(260, 205, 260, 390, fill = rgb(150, 150, 150))
    drawLine(260, 390, 1105, 390, fill = rgb(150, 150, 150))

    #Drawing the bottom titles:
    drawImage(app.linkedInIcon, app.bottomTierIconStartingX, 760, width = app.bottomTierIconDimensions, height = app.bottomTierIconDimensions)
    drawImage(app.GitHubIcon, app.bottomTierIconStartingX + 30, 760, width = app.bottomTierIconDimensions, height = app.bottomTierIconDimensions)
    drawLabel('lexicon_tanoctavius', 590, 770, font = 'impact', size = 15, align = 'left', fill = 'white')

def getFinalScore(app):
    return int(app.wpm // 4 + app.accuracy // 4 + app.rawWpm // 6)

def getRawWpm(app):
    if len(app.words) > 0:
        return int((len(app.inputCharacters)/ len(app.words))/ int(app.timeSelected) * 60)
    return 0

def getAccuracy(app):
    return int((app.lastCharIndex/ len(app.inputCharacters))* 100) % 100.01

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

    #Drawing the restart sign
    drawImage(app.restartIcon, app.width//2 - app.restartIconWidth, app.height - 175, width = app.restartIconWidth, height = app.restartIconWidth)

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

    gitHubIconBounds = app.bottomTierIconStartingX + 30, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, gitHubIconBounds):
        webbrowser.open("https://github.com/tanoctavius/Lexicon")
    
    linkedInIconBounds = app.bottomTierIconStartingX, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, linkedInIconBounds):
        webbrowser.open("https://www.linkedin.com/in/octaviusetetanzhylam/")
    
from cmu_graphics import *
import button
import webbrowser

def drawFinalHighScoreScreen(app):
    #Draws the titles for the high score screen 
    organisedList = getOrganisedListOfHighScores(app)
    drawLabel('Rank', app.width//2 - 135, app.yTopCord, font = app.highScoreFont, size = app.startScreenSize)
    drawLabel('Score', app.width//2 - 20, app.yTopCord, font = app.highScoreFont, size = app.startScreenSize)
    drawLabel('Time', app.width//2 + 110, app.yTopCord, font = app.highScoreFont, size = app.startScreenSize)
    
    #Draws all the scores stored
    for i in range(len(organisedList)):
        score, time = organisedList[i]
        drawLabel(f'{i + 1}.', app.width//2 - 110, app.yTopCord + (i+1)*45, font = app.highScoreFont, size = app.startScreenSize)
        drawLabel(f'{score}', app.width//2 - 24, app.yTopCord + (i+1)*45, font = app.highScoreFont, size = app.startScreenSize)
        drawLabel(f'{time}', app.width//2 + 115, app.yTopCord + (i+1)*45, font = app.highScoreFont, size = app.startScreenSize)

def getOrganisedListOfHighScores(app):
    result = []
    resultSet = set()
    resultDict = dict()
    for scores in range(len(app.allScores)):
        percentage, time = app.allScores[scores]
        resultSet.add(percentage)
        resultDict[percentage] = time 
    sortedDict = (sorted(resultSet))[::-1]
    for i in range(len(sortedDict)):
        time = resultDict[sortedDict[i]]
        result.append((sortedDict[i], time))
    return result

def drawLeaderboardScreen(app):
    #Initialise the background:
    drawRect(0, 0, app.width, app.height, fill = rgb(70, 75, 80))
    drawImage(app.keyboardIcon, 95, 80, width = 50, height = 30)
    drawRect(300, 300, 200, 200)
    
    #Initialising the titles:
    button.Label.drawLabel(app.mainPageTitle)
    button.Label.drawLabel(app.mainPageMiniTitle)

    #Icon:
    drawImage(app.homeIcon, 275, 93, width = 30, height = 20)
    drawImage(app.settingIcon, 320, 93, width = 20, height = 20)
    drawImage(app.infoIcon, 355, 93, width = 20, height = 20)
    drawImage(app.crownIcon, 390, 93, width = 20, height = 20)

    #Drawing the bottom titles:
    drawImage(app.linkedInIcon, app.bottomTierIconStartingX, 760, width = app.bottomTierIconDimensions, height = app.bottomTierIconDimensions)
    drawImage(app.GitHubIcon, app.bottomTierIconStartingX + 30, 760, width = app.bottomTierIconDimensions, height = app.bottomTierIconDimensions)
    drawLabel('lexicon_tanoctavius', 590, 770, font = 'impact', size = 15, align = 'left', fill = 'white')

def onMousePressIcon(app, mouseX, mouseY):
    mainScreenBounds = 275, 93, 30, 20
    if button.Button.buttonBounds(mouseX, mouseY, mainScreenBounds):
        app.mainScreen = True 
        app.leaderboardScreen = False

    infoScreenBounds = 355, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, infoScreenBounds):
        app.infoScreen = True
        app.leaderboardScreen = False 

    settingBounds = 320, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, settingBounds):
        app.settingScreen = True
        app.leaderboardScreen = False 

    leaderboardBounds = 390, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, leaderboardBounds):
        app.leaderboardScreen = True 
    
    gitHubIconBounds = app.bottomTierIconStartingX + 30, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, gitHubIconBounds):
        webbrowser.open("https://github.com/tanoctavius/Lexicon")
    
    linkedInIconBounds = app.bottomTierIconStartingX, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, linkedInIconBounds):
        webbrowser.open("https://www.linkedin.com/in/octaviusetetanzhylam/")
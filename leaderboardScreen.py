from cmu_graphics import *
import button
import webbrowser

def drawFinalHighScoreScreen(app):
    #Draws the titles for the high score screen 
    leaderboardFont = 'impact'
    leaderboardTitleSize = 22
    leaderboardYCoord = 200
    colour = rgb(228, 112, 61)
    drawLabel('Rank', 200, leaderboardYCoord, font = leaderboardFont, size = leaderboardTitleSize, fill = colour, align = 'left')
    drawLabel('Score', 300, leaderboardYCoord, font = leaderboardFont, size = leaderboardTitleSize, fill = colour, align = 'left')
    drawLabel('Wpm', 450, leaderboardYCoord, font = leaderboardFont, size = leaderboardTitleSize, fill = colour, align = 'left')
    drawLabel('Time; Mode', 600, leaderboardYCoord, font = leaderboardFont, size = leaderboardTitleSize, fill = colour, align = 'left')
    drawLabel('accur.', 875, leaderboardYCoord, font = leaderboardFont, size = leaderboardTitleSize, fill = colour, align = 'left')
    drawLabel('char.', 975, leaderboardYCoord, font = leaderboardFont, size = leaderboardTitleSize, fill = colour, align = 'left')
    drawLine(180, 230, 1050, 230, fill = rgb(150, 75, 45), lineWidth = 5)
    
    #Draws all the scores stored
    finalScoreList = app.allScores
    organisedList = getOrganisedListOfHighScores(finalScoreList)
    highScoreFont = 'impact'
    highScoreSize = 20
    highScoreYCord = 205
    highScoreIncreaseSize = 50
    for i in range((len(app.allScores))):
        score, wpm, time, mode, accuracy, character = organisedList[i]
        drawLabel(f'{i+1}', 220, highScoreYCord + (i + 1) * highScoreIncreaseSize, font = highScoreFont, size = highScoreSize, align = 'center', fill = "white")
        drawLabel(f'{score}', 320, highScoreYCord + (i + 1) * highScoreIncreaseSize, font = highScoreFont, size = highScoreSize, align = 'center', fill = "white")
        drawLabel(f'{wpm}', 470, highScoreYCord + (i + 1) * highScoreIncreaseSize, font = highScoreFont, size = highScoreSize, align = 'center', fill = "white")
        drawLabel(f'{time}; {mode}', 650, highScoreYCord + (i + 1) * highScoreIncreaseSize, font = highScoreFont, size = highScoreSize, align = 'center', fill = "white")
        drawLabel(f'{accuracy}', 900, highScoreYCord + (i + 1) * highScoreIncreaseSize, font = highScoreFont, size = highScoreSize, align = 'center', fill = "white")
        drawLabel(f'{character}', 1000, highScoreYCord + (i + 1) * highScoreIncreaseSize, font = highScoreFont, size = highScoreSize, align = 'center', fill = "white")
        drawLine(180, 230 + (i+1) * 50, 1050, 230 + (i+1) * 50, lineWidth = 3, fill = rgb(75, 50, 30))
    
def getOrganisedListOfHighScores(finalScoreList):
    result = []
    resultSet = set()
    resultDict = {}
    for object in range(len(finalScoreList)):
        score, wpm, time, mode, accuracy, character = finalScoreList[object]
        resultSet.add(score)
        resultDict[score] = wpm, time, mode, accuracy, character
    sortedDict = (sorted(resultSet))[::-1]
    for i in range(len(sortedDict)):
        wpm, time, mode, accuracy, character = resultDict[sortedDict[i]]
        result.append((sortedDict[i], wpm, time, mode, accuracy, character))
    return result 

def drawLeaderboardScreen(app):
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
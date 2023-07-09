from cmu_graphics import *
import button
import webbrowser

def drawSettingScreen(app):
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
        app.settingScreen = False

    infoScreenBounds = 355, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, infoScreenBounds):
        app.infoScreen = True
        app.settingScreen = False 

    settingBounds = 320, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, settingBounds):
        app.settingScreen = True

    leaderboardBounds = 390, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, leaderboardBounds):
        app.leaderboardScreen = True 
        app.settingScreen = False 
    
    gitHubIconBounds = app.bottomTierIconStartingX + 30, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, gitHubIconBounds):
        webbrowser.open("https://github.com/tanoctavius/Lexicon")
    
    linkedInIconBounds = app.bottomTierIconStartingX, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, linkedInIconBounds):
        webbrowser.open("https://www.linkedin.com/in/octaviusetetanzhylam/")
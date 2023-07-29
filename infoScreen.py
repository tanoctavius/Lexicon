from cmu_graphics import *
import button
import webbrowser

def drawInfoScreen(app):
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

    #Drawing all fo the information:
    drawInfoScreenInformation(app)

    #Drawing the bottom titles:
    drawImage(app.linkedInIcon, app.bottomTierIconStartingX, 760, width = app.bottomTierIconDimensions, height = app.bottomTierIconDimensions)
    drawImage(app.GitHubIcon, app.bottomTierIconStartingX + 30, 760, width = app.bottomTierIconDimensions, height = app.bottomTierIconDimensions)
    drawLabel('lexicon_tanoctavius', 590, 770, font = 'impact', size = 15, align = 'left', fill = 'white')

def drawInfoScreenInformation(app):
    drawLabel('a b o u t', 157, 170, size = 28, font = 'impact', fill = rgb(181, 94, 73), align = "left")
    #Introduction Paragraph: 
    drawLabel('Inspired by monkeytype, Lexicon features a customisable and interactive typing test.', 
              157, 206, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('Constructed on the CMU_Graphics framework, the code is organised on a Model-View-Controller', 
              157, 226, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('framework with Object-Orientated-Programming. There are varying difficulties, options', 
              157, 246, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('and time limits to be customised.', 
              157, 266, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    
    #Text Paragraph:
    drawLabel('t e x t', 157, 316, size = 20, font = 'impact', fill = rgb(181, 94, 73), align = "left", bold = True)
    drawLabel('The text is webscraped and accessed for difficulties using an algorithm. The level can be', 
              157, 341, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('selected in the settings.', 
              157, 361, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)

    #Stats Paragraph:
    drawLabel('s t a t s', 157, 401, size = 20, font = 'impact', fill = rgb(181, 94, 73), align = "left", bold = True)
    drawLabel('wpm - words per minute, based on correctly typed characters (including spaces)', 
              157, 426, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('raw wpm - total amount of characters typed, regardless of correctness', 
              157, 446, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('final score - based on correct characters typed, wpm, difficulty of text, on scale of 100%', 
              157, 466, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    
    #Result Pagagraph:
    drawLabel('r e s u l t', 157, 511, size = 20, font = 'impact', fill = rgb(181, 94, 73), align = "left", bold = True)
    drawLabel('After completing the time, a result page with wpm, raw wpm and final score will be displayed.', 
              157, 536, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('Moreover, a graph will mark the typing pace alongside a leaderboard for all attemps.', 
              157, 556, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)

    #Additional Note Pagagraph:
    drawLabel('a d d i t i o n a l  n o t e s', 157, 606, size = 20, font = 'impact', fill = rgb(181, 94, 73), align = "left", bold = True)
    drawLabel('Lexicon is a passion project created in two weeks. If any bugs are encountered, please', 
              157, 631, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('create an issue on GitHub (https://github.com/tanoctavius/Lexicon)', 
              157, 651, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('To reach me further with inquiries or any further opportunities, please contact me at:', 
              157, 681, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    drawLabel('Email: tanoctavius@gmail.com', 
              157, 701, size = 16, font = 'Courier New', fill = "white", align = "left", bold = False)
    
def onMousePressIcon(app, mouseX, mouseY):
    mainScreenBounds = 275, 93, 30, 20
    if button.Button.buttonBounds(mouseX, mouseY, mainScreenBounds):
        app.mainScreen = True 
        app.infoScreen = False

    infoScreenBounds = 335, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, infoScreenBounds):
        app.infoScreen = True

    settingBounds = 320, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, settingBounds):
        app.infoScreen = False
        app.settingScreen = True 

    leaderboardBounds = 390, 93, 20, 20
    if button.Button.buttonBounds(mouseX, mouseY, leaderboardBounds):
        app.leaderboardScreen = True 
        app.infoScreen = False 

    gitHubIconBounds = app.bottomTierIconStartingX + 30, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, gitHubIconBounds):
        webbrowser.open("https://github.com/tanoctavius/Lexicon")
    
    linkedInIconBounds = app.bottomTierIconStartingX, 760, app.bottomTierIconDimensions, app.bottomTierIconDimensions
    if button.Button.buttonBounds(mouseX, mouseY, linkedInIconBounds):
        webbrowser.open("https://www.linkedin.com/in/octaviusetetanzhylam/")
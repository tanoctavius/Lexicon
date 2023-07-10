from cmu_graphics import *
import button
import webbrowser

def drawSettingScreenOptions(app):
    #Drawing Instructions:
    drawLabel('TEST DIFFICULTY', 160, 160, fill = rgb(150, 150, 150), size = 16, font = 'impact', align = 'left')
    drawLabel('There are 3 levels, easy has common words and punctuation whilst medium', 160, 185, align = 'left', fill = 'white', size = 16, font = 'impact')
    drawLabel('and hard contains increasingly more complex punctuation and vocabulary.', 160, 205, align = 'left', fill = 'white', size = 16, font = 'impact')
    drawLabel('BLIND MODE', 160, 255, fill = rgb(150, 150, 150), size = 16, font = 'impact', align = 'left')
    drawLabel('Wrong characters (input) will not be marked red if incorrect.', 160, 280, align = 'left', fill = 'white', size = 16, font = 'impact')
    drawLabel('QUICK RESTART', 160, 335, fill = rgb(150, 150, 150), size = 16, font = 'impact', align = 'left')
    drawLabel('Press "tab" to quickly restart the test, whilst taking the test or after.', 160, 360, align = 'left', fill = 'white', size = 16, font = 'impact')
    drawLabel('FLIP COLOURS', 160, 415, fill = rgb(150, 150, 150), size = 16, font = 'impact', align = 'left')
    drawLabel('By default, typed text is brighter than the future text. When enabled, the ', 160, 440, align = 'left', fill = 'white', size = 16, font = 'impact')
    drawLabel('colors will flip and the future text will be brighter than the typed.', 160, 465, align = 'left', fill = 'white', size = 16, font = 'impact')
    drawLabel('SHOW TIMER', 160, 520, fill = rgb(150, 150, 150), size = 16, font = 'impact', align = 'left')
    drawLabel('If on, the timer will be shown throughout the typing test.', 160, 545, align = 'left', fill = 'white', size = 16, font = 'impact')
    drawLabel('SHOW CAPS LOCK WARNING', 160, 600, fill = rgb(150, 150, 150), size = 16, font = 'impact', align = 'left')
    drawLabel('If the setting is on alongside caps lock, a warning will be shown.', 160, 625, align = 'left', fill = 'white', size = 16, font = 'impact')

    #Drawing option clickers:
    for i in range(3):
        values = ["easy", "medium", "hard"]
        if values[i] == app.testDifficulty:
            colour = rgb(228, 112, 61)
        else:
            colour = rgb(45, 45, 45)
        drawRect(700 + (i * 123), 160, 93, 40, fill = colour)

        values1 = ["e a s y", "m e d i u m", "h a r d"]
        drawLabel(f'{values1[i]}', 746.5 + i * 123, 180, align = 'center', font = 'impact', size = 16)

    for i in range(2):
        if i == app.blindMode:
            blindColour = rgb(228, 112, 61)
        else:
            blindColour = rgb(45, 45, 45)
        drawRect(700 + (i * 190), 255, 150, 40, fill = blindColour)

        if i == app.quickRestart:
            quickRestartColour = rgb(228, 112, 61)
        else:
            quickRestartColour = rgb(45, 45, 45)
        drawRect(700 + (i * 190), 335, 150, 40, fill = quickRestartColour)

        if i == app.flipColours:
            flipColourColour = rgb(228, 112, 61)
        else:
            flipColourColour = rgb(45, 45, 45)
        drawRect(700 + (i * 190), 415, 150, 40, fill = flipColourColour)

        if i == app.showTimer:
            showTimerColour = rgb(228, 112, 61)
        else:
            showTimerColour = rgb(45, 45, 45)
        drawRect(700 + (i * 190), 520, 150, 40, fill = showTimerColour)

        if i == app.showCapsLockWarning:
            showCapsLockWarningColour = rgb(228, 112, 61)
        else:
            showCapsLockWarningColour = rgb(45, 45, 45)
        drawRect(700 + (i * 190), 600, 150, 40, fill = showCapsLockWarningColour)
    
    for i in range(5):
        values = [255, 335, 415, 520, 600]
        for j in range(2):
            if j == 0:
                drawLabel("f a l s e", 775, (values[i] + 20), align = 'center', fill = 'black', font = 'impact', size = 16)
            if j == 1:
                drawLabel("t r u e", 965, (values[i] + 20), align = 'center', fill = 'black', font = 'impact', size = 16)

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
    blindModeBoundsFalse = 700, 255, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, blindModeBoundsFalse):
        app.blindMode = False 
    blindModeBoundsTrue = 890, 255, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, blindModeBoundsTrue):
        app.blindMode = True 
    
    quickRestartBoundsFalse = 700, 335, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, quickRestartBoundsFalse):
        app.quickRestart = False 
    quickRestartBoundsTrue = 890, 335, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, quickRestartBoundsTrue):
        app.quickRestart = True 
    
    flipColoursBoundsFalse = 700, 415, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, flipColoursBoundsFalse):
        app.flipColours = False 
    flipColoursBoundsTrue = 890, 415, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, flipColoursBoundsTrue):
        app.flipColours = True 

    showTimerColoursBoundsFalse = 700, 520, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, showTimerColoursBoundsFalse):
        app.showTimer = False 
    showTimerColoursBoundsTrue = 890, 520, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, showTimerColoursBoundsTrue):
        app.showTimer = True 

    showCapsLockWarningBoundsFalse = 700, 600, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, showCapsLockWarningBoundsFalse):
        app.showCapsLockWarning = False 
    showCapsLockWarningBoundsTrue = 890, 600, 150, 40
    if button.Button.buttonBounds(mouseX, mouseY, showCapsLockWarningBoundsTrue):
        app.showCapsLockWarning = True 

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
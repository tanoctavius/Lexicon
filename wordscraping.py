from cmu_graphics import *
import requests
from bs4 import BeautifulSoup
import word 

def getText():
    r = requests.get('https://nobaproject.com/textbooks/introduction-to-psychology-the-full-noba-collection/modules/therapeutic-orientations')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='col-md-9 noba-col-main')
    lines = s.find_all('p')
    finalResult = ""
    for line in lines:
        finalResult += (line.text)
    return finalResult[17:]

def getChosenDifficultyText():
    finalText = app.text
    if app.currMode != None:
        new = word.getChangedStyle(finalText, app.currMode)
    return finalText if app.currMode == None else new

def getPresentedScreenText(app):
    line1, line2, line3 = "", "", ""
    currIndex = app.lastCharIndex
    completeText = (getChosenDifficultyText())
    line1, lastCharIndex = getAdjusted60Text(completeText[currIndex:])
    currIndex += lastCharIndex
    line2, newIndexAddition1 = getAdjusted60Text(completeText[currIndex:])
    currIndex += newIndexAddition1
    line3, newIndexAddition2 = getAdjusted60Text(completeText[currIndex:])
    currIndex += newIndexAddition2
    return (line1, line2, line3)

def getAdjusted60Text(completeText):
    result = ""
    for word in completeText.split():
        result += (word) + " "
        if len(result) > 75: 
            return (result, len(result))
    return
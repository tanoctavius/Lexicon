import math

character = #Get inputed character from Controller 
words = #Get words from Controller
time = #Get time from Controller (in minutes)

def getCPM(character, time):
    return character / time 

def getWPM(words, time):
    return words / time 

def createHistogram(..):
    #For each second, keep track of the characters inputed into a list, draw a histogram from that 
import random

'''''''''''''''''''''Paragraph Difficulty'''''''''''''''''''''''''''
def getDifficultyOfWords(input):
    score1 = getConsecutiveConsonantsAndVowels(input)
    score2 = getUniqueWords(input)
    score3 = getAverageLengthOfWords(input)
    total = score1 + score2 + score3

    #Seperating it into levels:
    if total < 30: return "Easy"
    elif total < 45: return "Medium"
    else: 
        return "Hard"

#Difficulty if word has 4 consecutive consonants/ no. of consonants > vowels, it is hard 
#Formula: (5 * (hard words) + 3 * (easy words))
def getConsecutiveConsonantsAndVowels(input):
    lengthOfSentence = len(input)
    completeSentenceDifficulty = 0
    for word in input.split(" "):
        iterativeCharDifficulty = 0 #Determines if it is a hard/ easy word 
        for character in word:
            consCount = 0
            vowelCount = 0
            values = {"a", "e", "i", "o", "u"}
            if getComplexPunctuation(character):
                completeSentenceDifficulty += 0.1
            if character not in values:
                consCount += 1
                if consCount >= 4:
                    iterativeCharDifficulty += 1
                    break
            if character in values:
                vowelCount += 1
        if vowelCount > len(word): 
            iterativeCharDifficulty += 1
        completeSentenceDifficulty += iterativeCharDifficulty
    finalScore = completeSentenceDifficulty // lengthOfSentence
    return completeSentenceDifficulty * 25

def getComplexPunctuation(n):
    values = {"@", "<", ">", "/", "[", "]", "#", "$", "%", "^", "*"}
    if n in values: return True
    return False 

#Getting unique + never seen before words:
def getUniqueWords(input):
    prevWords = set()
    countOfPrevious = 0
    for word in input:
        if word in prevWords:
            countOfPrevious += 1
        prevWords.add(word)
    finalDifference = 25*(countOfPrevious/ len(input))
    return finalDifference

def getAverageLengthOfWords(input):
    totalNumOfChar = 0
    for word in input.split(" "):
        for char in word:
            totalNumOfChar += 1
    average = totalNumOfChar / len(input)
    if average < 4: return 15
    if average < 5.3: return 20
    else: 
        return 25

'''''''''''''''''''''Adjusting Paragraph'''''''''''''''''''''''''''
def getChangedStyle(text, style):
    result = ""
    for word in text.split(" "):
        if style == "crazyCapital":
            temp = ""
            for character in word:
                temp += random.choice((character.upper(), character.lower()))
            result += temp + " "
        
        elif style == "uppercase":
            result += word.upper() + " "
        
        elif style == "normal":
            result += word + " "
        
        elif style == "crazySpaces":
            values = ["@", "<", ">", "/", "[", "]", "#", "$", "%", "^", "*"]
            result += word + random.choice(values)
        
        elif style == "crazyNumbers":
            values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            temp = ""
            for character in word:
                new = random.choice(values)
                temp += random.choice((character, new))
            result += temp + " "
    
        elif style == "mixed":
            tempMixedWord = ""
            tempValues = []
            for character in word:
                tempValues.append(character)
            while len(tempValues) > 0:
                choice = random.choice(tempValues)
                tempValues.remove(choice)
                tempMixedWord += choice
            result += tempMixedWord + " "
    return result[:-1]
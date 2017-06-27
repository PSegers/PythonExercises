'''
Created on 26 jun. 2017

@author: Chryomdar
'''

import time
from random import randint
from random import choice
import requests
from bs4 import BeautifulSoup

def intTest(number):
        try:
            int(number)
            return True
        except TypeError:
            return False

def ex1():
    """
    #Ask for infinite names and ages until "quit". 
    Then calculate when these people become 100 years old.
    """
    
    ageList = []
    nameList = []
    while(True):
        name = input("Enter your name (Enter \"quit\" to quit): ")
        if name == "quit":
            break
        age = input("Enter your age: ")
        if intTest(age) == False:
            print("Please enter a valid number")
            continue
        
        ageList.append(age)
        nameList.append(name)
        
    for i in range(len(ageList)):
        projAge = (100 - int(ageList[i])) + int(time.strftime("%Y"))
        print("{0}, you will be 100 years old in {1}".format(nameList[i],projAge))
    
def ex2():
    """
    Ask for two numbers.
    See if they are odd or even.
    See if they are a multiple of 4.
    See if the second number divides evenly into the first.
    """
    
    test = False
    while(not test):
        test = True
        num1 = input("First number: ")
        num2 = input("Second number: ")
        test1 = intTest(num1)
        test2 = intTest(num2)
        if test1 == False or test2 == False:
            test = False

    if int(num1) % 2 == 0:
        print("The first number {0} is even.".format(num1))
    else:
        print("The first number {0} is odd.".format(num1))
        
    if int(num2) % 2 == 0:
        print("The second number {0} is even.".format(num2))
    else:
        print("The second number {0} is odd.".format(num2))
        
    if int(num1) % 4 == 0:
        print("The first number {0} is divisible by 4.".format(num1))
    else:
        print("The first number {0} is not divisible by 4.".format(num1))
        
    if int(num1) % 4 == 0:
        print("The second number {0} is divisible by 4.".format(num2))
    else:
        print("The second number {0} is not divisible by 4.".format(num2))
        
    if int(num1) % int(num2) == 0:
        print("The first number {0} is divisible by the second number {1}.".format(num1, num2))
    else:
        print("The first number {0} is not divisible by the second number {1}.".format(num1, num2))

def ex3():
    """
    Print all numbers lower than the entered input.
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    
    test = False
    while(not test):
        test = True
        num = input("Enter a number: ")
        test = intTest(num)
    
    for var in a:
        if var < int(num):
            b.append(var)
            
    print(b)

def ex4(num):
    """
    Print all divisors of the entered input.
    """
    #num = int(input("Enter a number: ")) 
    a = range(2, num)
    listDiv = []
    for elem in a:
        if num % elem == 0:
            listDiv.append(elem)
    return listDiv

def ex5():
    """
    Adding both lists together with unique numbers.
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    
    for elem in a:
        if elem not in c:
            c.append(elem)
        
    for elem in b:
        if elem not in c:
            c.append(elem)
            
    print(sorted(c))
    
def ex6():
    """
    Check if word is palindrome.
    """
    word = input("Provide a single word: ")
    revWord = []
    for elem in reversed(word):
        revWord.append(elem)
    revWord = ''.join(revWord)
    if word == revWord:
        print("It's a palindrome alright.")
    else:
        print("The word is not a palindrome.")
    
def ex7():
    """
    Rock, paper, scissors.
    """
    def case_switch(argument):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissors": 2,
        }
        return switcher.get(argument, "rock")
    
    word = ""
    while (word != "quit"):
        word = input ("Your play (type quit to quit): ")
        if word != "scissors" and word != "paper" and word != "rock" and word !="quit":
            continue
        elif word == "quit":
            break
        else:
            aiWord = randint(0, 2)
            playerWord = case_switch(word)
            result = playerWord - aiWord
            if result == 0:
                continue
            elif result == -1 or result == 2:
                print("Player 1 lost!")
            else:
                print("Player 1 won!")
    
def ex8():
    """
    Generate random number between 1-9
    Player guesses until they're right
    Print count of tries
    """
    
    ranNumber = randint(1, 9)
    attempts = 0
    
    correct = False
    while (not correct):
        attempts += 1
        guessNumber = input("Guess a number: ")
        if intTest(guessNumber) == True:
            if int(guessNumber) == ranNumber:
                correct = True
        else:
            correct = True
        
    print("It took you {0} attempts".format(attempts))        

def ex9():
    """
    Seeing which numbers match both lists
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    
    for elemA in a:
        for elemB in b:
            if elemA == elemB:
                c.append(elemB)

    cSet = set(c)
    print(cSet)
    
def ex10():
    """
    Using ex4 to determine whether a given number is a prime number or not.
    """
    number = input("Enter a number: ")
    if len(ex4(int(number))) == 0:
        print("Number {0} is a prime number".format(number))
    else:
        print("Number {0} is not a prime number".format(number))
    
    
def ex11():
    """
    Take a list, add only the last and first value to a new list
    """
    a = [5, 10, 15, 20, 25]
    b = []
    b.append(a[0])
    b.append(a[len(a)-1])
    print(a)
    print(b)
    
def ex12():
    """
    Fibonnaci sequence generator
    """

    count = int(input("How many Fibonacci numbers: "))
    if count == 0:
        seq = []
    elif count == 1:
        seq = [1]
    elif count == 2:
        seq = [1, 1]
    elif count > 2:
        seq = [1, 1]
        for i in range(0, count-2):
            seq.append(seq[i] + seq[i+1])
    print(seq)
    
#Exercises 13 and 14 were easy and its functions are already used in the former exercises.

def ex15():
    """
    Password Generator
    """
    pasLength = int(input("Length of password: "))
    password = []
    for i in range(0, pasLength):
        password.append(choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
    print("".join(password))

def ex16():
    """
    Get all story headers from a url.
    """
    
    url = "https://www.nytimes.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for story_heading in (soup.find_all(class_="story-heading")):
        if story_heading.a: 
            #The stream below will remove all whitespaces and such from the text. There's a lot.
            print(story_heading.a.text.replace("\n", " ").strip())
    
def ex17():
    """
    Cows and Bulls game
    """
    
    ranNum = str(randint(1000, 9999))
    print(ranNum)
    
    cows = 0
    while(cows < 4):
        cows = 0
        bulls = 0
        choosing = True
        while(choosing):
            playNum = str(input("Enter a 4-digit number (\"quit\" to quit): "))
            if playNum == "quit":
                return True
            elif len(playNum) < 4 or len(playNum) > 4:
                print("Please choose a 4-digit number: ")
                continue
            elif not intTest(playNum):
                print("Please choose a 4-digit number: ")
                continue
            else:
                choosing = False
           
        ranList = list(ranNum)
        playList = list(playNum)
    
        for i in range(len(ranList)):
            if ranList[i] == playList[i]:
                cows += 1
            else:
                for j in range(len(playList)):
                    if ranList[i] == playList[j]:
                        bulls += 1    
                        
        print("You have {0} cow(s) and {1} bull(s)".format(cows, bulls))
    
def ex18():
    """
    Show entire text of article in url.
    """
    url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    #The [:-6] is there, because those are the footer <p>'s that snuck in.
    for p in (soup.find_all('p'))[:-6]:
        print(p.text)
        
def ex19():
    """
    See if number is included in list
    """
    
    a = [1, 5, 12, 17, 21, 36, 89, 102]
    b = int(input("Enter a number: "))
    
    for elem in a:
        if elem == b:
            print("Yes, it is included")
            return True
    return False
        
def ex20():
    """
    Write ex16 to a file instead.
    """
    
    url = "https://www.nytimes.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    with open('urltext.txt', 'w') as open_file:
        for story_heading in (soup.find_all(class_="story-heading")):
            if story_heading.a: 
                open_file.write(story_heading.a.text.replace("\n", " ").strip())
                open_file.write("\n")

def ex21():
    """
    List full of data
    Find duplicate data and count how much cases
    """
    sunNames = dict()
    with open('Training_01.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            lineList = line.split("/")
            if lineList[2] in sunNames:
                sunNames[lineList[2]] += 1
            else:
                sunNames[lineList[2]] = 1
        
        print(sunNames.items())

if __name__ == '__main__':
    #ex1()
    #ex2()
    #ex3()
    #ex4()
    #ex5()
    #ex6()
    #ex7()
    #ex8()
    #ex9()
    #ex10()
    #ex11()
    #ex12()
    #Exercises 13 and 14 were easy and its functions are already used in the former exercises.
    #ex15()
    #ex16()
    #ex17()
    #ex18()
    #ex19()
    #ex20()
    ex21()
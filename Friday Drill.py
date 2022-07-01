import random
def startImg():
    print("     +------+ ")
    print("     |      | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("===============")
def headImg():
    print("     +------+ ")
    print("     |      | ")
    print("     O      | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("===============")
def chestImg():
    print("     +------+ ")
    print("     |      | ")
    print("     O      | ")
    print("     |      | ")
    print("     |      | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("===============")
def armLeftImg():
    print("     +------+ ")
    print("     |      | ")
    print("   \ O      | ")
    print("    \|      | ")
    print("     |      | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("===============")
def armRightImg():
    print("     +------+ ")
    print("     |      | ")
    print("   \ O /    | ")
    print("    \|/     | ")
    print("     |      | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("            | ")
    print("===============")
def legLeftImg():
    print("     +------+ ")
    print("     |      | ")
    print("   \ O /    | ")
    print("    \|/     | ")
    print("     |      | ")
    print("    /       | ")
    print("   /        | ")
    print("            | ")
    print("            | ")
    print("===============")
def legRightImg():
    print("     +------+ ")
    print("     |      | ")
    print("   \ O /    | ")
    print("    \|/     | ")
    print("     |      | ")
    print("    / \     | ")
    print("   /   \    | ")
    print("            | ")
    print("            | ")
    print("===============")

def main():
    randomWords = ["grape", "orange", "sun", "moon", "table"]
    choice = random.randint(0, len(randomWords))
    print("Welcome to Hangman!\n")
    legRightImg()
    print()
    mysteryword = ""
    for i in range(len(randomWords[choice])):
        mysteryword += "-"
    mysteryarray = list(mysteryword)
    print(mysteryword)
    messups = 0
    badLetters = ""
    while "-" in mysteryword and messups < 6:
        print("Letters not in word: " + badLetters)
        letter = input("Guess a letter: ")
        hasLetter = False
        for i in range(len(mysteryword)):
            if randomWords[choice][i] == letter:
                mysteryarray[i] = letter
                mysteryword = ''.join(mysteryarray)
                hasLetter = True
        if not hasLetter:
            badLetters += letter + " "
            messups += 1
        imgs = {0 : startImg,
                1 : headImg,
                2 : chestImg,
                3 : armLeftImg,
                4 : armRightImg,
                5 : legLeftImg,
                6 : legRightImg
                }
        imgs[messups]()
        print()
        print(mysteryword)
    if messups >= 6:
        print("Better luck next time!")
    else:
        print("Awesome job! You won!")
    
main()





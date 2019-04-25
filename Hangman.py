"""
*** THE TEXT-BASED ADVENTURE GAME ***
"""
import random


def game():
    print("*** HANG MAN ***\n")
    c = True
    while c:
        d = str(input('Do you want to try & beat the Hang Man? (Y/N) : ')).upper()
        if d == 'Y':
            while c:
                print("\nThen let's get started!\n")
                c = play()
        elif d == 'N':
            c = False
            print("\nSee you later then!\n")
        else:
            print("\nInvalid response! Say 'Y' for YES or 'N' for NO!\n\nAND ONCE AGAIN,")
            c = True
    return None


def play():
    words = ["xylophone", "histamine", "kangaroo", "marsupial", "gigantic", "sapient", "confidence", "juggernaut", "yesterday", "terrestrial", "ostracise", "tantalise", "elegance", "barracuda", "languish", "sanctity", "candidature", "reliance", "geronimo", "apocalypse", "talisman", "harbinger", "fulcrum", "quarantine", "potassium", "zirconium", "deduction", "catastrophe", "internship", "machination", "necromancer", "ultraviolet", "velcro", "wordsworth"]
    cindex = random.randint(0, len(words))
    challenge = str(words[cindex]).upper()
    chalen = len(challenge)
    lifelines = 3
    i = 0
    gprogress = []
    while i < chalen:
        gprogress.append('?')
        i += 1
    print(gprogress)
    ccount = 0
    m = True
    while (not lifelines < 0) and m:
        ccount = 0
        g = str(input("\nMake your guess! : ")).upper()
        glen = len(g)
        if glen == 1:
            if g in gprogress:
                print("\nYou have already guessed it earlier!\n")
                ccount += 1
            else:
                j = 0
                while j < chalen:
                    if g == challenge[j]:
                        gprogress[j] = challenge[j]
                        ccount += 1
                    j += 1
                print(gprogress)
            if ccount == 0:
                lifelines -= 1
                if not lifelines < 0:
                    print("\nWrong guess! Only "+str(lifelines)+" lifeline(s) left!\n")
                ccount = 0
        else:
            print("Please input only a single character!\n")
            ccount = 0
        for i in range(chalen - 1):
            if gprogress[i] == '?':
                m = True
                break
            else:
                m = False
    r = 0
    for item in gprogress:
        if item == '?':
            r -= 1
    if r == 0:
        print("\nYOU WON!")
    else:
        print("\nYOU LOST!\n\nThe word was actually: ")
        print(challenge)
    choice = True
    choice2 = True
    while choice2:
        d = str(input('\nDo you want to play again? (Y/N): ')).upper()
        if d == 'Y':
            choice = True
            choice2 = False
        elif d == 'N':
            choice = False
            choice2 = False
        else:
            print("Invalid choice! Say 'Y' for YES or 'N' for NO! And ONCE AGAIN I ask :")
            choice2 = True
    return choice


def main():
    game()
    return None


if __name__ == '__main__':
    main()

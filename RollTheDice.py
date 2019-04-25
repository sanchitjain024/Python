import random


def roll_dice():
    choice = True
    selection = ''
    while not choice == False:
        try:
            n = int(input('Please input the no. of sides (at least 2) required on the dice you want to roll: '))
            if n > 1:
                print('\nNow let us roll this dice !\n')
                print('The number on the dice is : ', str(random.randint(1,n)))
                selection = ''
                while not selection == 'N':
                    selection = str(input('\nDo you want to roll the dice again? (Y/N) : ')).upper()
                    if selection == 'N':
                        print("\nThanks for rolling the dice! Goodbye!\n")
                        choice = False
                    elif selection == 'Y':
                        selection = 'N'
                        choice = True
                    else:
                        print('\nInvalid selection! Please input either "Y" or "N"!\n')
            else:
                print('\nNo. of sides of dice, cannot be less than 2! Please provide an appropriate input.\n')
                selection = ''
                choice = True
        except TypeError:
            print('\nInvalid selection! Please provide appropriate input!\n')
            choice = True
        except ValueError:
            print('\nInvalid selection! Please provide appropriate input!\n')
            choice = True


def main():
    print("*** DICE ROLLING PLATFORM ***\n\n")
    roll_dice()
    return None


if __name__ == '__main__':
    main()

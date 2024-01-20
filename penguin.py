# A fun adaptation of an Innocent post on Penguin Awareness Day. Thank you, Innocent Drinks, for the inspo.

yes = 'yes'
no = 'no'

print("Is this a penguin? Lert's find out...")
print("Is it black and white?")
answer = input()

if answer == yes:
    print("is it one of 101?")
    answer = input()
    if answer == yes:
        print("It's a dalmation")
    else:
        print("Can it fly?")
        answer = input()
        if answer == yes:
            print("Is it bad luck?")
            answer = input()
            if answer == yes:
                print("It's a magpie.")
            else:
                print("It's a zebra on a plane.")   
        else:
            print("Does it waddle?")
            answer = input()
            if answer == yes:
                print("Is it wearing a nappy?")
                answer = input()
                if answer == yes:
                    print("It's a baby wearing a tux!")
                else:
                    print("IT'S A PENGUIN!")
            else:
                print("It's a newspaper.")
else:
    print("It is not a penguin.")
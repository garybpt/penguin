# I asked ChatGPT how I could condense my script.


def ask_question(question):
    print(question)
    return input().lower() == 'yes'

print("Is this a penguin? Let's find out...")

if ask_question("Is it black and white?"):
    if ask_question("Is it one of 101?"):
        print("It's a dalmatian.")
    elif ask_question("Can it fly?"):
        if ask_question("Is it bad luck?"):
            print("It's a magpie.")
        else:
            print("It's a zebra on a plane.")
    else:
        if ask_question("Does it waddle?"):
            if ask_question("Is it wearing a nappy?"):
                print("It's a baby wearing a tux!")
            else:
                print("IT'S A PENGUIN!")
        else:
            print("It's a newspaper.")
else:
    print("It is not a penguin.")
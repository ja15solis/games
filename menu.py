from hangman import hangman

while True:
    txt = """Hi welcome to Javier's games.\n
    (1) Hangman
    (2) ConnectFour\n
    Please select one number to play a game or 'q' to quit: """

    value = input(txt)
    if value == '1':
        hangman()
    elif value == '2':
        pass
    elif value == 'q' or value == 'Q':
        break
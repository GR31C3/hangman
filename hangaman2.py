import random

#set up list possibile
word_list = ["dog", "coffee", "swan", "rose", "goverment"]

#player1 start game

player1 = input("Insert your name")
print(f"Welcome {player1}. Let's play!")
while True:
#computer choice
    computer_choice = random.choice(word_list)


#start game
    word = computer_choice     
    letter = len(word)
    print(f'Your word has {letter} letters')

#set up the game
    allowe_errors = 15
    guesses = []
    done = False
#loop
    while not done:
        guess = input(f"allowed errors left {allowe_errors}, insert a letter ")
        guesses.append(guess.lower())
        for letter in computer_choice:
            if letter.lower() in guesses:
                print(letter, end="")
            else:
                print("_ ", end="")
        print("")
        if guess.lower() not in computer_choice.lower():
            allowe_errors -= 1
    
            if allowe_errors == 0:
                break
        done = True
        for letter in computer_choice:
            if letter.lower() not in guesses:
                done = False
#end the game
    if done:
        print(f"You win! The word was {computer_choice}.")
    else:
        print(f"Game over! The word was {computer_choice}. ")

    user_input = input('Enter yes or no to continue: ')
    user_input.lower()
    answer1 = ['yes', 'y', 'YES', 'Y'] 
    answer2 = ['no', 'n', 'NO', 'N']
    if user_input in answer1:
        print('new game')
        continue
    elif user_input in answer2:
        print('Good bye')
        break
    else:
        print('please enter YES or NO')
input('Press ENTER to exit')
        
    

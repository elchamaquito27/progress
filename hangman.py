import random
def main():
    secret_word = (random.choice(open("words.txt", "r").readline().split()))  # list of words
    # randomly select a word
    characters = "abcdefghijklmnopqrstuvwxyz"
    guess = 0
    guessSecret = ''
 # guessSecret to display
    for e in secret_word:
        if e.lower() in characters:
            guessSecret = guessSecret+'_'+' '
    # list of letters guessed
    letters_guessed = []
    print('Welcome to the Hangman Game !')
    print('The secret sentence is '+guessSecret)
    print("Number of guesses remaining : 6")
    # loop to continue till there are some letters not guessed and total chance is not completed
    while(guess < 6 and ('_' in guessSecret)):
        letter = input('\n Please enter a letter : ')  # input the letter
        if letter not in letters_guessed:  # if letter has already been guessed then display message letter already used add to lettersGuessed list
            letters_guessed.append(letter)
        if letter.lower() in secret_word.lower():  # check if letter present in secret
            count = 0
            for i in range(0, len(secret_word)):  # update the guessSecret with the letter guessed
                if(secret_word[i].lower() == letter.lower()):

                    count = count + 1

                    guessSecret = guessSecret[0:2*i] + \
                        secret_word[i]+guessSecret[2*i+1:len(guessSecret)]

        guess = guess + 1
        print('The secret sentence is : '+guessSecret)
        print('Letters used thus far : '+str(letters_guessed))
        print('Number of guesses remaining : '+str(6-guess))
    # check if user was able to guess the word or not
    if('_' not in guessSecret):
        print("Congratulations you guessed the sentence")
    else:
        print("You lose.The secret word is "+secret_word)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
# calling the function
main()
# end of program
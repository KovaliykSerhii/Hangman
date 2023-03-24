from random import choice

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

max_wrong = len(HANGMAN) - 1
WORDS = ("cat", "fish", "app", "milk", "monika", "love", "man", "hangman", "game", "snake", "suicide")  # Words to guess

word = choice(WORDS)  # The word to guess
so_far = "_" * len(word)  # One dash for each letter in the word to be guessed
wrong = 0  # Number of incorrect assumptions made by the player
used = []  # The letters have already been guessed.

while wrong < max_wrong and so_far != word:
    print(HANGMAN[wrong])  # Displaying the Hangman by Index
    print("\nYou used the following letters:\n", used)
    print("\nAt the moment the word looks like this:\n", so_far)

    guess = input("\n\nEnter your guess: ")  # The user enters the expected letter

    while guess in used:
        print("You have already entered a letter", guess)  # If a letter has already been entered before, we output the corresponding message
        guess = input("Enter your guess: ")  # The user enters the expected letter

    used.append(guess)  #The entered letter is added to the list of used letters

    if guess in word:  # If the letter you entered is in the target word, we display the corresponding message
        print("\nYes!", guess, "is in the word!")
        new = ""
        for i in range(len(word)):  # In the loop we add the found letter in the right place
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nSorry, this letter\"" + guess + "\" not in the word.")  # If there is no letter, then print the corresponding message
        wrong += 1

if wrong == max_wrong:  # If a player exceeds the number of errors, he is hung
    print(HANGMAN[wrong])
    print("\nYou were hanged!")
else:  # If the number of errors is not exceeded, the player has won
    print("\nYou guessed the word!")

print("\nThe word that was guessed was \"" + word + '\"')
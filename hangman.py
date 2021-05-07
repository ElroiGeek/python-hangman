import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
@@ -54,8 +56,10 @@ def play(word):
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
@@ -64,6 +68,7 @@ def display_hangman(tries):
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
@@ -73,6 +78,7 @@ def display_hangman(tries):
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
@@ -82,6 +88,7 @@ def display_hangman(tries):
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
@@ -91,6 +98,7 @@ def display_hangman(tries):
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
@@ -100,6 +108,7 @@ def display_hangman(tries):
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
@@ -109,6 +118,7 @@ def display_hangman(tries):
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
@@ -129,5 +139,6 @@ def main():
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
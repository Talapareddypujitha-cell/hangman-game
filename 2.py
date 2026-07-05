import random

words = ["python", "apple", "computer", "program", "coding"]
word = random.choice(words)

guessed_letters = []
wrong_attempts = 6

print("===================================")
print("       WELCOME TO HANGMAN")
print("===================================")

while wrong_attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong Attempts Left:", wrong_attempts)
    print("Guessed Letters:", guessed_letters)

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_attempts -= 1
        print("❌ Wrong Guess!")

if wrong_attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing Hangman!")
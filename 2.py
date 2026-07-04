import random

words = ["python", "apple", "computer", "program", "coding"]
word = random.choice(words)

guessed = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("💀 Game Over! The word was:", word)
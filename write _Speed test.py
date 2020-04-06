#https://stackoverflow.com/questions/47954657/python-continue-from-input-with-the-space-key
import time
import random
import sys

def custom_input(prefix=""):
    """Custom string input that submits with space rather than enter"""
    concatenated_string = ""
    sys.stdout.write(prefix)
    sys.stdout.flush()
    while True:
        key = ord(getch())
        # If the key is enter or space
        if key == 32 or key == 13:
            break
        concatenated_string = concatenated_string + chr(key)
        # Print the characters as they're entered
        sys.stdout.write(chr(key))
        sys.stdout.flush()
    return concatenated_string

score = 0
start_time = int(time.time())
characters = 0
words = 0
current_word = random.choice(words)
next_word = random.choice(words)
while (int(time.time()) - start_time) <= TIME_LIMIT:
    os.system('cls')
    print(f"Your word is {current_word}")
    print(f"The next word will be {next_word}")
    print(f"Your current score is {score}")
    attempt = input("> ")
    if attempt.lower() == current_word.lower():
        score = score + 1
        words = words + 1
        characters = characters + len(current_word)
    current_word = next_word
    next_word = random.choice(words)
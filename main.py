import random
from words import words_list
# Error handling


def main():
    print("WORDLE Command Line Version")
    print("Press Enter to start")
    print("Enter q to quit")
    user = input()
    while(user == ""):
        game_loop()
        print("Enter q to quit")
        user = input("Press Enter to start")

def letters_left(word:str, letters: list, actual_word) -> str:
    word = [x.upper() for x in word]
    actual = [x.upper() for x in actual_word]
    for i in range(len(word)):
        if word[i] in actual:
            pass
        else:
            try:
                letters.remove(word[i])
            except ValueError:
                continue
    return " ".join(letters)


def game_loop():
    # 65 90
    letters = [chr(i) for i  in range(65,91)]
    r = random.randint(0,len(words_list) -1)
    actual_word = words_list[r]
    print("Wordle CMD Verison")
    print("Guess a 5 letter word")
    game_count = 0
    while game_count <= 4:
        word = get_user_guess(input())
        while not word:
            word = get_user_guess(input("Please enter 5 letter word: "))
        result = check_user_guess(word, actual_word)
        if isinstance(result, bool):
            print("YOU ARE A WINNER")
            print(word)
            break
        else:
            print(f"Tries Remaining: {5 - game_count}")
            print(" ".join(x for x in word))
            print("".join(result))
            print(letters_left(word, letters, actual_word))
        game_count+=1
    print("GAME OVER")
    if game_count == 5:
        print(f"Word was {actual_word}")
    print("\n")


def get_user_guess(word: str):
    if len(word) > 5 or len(word) < 5:
        print("Bad Word")
        return
    return word

def check_user_guess(user_word: str, actual_word: str):
    if user_word.upper() == actual_word.upper():
        return True
    return check_word_hints(user_word, actual_word)
    
    # Add logic to see if the letters in correct spot or incorrect position

def check_letter_wrong_place(word_list: list, actual_list: list, result: list):
    
    
    for i in range(len(word_list)):
        if word_list[i] in actual_list and result[i] == "🟥":
            result[i] = "🟧"
    return result

def check_word_hints(user_word: str, actual_word: str):
    user_word_list = [i.upper() for i in user_word]
    actual_word_list = [i.upper() for i in actual_word]

    result = ["","","","","",]
    # Check if letter in correct space
    for i in range(len(user_word_list)):
        if user_word_list[i] == actual_word_list[i]:
            result[i] = "✅"
        else:
            result[i] = "🟥"
    
    return check_letter_wrong_place(user_word_list, actual_word_list, result)




main()
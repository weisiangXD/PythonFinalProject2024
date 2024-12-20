import random
import time

def translate_to_traditional_chinese(text):
    translations = {
        "Type out as many of the displayed words as quickly and correctly as you can. Every word is worth 1 point and every phrase is 2 points. Getting any of them wrong is minus 1 point.": "盡可能快速且正確地輸入顯示的單字或短語。每個單字得1分，每個短語得2分。輸入錯誤將扣1分。",
        "Press 'Enter' when ready": "準備好後按下 'Enter' 鍵"
    }
    return translations.get(text, text)

def main():
    dictionary = ["cat", "dog", "elephant", "lion", "tiger", "bear", "giraffe", "zebra", "rabbit", "horse", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "apple", "banana", "orange", "grape", "mango", "pineapple", "pear", "peach", "watermelon", "strawberry", "phone", "laptop", "desk", "chair", "pen", "notebook", "bag", "car", "bike", "clock", "television", "remote", "bottle", "glass", "mirror", "pillow", "lamp", "shoes", "door", "window", "Instagram", "TikTok", "WhatsApp", "Snapchat", "YouTube", "sports", "badminton", "basketball", "table tennis", "volleyball", "rugby", "swimming", "I study at NTOU", "I love Taiwan", "I major in Computer Science"]

    print("Type out as many of the displayed words as quickly and correctly as you can. CAPITAL LETTER SENSITIVE!! Every word is worth 1 point and every phrase is 3 points. Getting any of them wrong is minus 1 point.\n")
    print("盡可能快速、正確地輸入盡可能多的顯示單字。對大小寫敏感！！每個單字得 1 分，每個片語得 3 分。其中任何一個錯誤扣 1 分。\n")

    print("Press 'Enter' when ready")

    input() # waits on player to input "Enter" and then it starts the game

    score = 0 # score starts out at zero
    start_time = time.time() # implements the the time given to get as many correct as you can
    elapsed_time = 0 # pretty self-explanatory

    print("Game start!")

    while elapsed_time < 30: # runs the following while there is time left (in this case, under 30 seconds)
        word = random.choice(dictionary) # chooses a random value in the dictionary provided above
        print(word) # shows the random word
        user_input = input("Your answer: ").strip() # takes the players input. ".strip" removes any extra spaces that the player puts in

        if user_input == word: # if the player inputs the correct word
            score += 3 if " " in word else 1 # adds 3 points if it is a phrase (in this case it's looking if it has spaces in between words) otherwise it adds 1 point
            print("Correct!")
        else:
            score -= 1 # if incorrect takes away 1 point for either option
            print("Incorrect!")

        dictionary.remove(word) # deletes the word/phrase what was randomly chosen
        print(f"Current score: {score}\n")

        elapsed_time = time.time() - start_time

    print("Time's up!")
    print(f"Your final score is: {score}")

if __name__ == "__main__":
    main()
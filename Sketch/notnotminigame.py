import random
import time

key_to_direction = {
    "w": "Up",
    "s": "Down",
    "a": "Left",
    "d": "Right"
}

directions = [
    ("Left", "a"),
    ("Right", "d"),
    ("Up", "w"),
    ("Down", "s")
]

score = 0
game_duration = 30

print("Instructions (指示):")
print("\n'Left' means type 'a', 'Not Left' means type anything BUT 'a'.")
print('“左”表示鍵入“a”，“非左”表示鍵入除“a”以外的任何內容。')
print("\nw = up : s = down : a = left : d = right")
print("\nThe game lasts 30 seconds. The timer starts after when you press 'Enter'!")
print('比賽持續30秒。當您按下“Enter”鍵後，計時器開始計時&#xff01;')
print("\nPress Enter when ready")
print('準備好後按 Enter 鍵')
print("\nInspired by Mobile game 'Not Not'")
print("\n")

input() #waits for user input

print("START!")

start_time = time.time()

while time.time() - start_time < game_duration:
    is_not = random.choice([True, False])
    direction, correct_key = random.choice(directions)
    instruction = f"Not {direction}" if is_not else direction

    print(f"\nInstruction: {instruction}")
    user_input = input("Your move: ").strip()

    if is_not:
        if user_input != correct_key:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            score -= 1
    else:
        if user_input == correct_key:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            score -= 1

print("\nTime's up!")
print(f"Your final score is: {score}")
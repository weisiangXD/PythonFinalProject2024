import random

def guess_the_number():
    print("歡迎來到猜數字遊戲！")
    print("我會隨機選一個1到100的數字，你需要猜出它是什麼。")
    print("如果猜錯了，我會告訴你答案是更大還是更小。")

    # 隨機生成1到100之間的數字
    number_to_guess = random.randint(1, 100)
    attempts = 0  # 記錄嘗試次數

    print("請輸入1到100之間的數字。")
    x = 100
    y = 1

    while True:
        try:
            # 玩家輸入猜測數字
            guess = int(input("請輸入你的猜測： "))
            attempts += 1

            if guess < number_to_guess:
                print("太小了！再試一次。")
                print(f"請輸入 {guess} 到 {x} 之間的數字。")
                y = guess
            elif guess > number_to_guess:
                print("太大了！再試一次。")
                print(f"請輸入 {y} 到 {guess} 之間的數字。")
                x = guess
            else:
                print(f"恭喜你猜中了！答案是 {number_to_guess} 。")
                print(f"你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入有效的數字！")

if __name__ == "__main__":
    guess_the_number()

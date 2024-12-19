import random
import time

def show_numbers():
    numbers = [random.randint(0, 9) for _ in range(6)]  # 生成N個隨機數字
    print("請記住這四個數字:")
    print("".join(map(str, numbers)))  # 顯示數字，沒有空格
    time.sleep(2)  # 等待2秒
    print("\n" * 50)  # 清空屏幕

    return numbers

def countdown():
    # 倒數 3, 2, 1
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

def main():
    print("歡迎來到 '跟我這樣做' 遊戲！")
    print("請輸入 1 來開始遊戲。")
    
    start_input = input()
    if start_input != "1":
        print("無效輸入，遊戲結束。")
        return
    
    time.sleep(1)

    # 開始倒數
    countdown()

    # 顯示並記住四個數字
    numbers_to_remember = show_numbers()

    # 要求玩家輸入相同的數字
    user_input = input("請輸入你記得的數字和順序：")
    
    # 處理輸入
    try:
        user_numbers = [int(num) for num in user_input]  # 把每個字符轉換為數字
    except ValueError:
        print("輸入無效，請只輸入數字。")
        return

    # 檢查結果
    if user_numbers == numbers_to_remember:
        print("恭喜！你答對了！")
    else:
        print("很遺憾，你答錯了！正確的數字是：", "".join(map(str, numbers_to_remember)))

if __name__ == "__main__":
    main()

import random
import time

# 顯示四個隨機數字的函數
def show_numbers():
    # 隨機生成四個 0 到 9 之間的數字
    numbers = [random.randint(0, 9) for _ in range(4)]
    
    # 顯示這些數字，並將它們合併成一個無空格的字符串
    print("請記住這四個數字:")
    print("".join(map(str, numbers)))  # 將數字轉換為字符串並顯示
    time.sleep(2)  # 等待2秒鐘讓玩家記住數字
    print("\n" * 50)  # 清空屏幕，將數字隱藏

    return numbers  # 返回這些數字，供後續比對使用

# 倒數計時函數
def countdown():
    # 從 3 開始倒數到 1
    for i in range(3, 0, -1):
        print(i)  # 顯示倒數的數字
        time.sleep(1)  # 每次倒數等待1秒鐘

# 主遊戲邏輯
def main():
    print("歡迎來到 '跟我這樣做' 遊戲！")  # 顯示遊戲歡迎語
    print("請輸入 1 來開始遊戲。")  # 提示玩家輸入 1 來開始遊戲
    
    start_input = input()  # 接受玩家的輸入
    if start_input != "1":  # 如果玩家輸入的不是 1，遊戲結束
        print("無效輸入，遊戲結束。")
        return  # 結束程式

    time.sleep(1)  # 等待1秒，準備開始倒數

    # 開始倒數
    countdown()

    # 顯示四個隨機數字並讓玩家記住
    numbers_to_remember = show_numbers()

    # 提示玩家輸入他們記得的數字
    user_input = input("請輸入你記得的數字和順序：")
    
    try:
        # 將玩家輸入的每個字符轉換為整數，並儲存成一個數字列表
        user_numbers = [int(num) for num in user_input]  
    except ValueError:
        # 如果玩家輸入了無效的字符，顯示錯誤提示
        print("輸入無效，請只輸入數字。")
        return  # 結束程式

    # 檢查玩家輸入的數字是否與顯示的數字相同
    if user_numbers == numbers_to_remember:
        print("恭喜！你答對了！")  # 如果答案正確，顯示成功訊息
    else:
        # 如果答案錯誤，顯示正確的數字
        print("很遺憾，你答錯了！正確的數字是：", "".join(map(str, numbers_to_remember)))

# 程式執行的入口
if __name__ == "__main__":
    main()  # 呼叫 main 函數開始遊戲

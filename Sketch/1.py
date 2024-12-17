import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import random
import csv


# 加载等待动画函数
def loading(waitTIME):
    rpack = random.randint
    progress = [rpack(0, 24), rpack(25, 49), rpack(50, 74), rpack(75, 98), '99', '100']
    cd = float(waitTIME / 6)
    for i in range(0, 6):
        print(f"loading {progress[i]}%")
        time.sleep(cd)


# 随机数生成器
def Rnumber():
    currentTIME = float(time.time())
    random.seed(currentTIME)
    return random.randint(0, 9)


# 游戏类
class Games:
    def __init__(self):
        self.score = 0

    def simplemath(self):
        ans_string = '1+1'
        ans = 1 + 1
        return self.ask_question(ans_string, ans, 1)

    def simplemath2(self):
        ans_string = '2+1'
        ans = 2 + 1
        return self.ask_question(ans_string, ans, 2)

    def ask_question(self, ans_string, correct_ans, score_increment):
        player_input = simpledialog.askinteger("问题", f"请输入答案 {ans_string} 等于多少？")
        if player_input == correct_ans:
            self.score += score_increment
            messagebox.showinfo("结果", "答案正确！")
        else:
            messagebox.showerror("结果", f"答案错误！正确答案是 {correct_ans}！")
        return self.score


# 名人堂类
class HallOfFame:
    def __init__(self):
        self.data = []
        self.seq = 1

    def add(self, uname, score):
        self.load("leaderboard.csv")
        self.data.append({'UID': self.seq, 'uname': uname, 'score': score})
        self.seq += 1

    def sort(self):
        self.data = sorted(self.data, key=lambda x: x['score'], reverse=True)

    def save(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['UID', 'uname', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for DATA in self.data:
                writer.writerow(DATA)

    def load(self, filename):
        try:
            with open(filename, 'r') as READfile:
                reader = csv.DictReader(READfile)
                self.data = []
                for row in reader:
                    self.data.append({'UID': int(row['UID']), 'uname': row['uname'], 'score': float(row['score'])})
                self.seq = len(self.data) + 1
        except:
            self.save("leaderboard.csv")

    def display(self):
        self.load("leaderboard.csv")
        self.sort()
        leaderboard = "\n".join([f"TOP {idx+1}: {row['uname']} - {row['score']}" for idx, row in enumerate(self.data)])
        messagebox.showinfo("排行榜", leaderboard)

    def save_data(self, score):
        self.load("leaderboard.csv")
        while True:
            playerNAME = simpledialog.askstring("名人堂", "请输入您的用户名称：")
            if not any(row['uname'] == playerNAME for row in self.data):
                self.add(playerNAME, score)
                self.sort()
                self.save("leaderboard.csv")
                messagebox.showinfo("成功", "您的分数已成功存入名人堂！")
                break
            else:
                messagebox.showerror("错误", "用户名称已存在，请重新输入。")

    # 管理员模式功能
    def admin_mode(self):
        while True:
            playerNAME = simpledialog.askstring("管理员模式", "请输入用户名称：")
            if playerNAME:
                playerSCORE = simpledialog.askfloat("管理员模式", f"请输入 {playerNAME} 的分数：")
                if playerSCORE is not None:
                    self.add(playerNAME, playerSCORE)
                    self.sort()
                    self.save("leaderboard.csv")
                    messagebox.showinfo("成功", f"管理员已成功添加用户 {playerNAME} 的分数！")
                    break
            else:
                messagebox.showerror("错误", "用户名不能为空！")


# 主窗口类
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("How Fast Are You?")
        self.geometry("600x400")
        self.configure(bg="black")
        self.button_font = ("Arial", 14, "bold")
        self.games = Games()
        self.hall_of_fame = HallOfFame()
        self.init_main_menu()

    def init_main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        # 标题
        tk.Label(self, text="How Fast Are You?", font=("Arial", 20, "bold"), bg="black", fg="white").pack(pady=20)

        # 按钮
        tk.Button(self, text="开始游戏", command=self.start_game, font=self.button_font,
                  bg="gray", fg="white", width=20, height=2).pack(pady=10)
        tk.Button(self, text="查看排行榜", command=self.show_leaderboard, font=self.button_font,
                  bg="gray", fg="white", width=20, height=2).pack(pady=10)
        tk.Button(self, text="管理员模式", command=self.admin_mode, font=self.button_font,
                  bg="red", fg="white", width=20, height=2).pack(pady=10)
        tk.Button(self, text="退出", command=self.quit, font=self.button_font,
                  bg="gray", fg="white", width=20, height=2).pack(pady=10)

    def start_game(self):
        i = 2
        while i > 0:
            dice = Rnumber()
            if dice < 5:
                self.games.simplemath()
            else:
                self.games.simplemath2()
            i -= 1
        self.end_game()

    def end_game(self):
        option = messagebox.askyesno("游戏结束", "恭喜！您已完成游戏，是否将分数存入排行榜？")
        if option:
            self.hall_of_fame.save_data(self.games.score)
        else:
            messagebox.showinfo("分数", f"您的最终分数是: {self.games.score}")
        self.games.score = 0
        self.init_main_menu()

    def show_leaderboard(self):
        self.hall_of_fame.display()

    def admin_mode(self):
        admin_code = simpledialog.askinteger("管理员验证", "请输入管理员模式代码：")
        if admin_code == 10086:
            self.hall_of_fame.admin_mode()
        else:
            messagebox.showerror("错误", "管理员代码错误！")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

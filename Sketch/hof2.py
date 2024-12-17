import csv

class hof1():
    def __init__(self):
        self.data = []
        self.seq = 1 #sequence number用于辨认这是第几位存入的用户

    def sort(self): #排大小
        self.data = sorted(self.data, key=lambda x: x['score'], reverse=True)

    def add(self,uname,score): # 序列号,用户名,分数
        self.data.append({'id': self.seq, 'uname': uname, 'score': score})

    def save(self):
        filename = "leaderboard.csv"
        with open(filename, 'r+', newline= '') as csvfile:
            fieldnames = ['id', 'uname', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            

            writer.writeheader()
            for j in self.data:
                writer.writerow(j)


    def display(self): #显示排行榜
        self.load() 
        self.sort()
        print("名人堂:")
        for i in self.data:
            print(f"ID: {i['id']}, User ID: {i['uname']}, Score: {i['score']}")

    def load(self, filename="leaderboard.csv"):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            max_seq = 0
            self.data = []
            for row in reader:
                readDATA = {'id': int(row['id']), 'uname': row['uname'], 'score': int(row['score'])}
                self.data.append(readDATA)
                if readDATA['id'] > max_seq:
                    max_seq = readDATA['id']
            self.seq = max_seq + 1  # 更新最大的序列号，以便保持唯一性

    def save_score(self, uname, score):
        print("恭喜！您已获得进入名人堂的资格，是否将自己的分数与其他人一较高下？")
        option = input("'Yes' or 'No' ? Y/N: ")
        if option.upper() == 'N':
            print("您的分数将被初始化，感谢游玩！")
            score = 0
        elif option.upper() == 'Y':
            self.add(uname, score)
            self.sort()
            self.save()
            print("您的分数已成功存入名人堂！")


def leaderboard_console():
    hof = hof1()
    option = int(input("↓我是菜单(排行榜debugger)↓\n1.添加分数\n2.查看排行榜\n"))

    match option:
        case 1:
            playerNAME = str(input("输入用户名称\n"))
            playerSCORE = int(input("输入用户分数\n"))
            hof.save_score(playerNAME, playerSCORE)
        case 2:
            hof.display()

# 运行菜单控制台
while(1):
    leaderboard_console()
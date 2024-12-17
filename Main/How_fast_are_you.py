import time
import csv 
import random


#Function definition zone START

def loading(waitTIME): 
    rpack = random.randint
    progress = [rpack(0,24),rpack(25,49),rpack(50,74), rpack(75,98), '99', '100']
    cd = float(waitTIME / 6)
    for i in range(0,6):
        print(f"loading {progress[i]}%")
        time.sleep(cd)

def Rnumber():   
    currentTIME = float(time.time()) #fetching current time
    random.seed(currentTIME) #using current time as random number generator seed.

    randomNUM = random.randint(0,9) #random number are int(0~9)

    return randomNUM #return value

class games():
    def __init__(self,score): #initialize user data.
        self.score = score
    
    def simplemath(self):
        ans_string = '1+1'
        ans = 1 + 1
        player_input = int(input(f'请输入答案{ans_string}等于多少: '))
        if player_input == ans:
            self.score += 1
            print("答案正确！")
            print(f'你目前的分数为{self.score}')
        else:
            print(f"答案错误！正确答案是{ans}!")
            print(f'你目前的分数为{self.score}')
        return self.score

    def simplemath2(self):
        ans_string = '2+1'
        ans = 2 + 1
        player_input = int(input(f'请输入答案{ans_string}等于多少: '))
        if player_input == ans:
            self.score += 2
            print("答案正确！")
            print(f'你目前的分数为{self.score}')
        else:
            print(f"答案错误！正确答案是{ans}!")
            print(f'你目前的分数为{self.score}')
        return self.score
    #def game2():

#HallOfFame()使用手册
#主资料变数为列表形态 HallOfFame().data，里面存了三笔资料: UID,uname,score，分别对用户ID，用户名称以及用户分数。
#HallOfFame().add() 可能会是你各位最常调用的功能，以下是解释与范例
#这个函数要吃两个变数，分别是用户名uname以及用户分数score
#例子(用户名=weisiang, 分数=99):游戏结算阶段时调佣 HallOfFame().add(weisiangXD,99)将玩家加入排行榜里。
class HallOfFame():
    def __init__(self):
        self.data = []
        self.seq = 1 #Initialize sequence number, use for determine amount of data has been saved.

    def add(self, uname, score):
        self.load("leaderboard.csv") #添加分数之前先读取文件。
        self.data.append({'UID': self.seq, 'uname': uname, 'score': score})
        self.seq += 1

    def sort(self):
        self.data = sorted(self.data, key=lambda x: x['score'], reverse=True) #key=数值大小做排序，reverse=True表示从小排到大

    def save(self, filename):
        with open(filename, 'w', newline='') as csvfile: # 'w' 模式为从文件的头部开始写入，若文件不存在，则创建文件。
            fieldnames = ['UID', 'uname', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader() #建立header row
            for DATA in self.data:
                writer.writerow(DATA) #写入资料

    def load(self, filename):
        try:
            with open(filename, 'r') as READfile: # 'r' 模式为从文件的开头读取
                reader = csv.DictReader(READfile)
                max_seq = 0 #创建最大序号变数，用于找出文件内已存在的资料笔数
                self.data = [] #初始化主资料列表
                for row in reader:
                    data_row = {'UID': int(row['UID']), 'uname': row['uname'], 'score': float(row['score'])}
                    self.data.append(data_row)
                    if data_row['UID'] > max_seq:
                        max_seq = data_row['UID']
                self.seq = max_seq + 1 #从最新的文件资料从找出记录最大笔数后+1，确保self.seq不与文件内的序号冲突
        except:
            self.save("leaderboard.csv")
            print("\n排行榜资料丢失！请向管理员反映！\n")

    def display(self): #打印出排行榜
        self.load("leaderboard.csv") #加载文件
        self.sort() #排序
        print("\n[HOF]排行榜：", end = "\n")
        top = 1
        for printer in self.data:
            result = f"\n[HOF]|TOP {top:>1}    |Player: {printer['uname']:<12}    |Score：{printer['score']:<6}"
            print(result, end="")
            top += 1
        print("\n")

    def save_data(self,mode,score): #功能模式 10086为管理员模式，可以手动添加分数，1为正常模式。
        self.load("leaderboard.csv")
        while 1: #无限循环直到我想干的事完成   
            if mode == 10086:
                playerNAME = str(input("\n[HOF_ADMIN]请输入您的用户名称\n"))
            else:
                playerNAME = str(input("\n[HOF]请输入您的用户名称\n"))
            name_exists = any(checkNAME['uname'] == playerNAME for checkNAME in self.data)
            if name_exists:
                print("\n[HOF]用户名称已存在！")
            else:
                print("\n[HOF]太好了！用户名称可用！\n")
                break

        if mode == 10086:
            playerSCORE = float(input("\n[HOF_ADMIN]输入用户分数\n"))
            self.add(playerNAME, playerSCORE)
        else:
            self.add(playerNAME, score)
        self.sort()
        self.save("leaderboard.csv")
        print("\n[HOF]您的分数已成功存入名人堂！")

    #管理员使用的后台程序。
    def leaderboard_console(self): 
        option = int(input("\n[HOF]↓我是菜单(排行榜debugger)↓\n{:<5}1.添加分数\n{:<5}2.查看排行榜\n".format('','')))

        match option:
            case 1:
                self.save_data(10086, 0)
            case 2:
                self.display()


#Function definition zone END

#Menu START

while 1:
    option = int(input("↓我是菜单↓\n1.开始游戏\n2.查看分数排行榜\n3.查看Credit\n"))

    loading(2)

    if option > 3 and option != 10086:
        print("未知功能！请重新选取！")
        continue

    match option:
        case 1: #proceed to MAIN program section
            break 
        
        case 2: #查看名人堂。
            HallOfFame().display()

        case 3: #Credit
            print("")
            print("-制作人员-")
            print("队名：APPLE（第十九组）")
            print("队长：林伟翔01257174\n队员：陈科宇01257175、林承濬01257171")
            print("")
            continue

        case 10086:
            HallOfFame().leaderboard_console()
            continue





    #print("欢迎游玩HowFastAreYou小游戏，在这游戏里你需要成功通过5个小关卡！\n")
    #print("以获得更高的分数与其他玩家一较高下吧！\n")
    
#Menu END

#MAIN program START

i = 2
game_over = False


GAMES = games(0) #创建一个GAMES instance，然后套用games class里的功能。

while i > 0 and game_over == False:
    DICE = Rnumber()

    if DICE < 5:
        updated_score = GAMES.simplemath()
    else:
        updated_score = GAMES.simplemath2()

    
    

    loading(1) #等待一秒, loading()内建等待1秒
    i -= 1


print("恭喜！您已获得进入名人堂的资格，是否将自己的分数与其他人一较高下？")
option = input("'Yes' or 'No' ? Y/N: ")
if option == 'N' or option == 'n':
    print(f"您的最终分数是: {GAMES.score}")
    print("您的分数已被初始化，感谢游玩！")
    GAMES.score = 0
elif option == 'Y' or option == 'y':
    HallOfFame().save_data(1,GAMES.score)
    print("您的分数已成功存入名人堂！")  
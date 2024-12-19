import time
import csv 
import random
import os

#Function definition zone START

def clear(): #用来清除命令行上的讯息
    os.system('cls')

def loading(waitTIME): 
    progress = [Rnumber(0,24),Rnumber(25,49),Rnumber(50,74), Rnumber(75,98), '99', '100']
    cd = float(waitTIME / 6)
    for i in range(0,6):
        print(f"loading {progress[i]}%")
        time.sleep(cd)

def Rnumber(min,max):   # min为随机范围最小数，max为随机范围最大数
    currentTIME = float(time.time()) #fetching current time, use float资料形态是为了让数值变化大一点。
    random.seed(currentTIME) #using current time as random number generator seed.
    randomNUM = random.randint(min,max) #random number are int(min~max)
    return randomNUM #return value

class games():
    def __init__(self,score): #initialize user data.
        self.score = score
    
    def simplemath(self):
        def GAMEprogress(player_input, ans, score):
            if player_input == ans:
                self.score += score
                print(f"答案正确！奖励 {score} 分！\n")
                print(f'你目前的總分数为 {self.score}。\n')
            else:
                print(f"答案错误！正确答案是 {ans}!\n")
                print(f'你目前的總分数为 {self.score}。\n')

        DICE = Rnumber(0,9)  # 0~9
        operators = ['+', '-', '*', '/']
        operands1 = [Rnumber(0,9), Rnumber(10,99), Rnumber(100,999)]
        time.sleep(0.25)  # 等待0.25秒，不然会出现operand1和operand2相同数值的情况（因为是在同时获得的以时间为随机种子的值）
        operands2 = [Rnumber(0,9), Rnumber(10,99), Rnumber(100,999)]
        num10 = Rnumber(0,9)
        
        if DICE <= 4:  # 0-4 为加法
            index = 0 if num10 < 50 else 1 if num10 < 90 else 2 # index 0为个位数，1为十位数，2为百位数加法
            ans_string = f'{operands1[index]} {operators[0]} {operands2[index]}'
            ans = operands1[index] + operands2[index]
            score = 20
        elif 5 <= DICE <= 8:  # 5-8 为减法 
            index = 0 if num10 < 50 else 1 if num10 < 90 else 2 # index 0为个位数，1为十位数，2为百位数减法
            ans_string = f'{operands1[index]} {operators[1]} {operands2[index]}'
            ans = operands1[index] - operands2[index]
            score = 20
        elif DICE == 8: # 8 为乘法
            ans_string = f'{operands1[0]} {operators[2]} {operands2[0]}'
            ans = operands1[0] * operands2[0]
            score = 20
        else: #9 为整数除法
            ans_string = f'{operands1[0]} {operators[3]} {operands2[0]}'
            ans = operands1[0] // operands2[0]
            score = 20

        dialog = f'请输入答案 {ans_string} 等于多少'
        if DICE == 9:  # 只有在除法情况下提示整数除法
            dialog += ' (整数除法): '
        else:
            dialog += ': '

        while True:
            try:
                player_input = int(input(dialog))
                break  # 输入正确则退出循环
            except ValueError:
                print("输入无效，请输入一个整数！\n")

            GAMEprogress(player_input, ans, score)
            return self.score

    def NMS_NUMseq(self):

        print("歡迎來到數列解密遊戲！")
        print("數組之間是有規律，請猜出-????-裏是什麼。")
        print("注意：1題只有 1 次機會！")

        def shiftL(numseq):
            temp = numseq[0] #将第一个元素用temp变数存储起来。
            for i in range(1, len(numseq)):
                numseq[i - 1] = numseq[i] #将数列的元素向左位移
            numseq[-1] = temp #将temp赋予最后一位元素。
            return numseq
        def shiftR(numseq):
            temp = numseq[-1]
            for i in range(len(numseq) - 2, -1, -1): #range(start,end,step)
                numseq[i + 1] = numseq[i] #将数列的元素向左位移
            numseq[0] = temp #将temp赋予最后一位元素。
            return numseq
        def ListToString(numseq):
                result_str = ''
                for num in numseq:
                    result_str += str(num)
                return result_str
        def progress(playerANS,ANS,score):
            if playerANS == ANS:
                print("对了！")
                self.score += score
                print(f"你获得了{score}\n")
                print(f"目前总分为{self.score}\n")
            else:
                print("错了！")
                print(f"正确答案是{ANS[0]}{ANS[1]}{ANS[2]}{ANS[3]}\n")
        NUMseq = [time.sleep(0.25) or Rnumber(0,9) for i in range(4)] #建立数字序列，create NUMsequence
        DICE = Rnumber(0,2)
        NUMseq_copy = NUMseq.copy() #为答案的结果独立计算所建立，避免相同地址冲突的情况发生
        WHEN_TO_ANSWER = Rnumber(0,3) #在哪个环节进行答题
        if DICE: #0为shift to left，向左位移
            for _ in range(WHEN_TO_ANSWER+1): #确保迭代至所要求的答案输入次序。
                ans = shiftL(NUMseq_copy)
            for i in range(4):
                if i == WHEN_TO_ANSWER:  
                    shiftL(NUMseq)
                    print("-????-", end =' ')
                    continue
                ans_string_output = shiftL(NUMseq)
                print(f"-{ans_string_output[0]}{ans_string_output[1]}{ans_string_output[2]}{ans_string_output[3]}-", end =' ')
            
        else:
            for _ in range(WHEN_TO_ANSWER+1): #确保迭代至所要求的答案输入次序。
                ans = shiftR(NUMseq_copy)
            for i in range(4):
                if i == WHEN_TO_ANSWER:  
                    shiftR(NUMseq)
                    print("-????-", end =' ')
                    continue
                ans_string_output = shiftR(NUMseq)
                print(f"-{ans_string_output[0]}{ans_string_output[1]}{ans_string_output[2]}{ans_string_output[3]}-", end =' ')

        ans_string_input = ListToString(ans)

        while True:
            try:
                player_input = str(input("\n请输入答案！\n"))  # 输入答案
                if len(player_input) != 4 or not player_input.isdigit():  # 检查是否为有效的 4 位数字
                    raise ValueError("输入必须是 4 位数字！\n")
                break
            except ValueError as e:
                print(f"输入错误：{e} 请重新输入！\n")

        progress(player_input,ans_string_input,20)

    def democratic_spirit(self):



    
    def guess_the_number(self):

        print("歡迎來到猜數字遊戲！")
        print("我會隨機選一個1到100的數字，你需要猜出它是什麼。")
        print("如果猜錯了，我會告訴你答案是更大還是更小。")
        print("注意：你最多只能猜 10 次！")

        number_to_guess = Rnumber(2,99) # 隨機生成1到100之間的數字,不包括1和100
        attempts = 0  # 記錄嘗試次數
        max_attempts = 10  # 最大猜測次數

        print("請輸入1到100之間的數字。")
        x = 100  # 初始化范围的上限
        y = 1    # 初始化范围的下限

        while attempts < max_attempts:
            try:
                # 玩家輸入猜測數字
                guess = int(input(f"您的猜測："))

                # 检查输入是否在动态范围内
                if guess < y or guess > x:
                    print(f"超出範圍了！請輸入 {y} 到 {x} 之間的數字。\n")
                    continue  # 跳回循环让玩家重新输入

                attempts += 1

                if guess < number_to_guess:
                    print("太小了！再試一次。\n")
                    print(f"請輸入 {guess} 到 {x} 之間的數字。")
                    y = guess  # 更新范围的下限
                elif guess > number_to_guess:
                    print("太大了！再試一次。\n")
                    print(f"請輸入 {y} 到 {guess} 之間的數字。")
                    x = guess  # 更新范围的上限
                else:
                    print(f"恭喜你猜中了！答案是 {number_to_guess} 。\n")
                    print(f"你總共猜了 {attempts} 次。")

                    # 加分逻辑：根据尝试次数奖励分数
                    if attempts <= 5:
                        self.score += 20  # 极快猜中，奖励 20 分
                        print("太厉害了！奖励 20 分！\n")
                    elif attempts <= 8:
                        self.score += 10  # 正常表现，奖励 10 分
                        print("很不错！奖励 10 分！\n")
                    else:
                        self.score += 5  # 尽管尝试多次，但最终成功，奖励 5 分
                        print("坚持就是胜利！奖励 5 分！\n")
                    
                    print(f"你目前的總分数为 {self.score}。\n")
                    break

                # 检查猜测次数是否已用尽
                if attempts == max_attempts:
                    print("很遗憾，你已经用尽了所有猜测机会！")
                    print(f"正確答案是 {number_to_guess} 。\n")
                    print(f"你目前的總分数为 {self.score}。\n")
                    
            except ValueError:  # 异常处理：捕获非数字输入的错误并提示玩家重新输入正确的数字。
                print(f"錯誤：請輸入 {y} 到 {x} 之間的有效數字！\n")



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
        print(f"\n[HOF]玩家{playerNAME}获得的总分是{score}恭喜成为我们第{self.seq}入榜的玩家！")
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

i = 5
game_over = False


GAMES = games(0) #创建一个GAMES instance，然后套用games class里的功能。

while i > 0 and game_over == False:
    DICE = Rnumber(0,9) # random number:0~9

    # if DICE:
    #     updated_score = GAMES.simplemath()
    # else:
    #     updated_score = GAMES.guess_the_number()
    #updated_score = GAMES.NMS_NUMseq()
    updated_score = GAMES.guess_the_number()#delete

    loading(1) #等待一秒, loading()内建等待1秒
    print("")
    i -= 1

print(f"你在本次游玩中获得了 {GAMES.score} 分")
print("恭喜！您已获得进入名人堂的资格，是否将自己的分数与其他人一较高下？")

while True:
    try:
        option = input("'Yes' or 'No' ? Y/N: ").strip()  # 去除多余空格
        if option in ['N', 'n']:
            print(f"您的最终分数是: {GAMES.score}")
            print("您的分数已被初始化，感谢游玩！")
            GAMES.score = 0
            break
        elif option in ['Y', 'y']:
            HallOfFame().save_data(1, GAMES.score)  # 保存分数到名人堂
            print("您的分数已成功存入名人堂！")
            break
        else:
            # 如果用户输入无效值，提示重新输入
            print("输入无效，请输入 'Y' 或 'N'！")
    except Exception as e:
        # 捕获其他可能的异常，避免程序崩溃
        print(f"发生错误：{e}")
        print("请重新输入 'Y' 或 'N'！")

#MAIN program END
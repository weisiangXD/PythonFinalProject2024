import time
import csv
import random 
import os

#Function definition zone START

def clear():
    #清道夫

def Runumber(min,max):
    #用当前时间为种子生成一个范围min ~ max的随机数

def loading(waitTIME):
    #加载动画

class games():
    def __init__(self):
        self.score = 0
    
    def simplemath(self): #简单数学题 by 偉翔
        clear()
        def GAMEprogress(player_input, ans, score):

    def NMS_NUMseq(self): #数字序列游戏, insipired by "NO MAN SKY的数字解谜游戏" by 偉翔
        clear()
        def GAMEprogress(playerANS, ANS, score):
        def shiftL(numseq):
        def shiftR(numseq):    
        def ListToString(numseq):

    #def democratic_spirit(self): #废案 insipired by "helldivers 2"

    def guess_the_number(self): #猜数字游戏 by KY
        clear()

    def v_code(self):
        def show_numbers():
        def countdown():

    def NotNot(self): #喜欢唱反调游戏 by 美国人

    def EnglishTypingGame(self): #英文打字游戏 by 美国人

class HallOfFame(): #名人堂 by 偉翔
    def __init__(self):
        self.data = []
        self.seq = 1
    
    def add(self, filename, uname, score):

    def sort(self):

    def save(self, filename):
        filepath = self.get_file_path(filename)

    def load(self, filename):
        filepath = self.get_file_path(filename)

    def display(self, filename):
        self.load(filename)
        self.sort()

    def save_data(self, filename, mode, score):
        self.load(filename)

    def get_file_path(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__)) #获取当前文件的绝对路径，绝对路径 = 从系统的根目录开始的路径
        return os.path.join(base_dir, 'leaderboard', filename) #返回文件路径

    def leaderboard_console(self):

#Function definition zone END

#Menu START
clear() #清一清
solo = False #当solo = False时为混合游戏模式
while 1: #进入主菜单
    option = input()
    match option:
        case 1:
            break
        case 2:
            break
        case 10086: #ADMIN mode
            break
#Menu END

#MAIN program start

clear() #清一清
i = 1 #游戏关卡数
GAMES = games(0) #建立游戏实例(create a person)，套用class games(ppl里的眼睛、耳朵、嘴巴)。

while i > 0:
    if solo:
        #solo玩单个游戏模式
    else:
        #混合游戏模式
    i -= 1

#分数结算 START
print("%告诉玩家他/她获得了进入名人堂的资格，询问是否要与他人一较高下！%")
if GAMES.score > 0:
    #进行分数的结算

    while 1: #一直干活，直到我喊卡
        #输入姓名
        #存储分数
        #显示排行榜

#分数结算 END

#MAIN program end





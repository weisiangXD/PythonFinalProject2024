import time
import csv 
import random


#Function definition zone START

def Rnumber():   
    currentTIME = float(time.time())
    random.seed(currentTIME)

    randomNUM = random.randint(0,9)

    return randomNUM

class games():
    def __init__(self,uname,score): #initialize user data.
        self.name = uname 
        self.score = score
    
    #def game1():

    #def game2():

class HallOfFame():
    def __init__(self):
        self.scores = []

    def add_score(self, user_id, score):
        self.scores.append({'user_id': user_id, 'score': score})

    def sort_scores(self):
        self.scores = sorted(self.scores, key=lambda x: x['score'], reverse=True)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['user_id', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for score in self.scores:
                writer.writerow(score)

    def load_from_csv(self, filename):
        self.scores = []
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.scores.append({'user_id': row['user_id'], 'score': int(row['score'])})

    def display(self):
        for entry in self.scores:
            print(f"User ID: {entry['user_id']}, Score: {entry['score']}")

    def save_score(self, uname, score):
        print("恭喜！您已获得进入名人堂的资格，是否将自己的分数与其他人一较高下？")
        option = input("'Yes' or 'No' ? Y/N: ")
        if option.upper() == 'N':
            print("您的分数将被初始化，感谢游玩！")
            score = 0
        elif option.upper() == 'Y':
            self.add_score(uname, score)
            self.sort_scores()
            self.save_to_csv('leaderboard.csv')
            print("您的分数已成功存入名人堂！")

#Function definition zone END


#MAIN program start

i = 5
game_over = False

while i >= 0 and game_over == False:
    decideNUM = Rnumber()
    print(f"随机数是{decideNUM}")
    match decideNUM:
        case "1":
            print("1")
            print(decideNUM)
        case "2":
            print("2")
        case "3":
            print("3")

    time.sleep(1) #等待一秒
    i -= 1

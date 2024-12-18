import time
import random

def Rnumber(multiplier=1):
    return random.randint(0, 9) * multiplier

class Games:
    def __init__(self, score):
        self.score = score
    
    def simplemath(self):
        def progress(player_input, ans, mark):
            if player_input == ans:
                self.score += mark
                print("答案正确！")
                print(f'你目前的分数为 {self.score}')
            else:
                print(f"答案错误！正确答案是 {ans}!")
                print(f'你目前的分数为 {self.score}')

        DICE = Rnumber()  # 0~9
        operators = ['+', '-', '*', '/']
        operands1 = [Rnumber(1), Rnumber(10), Rnumber(100)]
        time.sleep(0.25)  # 等待0.25秒，不然会出现operand1和operand2相同数值的情况（因为是在同时获得的以时间为随机种子的值）
        operands2 = [Rnumber(1), Rnumber(10), Rnumber(100)]
        num10 = Rnumber(10)
        
        if DICE < 4:  # 0-3
            index = 0 if num10 < 50 else 1 if num10 < 90 else 2
            ans_string = f'{operands1[index]} {operators[0]} {operands2[index]}'
            ans = operands1[index] + operands2[index]
            mark = 2 if index == 0 else 5 if index == 1 else 10
        elif 5 < DICE < 8:  # 6-7
            index = 0 if num10 < 50 else 1 if num10 < 90 else 2
            ans_string = f'{operands1[index]} {operators[1]} {operands2[index]}'
            ans = operands1[index] - operands2[index]
            mark = 2 if index == 0 else 5 if index == 1 else 10
        elif DICE == 8:
            ans_string = f'{operands1[0]} {operators[2]} {operands2[0]}'
            ans = operands1[0] * operands2[0]
            mark = 10
        else:
            ans_string = f'{operands1[0]} {operators[3]} {operands2[0]}'
            ans = operands1[0] // operands2[0]
            mark = 10

        prompt = f'请输入答案 {ans_string} 等于多少'
        if DICE == 9:  # 只有在除法情况下提示整数除法
            prompt += ' (整数除法): '
        else:
            prompt += ': '

        player_input = int(input(prompt))
        progress(player_input, ans, mark)
        return self.score

# 示例调用
game = Games(0)
game.simplemath()

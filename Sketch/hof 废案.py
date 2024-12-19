import random
import time

def Rnumber(min, max):   # min为随机范围最小数，max为随机范围最大数
    return random.randint(min, max)  # 直接使用random生成随机数

class Games:
    def __init__(self, score):  # 初始化用户数据
        self.score = score

    def NMS_NUMseq(self):
        def shiftL(numseq):
            temp = numseq[0]  # 将第一个元素用temp变量存储起来
            for i in range(1, len(numseq)):
                numseq[i - 1] = numseq[i]  # 将数列的元素向左位移
            numseq[-1] = temp  # 将temp赋予最后一位元素
            return numseq

        def ListToString(numseq):
            result_str = ''
            for num in numseq:
                result_str += str(num)
            return result_str

        def progress(playerANS, ANS, score):
            if playerANS == ANS:
                print("对了！")
                self.score += score
                print(f"你获得了{score}")
                print(f"目前总分为{self.score}")
            else:
                print("错了！")
                print(f"正确答案是{ANS}")

        NUMseq = [time.sleep(0.25) or Rnumber(0, 9) for _ in range(4)]  # 建立数字序列
        original_SEQ = NUMseq.copy()  # 保持原始序列不变

        DICE = Rnumber(0, 2)
        WHEN_TO_ANSWER = Rnumber(0, 3)  # 在哪个环节进行答题
        
        for i in range(4):
            if i == WHEN_TO_ANSWER:
                ans = shiftL(original_SEQ.copy())
                print("-????-", end=' ')
                continue
            ans_string_output = shiftL(original_SEQ.copy())
            print(f"-{ListToString(ans_string_output)}-", end=' ')
        
        print("")  # 换行，以便之后的输入提示
        player_input = input("请输入答案！")
        ans_string_input = ListToString(shiftL(original_SEQ.copy()))  # 使用原始序列的移位结果进行答案检查

        progress(player_input, ans_string_input, 10)

GAMES = Games(0)

while True:
    GAMES.NMS_NUMseq()

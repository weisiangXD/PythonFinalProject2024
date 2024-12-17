print("恭喜！您已获得进入名人堂的资格，是否将自己的分数与其他人一较高下？")
        option = input("'Yes' or 'No' ? Y/N: ")
        if option == 'N' or 'n':
            print("您的分数将被初始化，感谢游玩！")
            score = 0
        elif option == 'Y' or 'y':
            self.add(playerNAME, playerSCORE)
            self.sort()
            self.save("leaderboard.csv")
            print("您的分数已成功存入名人堂！")  
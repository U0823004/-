
import random
print("1A2B遊戲")
print("游戲規則：系統隨機給出0-9的4個不重複的數字，您可以輸入您猜測的4個數字，系統會比較並給予提示，A表示數字對且位置對，B表示數字對位置不對，如1A2B表示有1位您猜對了數字和位置，有2位您猜對數字，但位置不對。")
answer=random.sample('1234567890',4)
print("請選擇模式，輸入I不限挑戰次數，輸入F有限挑戰次數。")
mode = input('(I/F)')
    
if mode == 'I':
    guessTimes = 0
    while (guessTimes < 99999):
        guessTimes=guessTimes+1
        for inputErros in range(3):
            guess=input("請輸入4個0-9不重復的數字：") 
            if guess.isdigit()==True and len(guess)==4:
                guessSet=set(guess)
                if len(guessSet)==4 and guessSet.isdisjoint(set('')):
                    break
        else:
            print("請仔細讀游戲規則，再來遊玩，答案是%s，游戲結束。"%(answer))
            exit()

        A=0
        B=0
        for j in range(4):
            if guess[j]==answer[j]:
                A+=1
            else:
                for k in range(4):
                    if guess[j]==answer[k]:
                        B+=1
        if A<4:
            guessTimes += 1
            print("%dA%dB，目前猜了%d次。"%(A,B,guessTimes*0.5))
        else:
            print("恭喜您答對了！答案是%s"%(answer))
            print("總共猜了%d次"%(guessTimes*0.5))
            exit()

elif mode == 'F':
    guessTimesrange=int(input('請輸入最多要在幾次內完成挑戰，未達成則挑戰失敗:'))

    for guessTimes in range(guessTimesrange):
        guess=""
        for inputErros in range(3):
            guess=input("請輸入4個0-9不重復的數字：") 
            if guess.isdigit()==True and len(guess)==4:
                guessSet=set(guess)
                if len(guessSet)==4 and guessSet.isdisjoint(set('')):
                    break
        else:
            print("請仔細讀游戲規則，再來遊玩，答案是%s，游戲結束。"%(answer))
            exit()

        A=0
        B=0
        for j in range(4):
            if guess[j]==answer[j]:
                A+=1
            else:
                for k in range(4):
                    if guess[j]==answer[k]:
                        B+=1
        if A<4:
            if guessTimes<int(guessTimesrange-1):
                print("%dA%dB，您還有%d次機會。" %(A,B,guessTimesrange-guessTimes-1))
            else:
                print("很遺憾，挑戰失敗，答案是%s。" %(answer))
        else:
            print("恭喜您挑戰成功！答案是%s"%(answer))
            print("總共猜了%d次"%(guessTimes+1))
            exit()
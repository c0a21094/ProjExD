import random
import datetime
if __name__ == "__main__":
    num = random.randint(0, 2)    
    st = datetime.datetime.now() 
    def shutudai(n):
        q1 = "サザエの旦那の名前は？"
        q2 = "カツオの妹の名前は？"
        q3 = "タラオはカツオから見てどんな関係？"
        q_list = [q1, q2, q3]
        return q_list[n]

    def kaito(n):
        a1 = ["マスオ", "ますお"]
        a2 = ["ワカメ", "わかめ"]
        a3 = ["甥", "おい", "甥っ子", "おいっこ"]
        a_list = [a1, a2, a3]
        ans = input("答えるんだ：")
        if ans in a_list[n]:
            result = "正解！！！"
        else:
            result = "出直してこい"

        return result
    
    print("問題：")
    print(shutudai(n))
    print(kaito(n))
    ed = datetime.datetime.now()

    print(f"{(ed-st).seconds}秒")
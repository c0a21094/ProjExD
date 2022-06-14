import random
import datetime

t_num = 10 #対象文字数
m_num = 2 #欠損文字数
max = 5 #最大繰り返し回数
def shutudai():
    global t_num, m_num
    t = []
    k = []
    ans = []
    for i in range(t_num):
        a = random.randint(65, 90)
        t.append(chr(a))
        k = t.copy()
    for i in range(m_num):
        b = random.randint(0, 8)
        k.pop(b)
        ans.append(t[b])
    print(f"対象文字：{t}")
    print(f"欠損文字：{ans}")
    print(f"表示文字：{k}")

    return ans

def kaitou_kazu():
    global m_num
    ans = input("欠損文字はいくつしょうか？")
    if int(ans) == int(m_num):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        return 1
    else:
        print("不正解です。またチャレンジしてください")
        return 0

def kaitou(seikai):
    c = 1
    while c <= m_num:
        ans = input(f"{c}つ目の文字を入力してください：")
        if ans in seikai:
            print("正解です")
        else:
            print("不正解です。またチャレンジしてください")
            return 0
        c += 1
    return 1
def main():
    st = datetime.datetime.now() 
    for i in range(max):
        seikai = shutudai()
        f1 = kaitou_kazu()
        if f1 == 0:
            break
        f2 = kaitou(seikai)
        if f2 == 1:
            ed = datetime.datetime.now()
            time = (ed-st).seconds
            return f"解答時間は{time}秒でした"
        
if __name__ == "__main__":
    main()
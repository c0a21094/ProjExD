
import random
import tkinter as tk
import maze_maker
import tkinter.messagebox as tkm

#グローバル変数
key = ""        #押されたキーを代入する関数
cx, cy =150, 150     #こうかとんの現在地を表す変数
mx, my = 1, 1       # マスの位置
png_num = 1     # こうかとんの画像番号
tmr = 0         # タイマー
#こうかとんを表示する関数
def draw():
    global tori, cx, cy, tori_id, png_num
    png = f"fig/{png_num}.png"
    tori = tk.PhotoImage(file = png)
    tori_id = canvas.create_image(cx, cy,
    image = tori, tag = "tori")

#keyに押されたキーを代入する関数
def key_down(event):
    global key, png_num
    key = event.keysym
    if key == "s":
        png_num = random.randint(0, 9)
        draw()
    else:
        draw()
#keyの値を初期化する関数
def key_up(event):
    global key
    key = event.keysym
    key = ""


#押したキーによってこうかとんを移動させる関数
def main_proc():                                                         
    global cx, cy, key, mx, my                                  
    if key == 'Up' and maze_list[my-1][mx] == 0 or maze_list[my-1][mx] == 2:                        
        my += -1   

    elif key == 'Down' and maze_list[my+1][mx] == 0 or maze_list[my+1][mx] == 2:                 
        my += 1                                                     

    elif key == 'Right' and maze_list[my][mx+1] == 0 or maze_list[my][mx+1] == 2 :                 
        mx += 1                                                

    elif key == 'Left' and maze_list[my][mx-1] == 0 or maze_list[my][mx-1] == 2:                   
        mx -= 1     
    elif maze_list[my][mx] == 2:
        tkm.showinfo("警告！！", "落とし穴に落ちましたwww")
    else:
        pass
    cx = (mx*100)+50
    cy = (my*100)+50
    maze.after(100, main_proc)
    canvas.coords("tori", cx, cy)
    draw()

# 経過時間の表示
def count_up():
    global tmr
    tmr = tmr+1
    label["text"] = f"{tmr}秒"
    if mx == 13 and my == 7:
        tkm.showinfo("おめでとう",f"{tmr}秒でクリアしました")
    else:
        maze.after(1000, count_up)

# スタートラベルの作成
def draw_start():
    start = tk.Label(maze, 
                    text="S", 
                    font=("Times New Roman", 60), 
                    bg="yellow", 
                    height=1, 
                    width=2)
    start.pack()
    start.place(x=100, y=0)

# ゴールラベルの作成 
def draw_goal():
    goal = tk.Label(maze, 
                    text="G", 
                    font=("Times New Roman", 60), 
                    bg="red", 
                    height=1, 
                    width=2)
    goal.pack()
    goal.place(x=1300, y=800)

# 落とし穴の作成
def otosiana():
    global maze_list
    c = 0
    while c < 1:
        b = random.randint(1, 13)
        a = random.randint(1, 7)
        if maze_list[a][b] == 0:
            maze_list[a][b] = 2
            c += 1
        else:
            continue
if __name__ == "__main__":

    #ウィンドウ作成
    maze = tk.Tk()
    maze.geometry("1500x1000")
    maze.title("迷えるこうかとん")
    canvas = tk.Canvas(maze, width = 1500,
    height = 900,bg = 'black')   
    canvas.place(x=0, y=0)

    # 迷路の作成
    maze_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze_list)

    
    otosiana()
    maze.bind("<KeyPress>", key_down)                       
    maze.bind("<KeyRelease>", key_up)  
    maze.after(100, main_proc)
    label = tk.Label(maze, font=("Times New Roman", 60))
    label.pack()
    label.place(x=0, y=900)
    draw_start()
    draw_goal()
    draw()
    maze.after(1000, count_up)
    maze.mainloop()
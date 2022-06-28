import tkinter as tk
import maze_maker

#グローバル変数
key = ""        #押されたキーを代入する関数
cx, cy =150, 150     #こうかとんの現在地を表す変数
mx, my = 1, 1

#こうかとんを表示する関数
def draw():
    global tori, cx, cy, tori_id
    png_num = 1
    png = f"fig/{png_num}.png"
    tori = tk.PhotoImage(file = png)
    tori_id = canvas.create_image(cx, cy,
    image = tori, tag = "tori")

#keyに押されたキーを代入する関数
def key_down(event):
    global key
    key = event.keysym

#keyの値を初期化する関数
def key_up(event):
    global key
    key = event.keysym
    key = ""

#押したキーによってこうかとんを移動させる関数
def main_proc():                                                         
    global cx, cy, key, mx, my                                  
    if key == 'Up' and maze_list[my-1][mx] == 0:                        
        my += -1   

    elif key == 'Down' and maze_list[my+1][mx] == 0:                 
        my += 1                                                     

    elif key == 'Right' and maze_list[my][mx+1] == 0:                 
        mx += 1                                                

    elif key == 'Left' and maze_list[my][mx-1] == 0:                   
        mx -= 1     
    cx = (mx*100)+50
    cy = (my*100)+50
    maze.after(100, main_proc)
    canvas.coords("tori", cx, cy)

if __name__ == "__main__":

    #ウィンドウ作成
    maze = tk.Tk()
    maze.geometry("1500x900")
    maze.title("迷えるこうかとん")

    canvas = tk.Canvas(maze, width = 1500,
    height = 900,bg = 'black')   
    canvas.place(x=0, y=0)

    maze.bind("<KeyPress>", key_down)                       
    maze.bind("<KeyRelease>", key_up)  
    maze.after(100, main_proc)
    maze_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze_list)
    draw()
    maze.mainloop()
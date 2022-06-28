import tkinter as tk



if __name__== "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry()
 
    cx = 300 # こうかとんのx座標
    cy = 400 # こうかとんのy座標
    tori = tk.PhotoImage(file="fig/0.png", width=cx, height=cy)
    canvas = tk.Canvas(root, bg="#000000", height=900, width=1500)
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.pack()

    root.mainloop()

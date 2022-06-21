import tkinter as tk
import tkinter.messagebox as tkm
import random as rd

def button_click(event):
    button = event.widget
    num = button["text"]
    #tkm.showinfo("",f"{num}のボタンが押されました")
    entry.insert(tk.END, num)
    rdcolor = [
        "#000000", "#FF0000", "#FFA500", "#FFFF00", "#008000", "#00FFFF", "#0000FF", "#800080"
    ]
    i = rd.randint(0, 7)
    button["bg"] = rdcolor[i]

def eqall_click(event):
    a = entry.get()
    result = eval(a)
    entry.delete(0,tk.END)
    entry.insert(tk.END, result)


def allclear_click(event):
    entry.delete(0, tk.END)


def clear_click(event):
    a = len(entry.get())-1
    entry.delete(a, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x700")
    root.title("電卓")

    entry = tk.Entry(root,justify="right", width=14, font=("Times New Roman", 40))
    entry.grid(row=0, column=0, columnspan=4)

    r,c=1,0
    for i, num in enumerate(["CE", "C", "=","+", 9, 8, 7, "/",6, 5, 4,"*",  3, 2, 1,"-", 0]):
        button =tk.Button(root,text=num,width=4, height=2,font=("Times New Roman",30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c+=1
        if num == "=":
            button.bind("<1>", eqall_click)
        if num == "CE":
            button.bind("<1>", allclear_click)
        if num == "C":
            button.bind("<1>", clear_click)
        if (i+1)%4==0:
            r+=1
            c=0
        
    root.mainloop()
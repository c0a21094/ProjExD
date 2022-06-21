import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    button = event.widget
    num = button["text"]
    #tkm.showinfo("",f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

def eqall_click(event):
    a = entry.get()
    result = eval(a)
    entry.delete(0,tk.END)
    entry.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x600")
    root.title("電卓")

    entry = tk.Entry(root,justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column=0, columnspan=3)

    r,c=1,0
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]+["+", "="]):
        button =tk.Button(root,text=num,width=4, height=2,font=("Times New Roman",30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c+=1
        if num == "=":
            button.bind("<1>", eqall_click)
        if (i+1)%3==0:
            r+=1
            c=0
        
    root.mainloop()
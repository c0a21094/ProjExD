import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x500")
root.geometry("300x500")
font1=("Times New Roman", 30)
for i in range(9, -1, -1):
    button = tk.Button(root, text=i, font=font1)
    button.grid(row=0, column=0)
    button.pack()
root.mainloop()
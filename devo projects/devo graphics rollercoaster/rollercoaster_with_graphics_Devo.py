import tkinter as tk
from PIL import Image, ImageTk
from os import system
system("cls")
win1 = tk.Tk()
pic = Image.open(r"C:\Users\bhuvnesh\Desktop\practice\devo graphics rollercoaster\img.jpg")
tkpic = ImageTk.PhotoImage(pic)
win1.title("Rollercoaster ticket booking")
win1.geometry("1500x1500")
tkage = tk.StringVar()
tkheight = tk.StringVar()
img = tk.Label(win1, image=tkpic).grid(row=0, column=0, columnspan= 5)
t1 = tk.Label(win1, text="Your Age:  ", font= ("Times New Roman", 16, "bold")).grid(row = 1, column = 0, sticky="w")
i1 = tk.Entry(win1, textvariable=tkage).grid(row=1, column=0, sticky="e")

t2 = tk.Label(win1, text="Your Height:   ", font= ("Times New Roman", 16, "bold")).grid(row = 2, column = 0, sticky="w")
i2 = tk.Entry(win1, textvariable=tkheight).grid(row=2, column=0, sticky="e")
age = 0
height = 0
def showdata():
    age, height = int(tkage.get()), int(tkheight.get())
    
btn = tk.Button(win1, text="Submit", command=showdata).grid(row=3, column = 0)
win1.mainloop()
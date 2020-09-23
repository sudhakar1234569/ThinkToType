import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    "python",
    "java",
    "swift",
    "mouse",
    "screen",
    "circuit",
    "network"
]
words = [
   "nptoyh",
   "ajav",
   "wfsit",
   "smeuo",
   "eesncr",
   "ctruiic",
   "tknwoer"
]

num = random.randrange(0, 7, 1)
def default():
    global words, answers, num
    lab.config(text="word: " + words[num])
def resetans():
    global words, answers, num
    num = random.randrange(0, 7, 1)
    lab.config(text="word: "+words[num])
    e.delete(0, END)


def checkans():
    global words, answers, num
    var = e.get()

    if var == answers[num]:
        messagebox.showinfo("Success", "Correct answer (^_^)..")
        resetans()

    else:
        messagebox.showerror("Error", "This is not Correct (-_-)..")
        e.delete(0, END)


window = tkinter.Tk()
window.geometry("350x500")
window.title("Think-To-Type")
window.configure(background="#000000")

lab1 = Label(
    window,
    text="Welcome To TTT",
    font=("verdana", 18),
    bg="#000000",
    fg="#ffffff"
)
lab1.pack(pady=20)

lab = Label(
    window,
    font=("verdana", 18),
    bg="#000000",
    fg="#ffffff"
)
lab.pack(pady=5, ipadx=10, ipady=10)

ans = StringVar()
e = Entry(
    window,
    font=("verdana", 13),
    textvariable=ans
)
e.pack(ipadx=6, ipady=6)

btnCheck = Button(
    window,
    text="Check",
    font=("comic sans ms", 16),
    width=15,
    bg="#2C3335",
    fg="#45CE30",
    relief=GROOVE,
    command=checkans
)
btnCheck.pack(pady=20)
btnReset = Button(
    window,
    text="Reset",
    font=("comic sans ms", 16),
    width=15,
    bg="#2C3335",
    fg="#FF3031",
    relief=GROOVE,
    command=resetans
)
btnReset.pack()
default()
window.mainloop()




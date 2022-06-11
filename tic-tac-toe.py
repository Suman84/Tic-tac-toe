from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-tac-toe')

clicked = True
count = 0
XorO = "X"
def disable_all_buttons():
    b1.config(state= DISABLED)
    b2.config(state= DISABLED)
    b3.config(state= DISABLED)
    b4.config(state= DISABLED)
    b5.config(state= DISABLED)
    b6.config(state= DISABLED)
    b7.config(state= DISABLED)
    b8.config(state= DISABLED)
    b9.config(state= DISABLED)


def checkIfWon(xoro):
    global winner
    winner = False

    if b1["text"] == xoro and b2["text"] == xoro and b3["text"] == xoro:
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()
    elif b4["text"] == xoro and b5["text"] == xoro and b6["text"] ==xoro:
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()
    elif b7["text"] == xoro and b8["text"] == xoro and b9["text"] ==xoro:
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()

    elif b1["text"] == xoro and b4["text"] ==xoro and b7["text"] ==xoro:
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()
    elif b2["text"] == xoro and b5["text"] == xoro and b8["text"] ==xoro:
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()
    elif b3["text"] == xoro and b6["text"] == xoro and b9["text"] ==xoro:
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()

    elif b1["text"] == xoro and b5["text"] == xoro and b9["text"] ==xoro:
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()
    elif b3["text"] == xoro and b5["text"] == xoro and b7["text"] ==xoro:
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", xoro + " won!")
        disable_all_buttons()
    else:
        pass
    if count == 9 and winner == False:
        messagebox.showinfo("tic tac toe", "TIE")


def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global count,clicked
    count = 0
    clicked = True
    b1 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b1))
    b2 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b2))
    b3 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b3))

    b4 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b4))
    b5 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b5))
    b6 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b6))

    b7 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b7))
    b8 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b8))
    b9 = Button(root, text='', font=("helvetica", 20), height=3, width=6, bg="systemButtonFace",command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def b_click(b):
    global clicked, count

    if b["text"] == '' and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkIfWon("X")
    elif b["text"] == '' and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkIfWon("O")
    else:
        messagebox.showerror("tic tac toe","click somewhere else")

reset()
#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label= "Options", menu = options_menu)
options_menu.add_command(label= "reset game", command= reset)

root.mainloop()



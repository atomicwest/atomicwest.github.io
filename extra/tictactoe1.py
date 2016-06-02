# install tkinter dependencies:
# sudo apt-get install python python-tk idle python-pmw python-imaging
# test tkinter; start python console $ python
# import Tkinter as tk
# tk._test()

# code from https://www.youtube.com/watch?v=RuYg_D_ppYk

from Tkinter import *
import Tkinter
# import tkMessageBox
import tkMessageBox as tkmsg

# tk = Tk()
tk = Tkinter.Tk()
tk.title("Tic Tac Toe Test")

click = True
def checker(buttons):
    global click

    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True

    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        # button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        # button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        tkmsg.showinfo("X has won", "O has lost")
        # tkMessageBox.showinfo("X has won", "O has lost")


    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        # button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
        # button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        tkmsg.showinfo("O has won", "X has lost")
        # tkMessageBox.showinfo("O has won", "X has lost")

    elif(button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
        button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
        button7["text"] != " " and button8["text"] != " " and button9["text"] != " " ):
        # tkMessageBox.showinfo("Cat's game", "Stalemate")
        tkmsg.showinfo("Cat's game", "Stalemate")



buttons=StringVar()

button1 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky = S+N+E+W)

button2 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky = S+N+E+W)

button3 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky = S+N+E+W)

button4 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky = S+N+E+W)

button5 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky = S+N+E+W)

button6 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky = S+N+E+W)

button7 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky = S+N+E+W)

button8 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky = S+N+E+W)

button9 = Button(tk, text = " ", font = ('Courier 28 bold'), height = 5, width = 9, command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky = S+N+E+W)

tk.mainloop()  #this brings up the game GUI

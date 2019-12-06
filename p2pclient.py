# TicTacToe client
#
#By: Brandon Griggs
import socket
import threading
import tkinter
import sys
                   # Import socket module
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


            # Create a socket object
s = socket.socket()
s2 = socket.socket()

#globals to keep track of important info
IDlist = []
usedBoxes = [0,0,0,0,0,0,0,0,0]
turn = 0
changes = 0
class ClientThread(threading.Thread):
    def __init__(self,serversocket):
        threading.Thread.__init__(self)
        self.ssocket = serversocket
    def run(self):
        global T
        global turn
        global usedBoxes
        global winStreak
        data = s.recv(1024)
        msg = data.decode()
        if msg[:-1] == "bat":
            T.config(state=NORMAL)
            T.insert('1.0',"Time to battle!\n")
            T.insert('1.0',"You go first\n")
            T.config(state=DISABLED)
            turn = 1
        if msg == "O1":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 1\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=1, column=1, pady=4)
            turn = 1
            usedBoxes[0] = 2
            if((usedBoxes[1]==2 and usedBoxes[2]==2) or (usedBoxes[3]==2 and usedBoxes[6]==2)or(usedBoxes[4]==2 and usedBoxes[8]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()
        if msg == "O2":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 2\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=1, column=2, pady=4)
            turn = 1
            usedBoxes[1] = 2
            if((usedBoxes[0]==2 and usedBoxes[2]==2) or (usedBoxes[4]==2 and usedBoxes[7]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()
        if msg == "O3":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 3\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=1, column=3, pady=4)
            turn = 1
            usedBoxes[2] = 2
            if((usedBoxes[0]==2 and usedBoxes[1]==2) or (usedBoxes[4]==2 and usedBoxes[6]==2)or(usedBoxes[5]==2 and usedBoxes[8]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()
        if msg == "O4":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 4\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=2, column=1, pady=4)
            turn = 1
            usedBoxes[3] = 2
            if((usedBoxes[4]==2 and usedBoxes[5]==2) or (usedBoxes[0]==2 and usedBoxes[6]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()
        if msg == "O5":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 5\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=2, column=2, pady=4)
            turn = 1
            usedBoxes[4] = 2
            if((usedBoxes[3]==2 and usedBoxes[5]==2) or (usedBoxes[1]==2 and usedBoxes[7]==2)or(usedBoxes[0]==2 and usedBoxes[8]==2)or(usedBoxes[2]==2 and usedBoxes[6]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()
        if msg == "O6":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 6\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=2, column=3, pady=4)
            turn = 1
            usedBoxes[5] = 2
            if((usedBoxes[8]==2 and usedBoxes[2]==2) or (usedBoxes[4]==2 and usedBoxes[3]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()

        if msg == "O7":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 7\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=3, column=1, pady=4)
            turn = 1
            usedBoxes[6] = 2
            if((usedBoxes[7]==2 and usedBoxes[8]==2) or (usedBoxes[4]==2 and usedBoxes[2]==2)or(usedBoxes[0]==2 and usedBoxes[3]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()
        if msg == "O8":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 8\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=3, column=2, pady=4)
            turn = 1
            usedBoxes[7] = 2
            if((usedBoxes[6]==2 and usedBoxes[8]==2) or (usedBoxes[4]==2 and usedBoxes[1]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()

        if msg == "O9":
            T.config(state=NORMAL)
            T.insert('1.0',"Opponent took square 9\n")
            T.insert('1.0',"It is your turn\n")
            T.config(state=DISABLED)
            tkinter.Button(master, image=igm2, command =(lambda: used_button()), height=85, width=85).grid(row=3, column=3, pady=4)
            turn = 1
            usedBoxes[8] = 2
            if((usedBoxes[5]==2 and usedBoxes[2]==2) or (usedBoxes[7]==2 and usedBoxes[6]==2)or(usedBoxes[4]==2 and usedBoxes[0]==2)):
                winStreak = 0
                T.config(state=NORMAL)
                T.insert('1.0',"Opponent Won\n")
                T.config(state=DISABLED)
                Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                x=0
                while x<len(usedBoxes):
                    if usedBoxes[x] == 0:
                        usedBoxes[x] = 3
                    x =x+1
            else:
                tie_check()

def tie_check():
    global T
    global usedBoxes
    if(usedBoxes[0]!=0 and usedBoxes[1]!=0 and usedBoxes[2]!=0 and usedBoxes[3]!=0 and usedBoxes[4]!=0 and usedBoxes[5]!=0 and usedBoxes[6]!=0 and usedBoxes[7]!=0 and usedBoxes[8]!=0):
        T.config(state=NORMAL)
        T.insert('1.0',"TIE game\n")
        T.config(state=DISABLED)

def click_algo(box):
    global s
    global turn
    global usedBoxes
    global changes
    if turn ==1:
        if usedBoxes[box-1]==0:
            usedBoxes[box-1] = 1
            s.send(bytes("T"+str(box),'utf-8'))
            turn = 0
            changes = 1
            newthread = ClientThread(s)
            newthread.start()

def connection_click(host, port):
    global s
    global T
    global winStreak
    sendStr = "hi"+ str(winStreak)
    print(sendStr)
    s.connect((host,int(port)))
    print('connected to server')
    s.send(bytes(sendStr,'utf-8'))
    T.config(state=NORMAL)
    T.insert('1.0',"Connected to server\n")
    T.insert('1.0',"Waiting...\n")
    T.config(state=DISABLED)
    data = s.recv(1024)
    msg = data.decode()
    if msg[:-1] == "bat":
        T.config(state=NORMAL)
        T.insert('1.0',"Time to battle!\n")
        T.insert('1.0',"Opponent's turn\n")
        T.config(state=DISABLED)
    if msg == "no":
        T.config(state=NORMAL)
        T.insert('1.0',"No available players yet...\n")
        T.config(state=DISABLED)
    newthread = ClientThread(s)
    newthread.start()




def disconnection_click():
    global s
    global turn
    global usedBoxes
    usedBoxes = [0,0,0,0,0,0,0,0,0]
    turn = 0
    s.send(bytes("quit",'utf-8'))
    s.close()
    print("disconnected from server")
    s = socket.socket()
    T.config(state=NORMAL)
    T.insert('1.0',"disconnected from server\n")
    T.config(state=DISABLED)
    b1 = tkinter.Button(master, image=igm3, command =(lambda: one_click()), height=85, width=85).grid(row=1, column=1, pady=4)
    b2 = tkinter.Button(master, image=igm3, command =(lambda: two_click()),height=85, width=85).grid(row=1, column=2, pady=4)
    b3 = tkinter.Button(master, image=igm3, command =(lambda: three_click()),height=85, width=85).grid(row=1, column=3, pady=4)
    b4 = tkinter.Button(master, image=igm3, command =(lambda: four_click()),height=85, width=85).grid(row=2, column=1, pady=4)
    b5 = tkinter.Button(master, image=igm3, command =(lambda: five_click()),height=85, width=85).grid(row=2, column=2, pady=4)
    b6 = tkinter.Button(master, image=igm3, command =(lambda: six_click()),height=85, width=85).grid(row=2, column=3, pady=4)
    b7 = tkinter.Button(master, image=igm3, command =(lambda: seven_click()),height=85, width=85).grid(row=3, column=1, pady=4)
    b8 = tkinter.Button(master, image=igm3, command =(lambda: eight_click()),height=85, width=85).grid(row=3, column=2, pady=4)
    b9 = tkinter.Button(master, image=igm3, command =(lambda: nine_click()),height=85, width=85).grid(row=3, column=3, pady=4)
def used_button():
    print("button used")
def one_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(1)
    if changes ==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=1, column=1, pady=4)
        if((usedBoxes[1]==1 and usedBoxes[2]==1) or (usedBoxes[3]==1 and usedBoxes[6]==1)or(usedBoxes[4]==1 and usedBoxes[8]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()



def two_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(2)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=1, column=2, pady=4)
        if((usedBoxes[0]==1 and usedBoxes[2]==1) or (usedBoxes[4]==1 and usedBoxes[7]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()
def three_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(3)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=1, column=3, pady=4)
        if((usedBoxes[0]==1 and usedBoxes[1]==1) or (usedBoxes[4]==1 and usedBoxes[6]==1)or(usedBoxes[5]==1 and usedBoxes[8]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()
def four_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(4)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=2, column=1, pady=4)
        if((usedBoxes[4]==1 and usedBoxes[5]==1) or (usedBoxes[0]==1 and usedBoxes[6]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()
def five_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(5)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=2, column=2, pady=4)
        if((usedBoxes[3]==1 and usedBoxes[5]==1) or (usedBoxes[1]==1 and usedBoxes[7]==1)or(usedBoxes[0]==1 and usedBoxes[8]==1)or(usedBoxes[2]==1 and usedBoxes[6]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()
def six_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(6)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=2, column=3, pady=4)
        if((usedBoxes[8]==1 and usedBoxes[2]==1) or (usedBoxes[4]==1 and usedBoxes[3]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()
def seven_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(7)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=3, column=1, pady=4)
        if((usedBoxes[7]==1 and usedBoxes[8]==1) or (usedBoxes[4]==1 and usedBoxes[2]==1)or(usedBoxes[0]==1 and usedBoxes[3]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()
def eight_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(8)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=3, column=2, pady=4)
        if((usedBoxes[6]==1 and usedBoxes[8]==1) or (usedBoxes[4]==1 and usedBoxes[1]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()
def nine_click():
    global changes
    global usedBoxes
    global winStreak
    click_algo(9)
    if changes==1:
        changes = 0
        tkinter.Button(master, image=igm1, command =(lambda: used_button()), height=85, width=85).grid(row=3, column=3, pady=4)
        if((usedBoxes[5]==1 and usedBoxes[2]==1) or (usedBoxes[7]==1 and usedBoxes[6]==1)or(usedBoxes[4]==1 and usedBoxes[0]==1)):
                    winStreak = winStreak + 1
                    T.config(state=NORMAL)
                    T.insert('1.0',"you Won, Win Streak: "+ str(winStreak)+"\n")
                    T.config(state=DISABLED)
                    Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)

                    x=0
                    while x<len(usedBoxes):
                        if usedBoxes[x] == 0:
                            usedBoxes[x] = 3
                        x =x+1
        else:
            tie_check()


master = Tk()
master.title("TicTacToe")
Label(master, text="server hostname").grid(row=0)
Label(master, text="port").grid(row=0, column=2)
v1 = StringVar(master, value='127.0.0.2')
v2 = StringVar(master, value='8080')
e1 = Entry(master,textvariable=v1)
e2 = Entry(master,textvariable=v2)
winStreak = 0
e1.grid(row=0, column=1)
e2.grid(row=0, column=3)

T = Text(master, height=10, width=70)
T.grid(row=4, columnspan=6)
T.config(state=DISABLED)

Lab1 = Label(master, text="Win Streak: "+str(winStreak), font='size, 20').grid(row=5)
igm1 = PhotoImage(file="./anX.png")
igm2 = PhotoImage(file="./anO.png")
igm3 = PhotoImage(file="./blank.png")

Button(master, text='Connect', command =(lambda: connection_click(e1.get(),e2.get()))).grid(row=0, column=5, sticky=W, pady=4)
Button(master, text='Disconnect', command =(lambda: disconnection_click())).grid(row=0, column=6, sticky=W, pady=4)
b1 = tkinter.Button(master, image=igm3, command =(lambda: one_click()), height=85, width=85).grid(row=1, column=1, pady=4)
b2 = tkinter.Button(master, image=igm3, command =(lambda: two_click()),height=85, width=85).grid(row=1, column=2, pady=4)
b3 = tkinter.Button(master, image=igm3, command =(lambda: three_click()),height=85, width=85).grid(row=1, column=3, pady=4)
b4 = tkinter.Button(master, image=igm3, command =(lambda: four_click()),height=85, width=85).grid(row=2, column=1, pady=4)
b5 = tkinter.Button(master, image=igm3, command =(lambda: five_click()),height=85, width=85).grid(row=2, column=2, pady=4)
b6 = tkinter.Button(master, image=igm3, command =(lambda: six_click()),height=85, width=85).grid(row=2, column=3, pady=4)
b7 = tkinter.Button(master, image=igm3, command =(lambda: seven_click()),height=85, width=85).grid(row=3, column=1, pady=4)
b8 = tkinter.Button(master, image=igm3, command =(lambda: eight_click()),height=85, width=85).grid(row=3, column=2, pady=4)
b9 = tkinter.Button(master, image=igm3, command =(lambda: nine_click()),height=85, width=85).grid(row=3, column=3, pady=4)

master.grid_rowconfigure(5, weight = 1)

mainloop()
print("GUI closed")


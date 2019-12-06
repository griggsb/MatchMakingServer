#match making server
#By: Brandon Griggs
import socket, threading
import time

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
    def run(self):
        global array
        global battle
        global clientId
        global openPlayer
        global openPlayer1
        global openPlayer2
        global activeTurns
        global oppMove
        global collision
        turn = 0
        confirmedCon = 0
        ID = clientId
        clientId = clientId + 1
        array.append(ID)
        msg = ''
        #use to pass over the recv statement
        passer = 0
        moveSent = 0
        while True:
            if moveSent ==0:
                time.sleep(.4)
                removeIndex = 0
                m=0
                while m < len(oppMove):
                    if ID == oppMove[m][0]:
                        mss = "O"+str(oppMove[m][1])
                        self.csocket.send(mss.encode('utf-8'))
                        removeIndex = m
                        moveSent = 1
                    m = m+1
                if(moveSent == 1):
                    hold = oppMove[removeIndex]
                    oppMove.remove(hold)
            if turn == 0:
                n = 0
                while n <len(activeTurns):
                    if activeTurns[n] == ID:
                        turn = 1
                        passer = 0
                    n = n+1
            msg = ''
            sendstring = ''
            if passer == 0:
                data = self.csocket.recv(1024)
                msg = data.decode()
            if confirmedCon == 0:
                i=0
                while i < len(battle):
                    x=0
                    while x<len(battle[i]):
                        if battle[i][x] == ID:
                            self.csocket.send("bat1".encode('utf-8'))
                            confirmedCon = 1
                            passer = 0
                        x = x+1
                    i = i+1
            if (len(msg)>0):
                if (msg=="quit"):
                    print("socket closed")
                    self.csocket.close()
                    array.remove(ID)
                    break
                elif(msg[:2]=="hi"):
                    if (msg[2]=="0"):
                        array.append(ID)
                        print("Added "+ str(ID))
                        if (openPlayer!=0):
                            battle.append([ID,openPlayer])
                            self.csocket.send("bat2".encode('utf-8'))
                            openPlayer = 0
                            confirmedCon = 1
                            passer = 1
                        else:
                            openPlayer = ID
                            self.csocket.send("no".encode('utf-8'))
                            passer = 1
                            turn = 1
                            activeTurns.append(ID)
                    if (msg[2]=="1"):
                        array.append(ID)
                        print("Added "+ str(ID))
                        if (openPlayer1!=0):
                            battle.append([ID,openPlayer1])
                            self.csocket.send("bat2".encode('utf-8'))
                            openPlayer1 = 0
                            confirmedCon = 1
                            passer = 1
                        else:
                            openPlayer1 = ID
                            self.csocket.send("no".encode('utf-8'))
                            passer = 1
                            turn = 1
                            activeTurns.append(ID)
                    if (int(msg[2])>1):
                        array.append(ID)
                        print("Added "+ str(ID))
                        if (openPlayer2!=0):
                            battle.append([ID,openPlayer2])
                            self.csocket.send("bat2".encode('utf-8'))
                            openPlayer2 = 0
                            confirmedCon = 1
                            passer = 1
                        else:
                            openPlayer2 = ID
                            self.csocket.send("no".encode('utf-8'))
                            passer = 1
                            turn = 1
                            activeTurns.append(ID)
                elif(msg=="T1"):
                    i = 0
                    moveSent = 0
                    print("got button 1")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],1])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                collision = 1
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],1])
                                collision = 0
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T2"):
                    i = 0
                    moveSent = 0
                    print("got button 2")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],2])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],2])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T3"):
                    i = 0
                    moveSent = 0
                    print("got button 3")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],3])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],3])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T4"):
                    i = 0
                    moveSent = 0
                    print("got button 4")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],4])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],4])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T5"):
                    i = 0
                    moveSent = 0
                    print("got button 5")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],5])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],5])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T6"):
                    i = 0
                    moveSent = 0
                    print("got button 6")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],6])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],6])
                                collision = 0
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T7"):
                    i = 0
                    moveSent = 0
                    print("got button 7")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],7])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],7])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T8"):
                    i = 0
                    moveSent = 0
                    print("got button 8")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],8])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],8])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
                elif(msg=="T9"):
                    i = 0
                    moveSent = 0
                    print("got button 9")
                    while i < len(battle):
                        x = 0
                        while x<len(battle[i]):
                            if ID == battle[i][x] and x==0:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][1])
                                oppMove.append([battle[i][1],9])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            elif ID == battle[i][x] and x==1:
                                activeTurns.remove(ID)
                                activeTurns.append(battle[i][0])
                                oppMove.append([battle[i][0],9])
                                turn = 0
                                passer = 1
                                moveSent = 0
                            x = x+1
                        i = i+1
        print ("user disconnected...")

LOCALHOST = "127.0.0.2"
PORT = 8080
server = socket.socket()
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
clientId=1
openPlayer=0
openPlayer1=0
openPlayer2=0
array = list()
battle = list()
activeTurns = list()
oppMove = list()
collision = 0
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()

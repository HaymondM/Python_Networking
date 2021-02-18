#cleint
import socket
from tkinter import *

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
play = True

x = 'shoot'

def setText():
    btn['text'] = 'Submitted'
    x = 'rock'
    return x



root = Tk()

root.geometry('100x100') 

btn = Button(root, text = 'Rock', bd = '5',
                          command = setText) 
btn.pack(side = 'top')    
 
root.mainloop()

print(x)

while play == True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        s.connect((HOST, PORT))
        print("Connected to the server: " + HOST)
        user_input = input('Rock, papaer, or Scissor?').lower()
        user_input = bytes(user_input, 'utf-8') 
        s.sendall(user_input)
        data = s.recv(1024)
        print(data.decode()) # print out result
        play_again = input("Play again?(Y/N)").lower()
        if play_again == 'n':
            play = False
            #break


   

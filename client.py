#cleint
import socket
#import main
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
play = True
play_again = ''
#user_input = b''


root = tk.Tk()
root.geometry('500x400')
root.configure(bg='#0059b3')
root.resizable(False, False)
root.title('Rock, Paper, Scissors')

rock_icon = tk.PhotoImage(file='rock.png')
paper_icon = tk.PhotoImage(file='paper.png')
scissor_icon = tk.PhotoImage(file='scissor.png')

def rock_clicked():
    user_input = b'rock'
    return user_input

def paper_clicked():
    user_input = b'paper'
    return user_input

def scissor_clicked():
    user_input = b'scissor'
    return user_input



#make the buttons
rock_button = ttk.Button(
    root,
    image=rock_icon,
    command=rock_clicked
)

paper_button = ttk.Button(
    root,
    width=10,
    image=paper_icon,
    command=paper_clicked
)

scissor_button = ttk.Button(
    root,
    image=scissor_icon,
    command=scissor_clicked
)

#place on canvas
rock_button.place(x = 20,
        y = 20,
        width=200,
        height=100)

paper_button.place(x = 275,
        y = 20,
        width=200,
        height=100)

scissor_button.place(x = 150,
y = 200,
width=200,
height=100)

root.mainloop() 
 


while play:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #user_input = b'rock'
        s.connect((HOST, PORT))
        print("Connected to the server: " + HOST)
        user_input = input('Rock,Paper, or Scissor?').lower()
        user_input = bytes(user_input, 'utf-8')
        if rock_clicked == b'rock':
            user_input = b'rock'
        if paper_clicked == b'paper':
            user_input = b'paper'
        if scissor_clicked == b'scissor':
            user_input = b'scissor'
        print(user_input)
        s.sendall(user_input)
        data = s.recv(1024)
        print(data.decode()) # print out result
        play_again = input("Play again?(Y/N)").lower()
        #print(play_again) 
        if play_again == 'n':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b'stop')
                print("Thanks for playing!")
                break



          

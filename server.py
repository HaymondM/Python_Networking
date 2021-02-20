#server
import socket
import random

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


while True:
    n = random.randint(0,2)
    rpc = ['rock','paper','scissors']
    print(rpc[n])
    final = 'Error'
    choice = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        user_data =b''
        with conn:
            print('Connected by', addr)
            while True:
                user_data = conn.recv(1024)
                server_move = bytes(rpc[n], 'utf-8')
                #print(user_data)
                if user_data == b'stop':
                    break

                if server_move == b'rock':
                    choice = 'rock'
                    if user_data == b'rock':
                        final = 'A tie!'
                    if  user_data == b'paper':
                        final = 'You won!'
                    if  user_data == b'scissors':
                        final = 'I won!'

                if server_move == b'paper':
                    choice = 'paper'
                    if user_data == b'rock':
                        final = 'I won!'
                    if  user_data == b'paper':
                        final = 'It \'s tie!'
                    if  user_data == b'scissors':
                        final = 'You won!'

                if server_move == b'scissors':
                    choice = 'scissors'
                    if user_data == b'rock':
                        final = 'You won'
                    if  user_data == b'paper':
                        final = 'I won!'
                    if  user_data == b'scissors':
                        final = 'Tie!'
                
                #print(user_data)
                final_d = ('My choice was ' + choice + '. ' + final)
                final_d = bytes(final_d, 'utf-8')

                
                conn.sendall(final_d)
                print("Connection ended")
                break
            #print(user_data)
            if user_data == b'stop':
                    print("Sever Stoped!")
                    break
            
  

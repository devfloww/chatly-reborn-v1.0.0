"""
    This is version 1.0.0 of Chatly reborn: a small project developed by Ebae-b. Started on 2nd of May, 2024. 
"""
from datetime import datetime
import socket
import threading

# Constants (per se)
bufferSize = 1024 # a standard buffer size

# The chatly class
class Chatly:
    """ The main Class of the Application itself """
    def __init__(self, ip, port):

        # Configs
        self.ip = ip
        self.port = port
        self.userName = input("Enter a userName: ")

        self.sockectInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # The server state of the app
    def startServer(self):
        # Binding the configs
        self.sockectInstance.bind((self.ip, self.port))

        # Start listening
        self.sockectInstance.listen(10)
        print(f"Listening on {self.ip}:{self.port} for maximum of 10 seconds...")

        # Accepting connection from client
        client, addr = self.sockectInstance.accept()
        print(f"Connection Accepted from {addr}")


        # The chat itself
        print("\n ----- CHAT ----- \n")

        def recieveMessage():
            while True:
                recievedMessage = client.recv(bufferSize).decode()
                if recievedMessage:
                    print(f"{recievedMessage}") # Printing recieved message first
                else:
                    continue
        def sendMessage():
                while True:
                    message = input('')
                    if message == "quit":
                        self.sockectInstance.close()
                        print("\nQuiting the program!")
                        quit()
                    elif message == "":
                        continue
                    else:
                        time = datetime.now().strftime("%H:%M:%S")
                        message = self.userName + ": " +  message + f"{f'--{time}--':>20}"
                        client.send(message.encode())

        def chat():
            serverThread = threading.Thread(target=recieveMessage, daemon=True)
            serverThread.start()
        chat()
        sendMessage()

    # The client state of the app
    def startClient(self):

        # Trying to connect to Server
        try:
            self.sockectInstance.connect((self.ip, self.port))
            print(f"Connected to {self.ip}:{self.port}")
        except OSError:
            print(f"Connection failed: {self.ip} is probably offline!")
            quit()

        # The chat itself
        print("\n ----- CHAT ----- \n")
        def sendMessage():
            while True:
                message = input('')
                if message == "quit":                        
                    self.sockectInstance.close()
                    print("\nQuiting the program!")
                    quit()
                elif message == "":
                    continue
                else:
                    time = datetime.now().strftime("%H:%M:%S")
                    message = self.userName + ": " + message + f"{f'--{time}--':>20}"
                    self.sockectInstance.send(message.encode())

        def recieveMessage():
            while True:
                recievedMessage = self.sockectInstance.recv(bufferSize).decode()
                if recievedMessage:
                    print(f"{recievedMessage}") # Printing the message
                else:
                    continue    
        def chat():
            clientThread = threading.Thread(target=recieveMessage, daemon=True)
            clientThread.start()
        chat()
        sendMessage()

# Notes:
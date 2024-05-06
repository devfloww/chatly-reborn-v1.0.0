"""
    This is the file that runs the server instance of the app
"""
# Importing Dependencies
from argparse import ArgumentParser

# Importing The chalty class
from Main import Chatly

# Importing Banner
from Banner import Banner

# Creating the argument parser instance
parser = ArgumentParser(description="Chatly reborn: v1.0.0. A cli based chat program.")

# Adding the arguments 
parser.add_argument("-i", "--ipaddr", type=str, help="Supply your public IP address.")
parser.add_argument("-p", "--port", type=int, help="Supply the port you want to communicate on.")

args = parser.parse_args()

givenIP = args.ipaddr
givenPort = args.port

if givenIP and givenPort:
    Banner.bannerWithArgsServer()
    server = Chatly(givenIP, givenPort)
    server.startServer()
else:
    config = Banner.bannerWithoutArgsServer()
    server = Chatly(config[0], config[1])
    server.startServer()

import socket, threading, datetime, queue
import os, json, time, random, string

class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 12345
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.clients = []            
        self.client_data = {}        
        self.lock = threading.Lock()
        self.running = True

        print(f"Server initialized on {self.host}:{self.port}")

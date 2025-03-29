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
    
    def start(self):
        print("Waiting for clients to connect...")
        while len(self.clients) <3:
            conn,addr = self.server_socket.accept()
            print(f"Client connected from {addr[0]}:{addr[1]}")
            self.clients.append(conn)
            client_id = len(self.clients) - 1
            self.client_data[conn] = {"id": client_id}
            thread = threading.Thread(target=self.handle_client, args=(conn, client_id))
            thread.daemon = True
            thread.start()
        print("Both clients connected. Chat can begin!")




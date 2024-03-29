import socket

def echo_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((host, port))
    
    server_socket.listen()
    print(f"Echo server is listening on {host}:{port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        data = client_socket.recv(1024)
        
        client_socket.sendall(data)        
        client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    
    echo_server(host, port)
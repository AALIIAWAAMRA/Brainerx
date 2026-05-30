import socket

HOST = '127.0.0.1'
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
   server_socket.bind((HOST, PORT))
   server_socket.listen(1)
   print(f"[INFO] Server is running and listening on {HOST}:{PORT}...")

   conn, addr = server_socket.accept()
   with conn:
      print(f"[SUCCESS] Connected successfully by: {addr}")
      
      message = "Welcome! Connection is now open. Type anything to reply.\n"
      conn.sendall(message.encode('utf-8'))
      
      while True:
            data = conn.recv(1024)
            if not data:
               break
            
            print(f"[CLIENT]: {data.decode('utf-8').strip()}")
            
            response = "Message received!\n"
            conn.sendall(response.encode('utf-8'))

print("[INFO] Connection closed.")


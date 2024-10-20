# Brian lesko 

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ('10.42.0.117', 8000)  # Replace with the client's IP address and port
client.bind(client_address)
print('Client is listening at', client_address)
while True: 
    chunk, addr = client.recvfrom(1000)
    print(chunk.decode('utf-8'))



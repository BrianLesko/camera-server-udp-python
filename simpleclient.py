import socket
import cv2
import numpy as np

# Create a UDP socket
print("getting ready to create a socket")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the client to a specific address (optional)
client_address = ('10.42.0.117', 8000)  # Replace with the client's IP address and port
client.bind(client_address)
print('Client is listening at', client_address)

data = b''  # initialize the data variable
buffer_size = 65536  # Set a more reasonable buffer size

while True:
    chunk, addr = client.recvfrom(buffer_size)
    if chunk == b'END':  # check for the "END" delimiter
        try:
            frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            # show the image
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            print('Error deserializing the frame:', e)
        data = b''  # reset the data for the next frame
    else:
        data += chunk

# Release resources
cv2.destroyAllWindows()
client.close()
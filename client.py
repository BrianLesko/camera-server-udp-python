
# display the image in the client using streamlit web browser

import socket
import cv2
import numpy as np
import streamlit as st

col1, col2, col3 = st.columns([1,9,1])
with col2: image_spot = st.empty()

# Create a UDP socket
print("getting ready to create a socket")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the client to a specific address (optional)
client_address = ('10.42.0.117', 8000)  # Replace with the client's IP address and port
client.bind(client_address)
print('Client is listening at', client_address)

data = b''  # initialize the data variable
while True:
    chunk, addr = client.recvfrom(90000)
    if chunk == b'END':  # check for the "END" delimiter
        try: 
            frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            # show the image
            with image_spot:
                st.image(frame, channels="BGR", width=800)  # Set the width to the desired value
        except:
            print('Error deserializing the frame')
            data = b''
        data = b''  # reset the data for the next frame
    else:
        data += chunk




# display the image in the client using streamlit web browser

import socket
import cv2
import numpy as np
import streamlit as st

col1, col2, col3 = st.columns([1,9,1])
with col2: image_spot = st.empty()

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the client to a specific address (optional)
client_address = ('172.20.10.2', 8000)  # Replace with the client's IP address and port
client.bind(client_address)
print('Client is listening at', client_address)

data = b''  # initialize the data variable
while True:
    chunk, addr = client.recvfrom(1000)
    if chunk == b'END':  # check for the "END" delimiter
        try: 
            # print the length of the data
            #print('Length of data:', len(data))
            frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            # show the image
            with image_spot:
                frame_resized = cv2.resize(frame, None, fx=6, fy=6)
                st.image(frame_resized, channels="BGR")
        except:
            with image_spot: st.image(np.zeros([100, 100, 3], dtype=np.uint8))
            print('Error deserializing the frame')
        data = b''  # reset the data for the next frame
    else:
        data += chunk



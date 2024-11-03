import numpy as np
import cv2  # pip install opencv-python-headless
import socket
import argparse

camera = cv2.VideoCapture(0)  # on a mac you can use either your mac webcam or an iphone camera using continuity camera! for me, my iphone was (1) and my mac webcam was (0)
# Limit the size and FPS to increase speed
camera.set(cv2.CAP_PROP_FPS, 60)  # FPS
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # compression method

def get_frame(): 
    global camera
    try: 
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)  # this line flips the image
        return frame
    except:
        return np.zeros((300, 300, 3))

def main(client_ip):
    # UDP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('Host:', host_ip)
    server.bind((host_ip, 8000))  # Bind the socket to a specific address

    client_address = (client_ip, 8000)  # Use the passed client IP address

    while True:
        frame = get_frame()
        data = cv2.imencode('.jpg', frame)[1].tobytes()

        # Split the data into chunks
        chunk_size = 500  # Maximum UDP packet size
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            server.sendto(chunk, client_address)
        server.sendto(b'END', client_address)  # send an empty chunk to signal the end of the frame

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LAN server for live data feed")
    parser.add_argument("client_ip", type=str, help="Client IP address to send data to")
    args = parser.parse_args()
    main(args.client_ip)

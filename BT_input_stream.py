"""
Bluetooth Input Stream

stream_input() is a generator that start up the 
bluetooth serial server via PyBluez and yields
events sent from a device

Ex:
    # print data send from bluetooth device
    for event in stream_input():
        print(event)  

Note: pairing must be done prior to this. 
Once paired, running this will allow a connection
"""
from bluetooth import *


def stream_input():
    MIN_INT = 0
    MAX_INT = 255
    while True:
        client_sock, server_sock = _init_connection()
        try:
            last = 0.0
            while True:
                data = client_sock.recv(100)
                if len(data) == 0: break
                input = data.decode('utf-8')
                if input.isdigit():
                    inter = int(input)
                    input = inter/MAX_INT if inter<=MAX_INT else last
                yield input
                last = input
        except IOError:
            pass
        _close_connection(client_sock,server_sock)


def _init_connection():
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service( server_sock, "SampleServer",
                    service_id = uuid,
                    service_classes = [ uuid, SERIAL_PORT_CLASS ],
                    profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                        )
                    
    print("Waiting for connection on RFCOMM channel %d" % port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)
    return client_sock, server_sock

def _close_connection(client_sock,server_sock):
    print("disconnected")
    client_sock.close()
    server_sock.close()
    print("all done")
    return


if __name__ == "__main__":
    for event in stream_input():
        print(event)    

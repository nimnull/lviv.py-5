#!/usr/bin/env python
import click
import zmq


context = zmq.Context()
# subscriber = context.socket(zmq.SUB)


@click.group()
def main():
    pass


@main.command()
def client():
    socket = context.socket(zmq.REQ)
    socket.connect('ipc://lvivpy-feed')
    for req in range(10):
        socket.send(b"Hello")
        msg = socket.recv()
        print("Recived reply [%s] %s" % (req, msg,))
    pass


@main.command()
def server():
    socket = context.socket(zmq.REP)
    socket.bind('ipc://lvivpy-feed')
    while True:
        msg = socket.recv()
        print("Recieved: %s" % msg)
        socket.send(b'World')

if __name__ == '__main__':
    main()

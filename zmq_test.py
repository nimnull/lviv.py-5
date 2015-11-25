#!/usr/bin/env python
import click
import zmq
import time
import statistics
import numpy
import numpy.matlib

context = zmq.Context()
# subscriber = context.socket(zmq.SUB)
TIMES = 1000
SHAPE = (1000, 1000,)


@click.group()
def main():
    # print("Current libzmq version is %s" % zmq.zmq_version())
    # print("Current  pyzmq version is %s" % zmq.__version__)
    pass


@main.command()
def client():
    matrix = numpy.matlib.randn(SHAPE)
    print("Size: %.2f Mb" % (matrix.nbytes / 1024 / 1024))
    socket = context.socket(zmq.REQ)
    socket.connect('ipc://lvivpy-feed')
    for req in range(TIMES):
        matrix.itemset((0, 0), time.time())
        socket.send(matrix.tobytes())
        msg = socket.recv()
    pass


@main.command()
def server():
    socket = context.socket(zmq.REP)
    socket.bind('ipc://lvivpy-feed')
    results = []
    while True:
        msg = socket.recv()
        matrix = numpy.fromstring(msg)
        # convert np array into original matrix of the SHAPE
        sent_at = matrix.reshape(SHAPE).item((0, 0))
        elapsed = (time.time() - sent_at) * 1000
        results.append(elapsed)
        if len(results) >= TIMES:
            print(sent_at)
            print("Recieved: %s, " % statistics.mean(results))
        socket.send(str(len(results)).encode())

if __name__ == '__main__':
    main()

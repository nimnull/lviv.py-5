import os
import time
import numpy.matlib


SHAPE = (1000, 1000,)


def child_process(matrix):
    print("\nNew child created %s\n", os.getpid())
    time.sleep(20)
    print("Size: %s" % matrix.size)
    matrix.sort()
    time.sleep(20)
    print("Consumed %s \n" % matrix.nbytes)

    os._exit(0)


def parent_process(matrix):
    pass


def parent():
    matrix = numpy.matlib.randn(SHAPE)
    while True:
        newpid = os.fork()
        print("New pid: %s\n" % newpid)
        if newpid is 0:
            child_process(matrix)
        else:
            parent_process(matrix)
        reply = input("\nq for quit / c for new fork:")
        if reply == 'c':
            continue
        else:
            break


if __name__ == '__main__':
    parent()

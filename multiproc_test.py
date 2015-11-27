import click
import numpy.matlib
import time

from multiprocessing import Process, Pipe


SHAPE = (1000, 1000,)


def pipe_worker(conn):

    while True:
        matrix = conn.recv()
        print("Got matrix of %d elements" % matrix.size)
        time.sleep(30)
        print('Loop\n')

    conn.close()


@click.group()
def cli():
    pass

# @cli.command()
# def queue():
#     pass


@cli.command()
def pipe():
    parent_conn, child_conn = Pipe()
    p = Process(target=pipe_worker, args=(child_conn,))
    p.start()
    matrix = numpy.matlib.randn(SHAPE)
    val = input("Continue? (y/n):")

    while val == 'y':
        parent_conn.send(matrix)
        val = input("Continue? (y/n):")

    p.join()


if __name__ == '__main__':
    cli()

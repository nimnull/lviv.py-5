import time
from multiprocessing import Process
import os.path as path
import numpy as np
import numpy.matlib

from tempfile import mkdtemp


SHAPE = (1000, 1000,)


def main():
    filename = path.join(mkdtemp(), 'data.dat')
    data = np.memmap(filename, dtype='float32', mode='w+', shape=SHAPE)
    matrix = numpy.matlib.randn(SHAPE)[:]
    time.sleep(20)
    data[:] = matrix
    p = Process(target=calculation, args=(data,))
    p.start()

    # pool = multiprocessing.Pool()
    # results = pool.imap(calculation, chunks(data))
    # results = np.fromiter(results, dtype=np.float)
    p.join()


# def chunks(data, chunksize=1000):
#     intervals = range(0, data.size + 1, chunksize)
#     for start, stop in zip(intervals[:-1], intervals[1:]):
#         yield np.array(data[start:stop])


def calculation(data):
    data.sort()
    res = data.mean() - data.std()
    print(data.nbytes / 1024 / 1024)
    print(res)
    time.sleep(20)

if __name__ == '__main__':
    main()

import json
import base64

import numpy
import numpy.matlib


def main():
    SHAPE = (1000, 1000,)
    matrix = numpy.matlib.randn(SHAPE)

    encoded = json.dumps([
        str(matrix.dtype),
        base64.b64encode(matrix).decode(),
        matrix.shape
    ])
    # print(encoded)

    decoded = json.loads(encoded)
    data_type = numpy.dtype(decoded[0])
    data_array = numpy.frombuffer(base64.decodestring(decoded[1].encode()),
                                  data_type)
    return data_array.reshape(decoded[2])


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main"))

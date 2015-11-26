import json
import base64
import pickle
import ujson
import msgpack

import numpy
import numpy.matlib


SHAPE = (100, 100,)


def serializer1(json_serializer):

    matrix = numpy.matlib.randn(SHAPE)

    encoded = json_serializer.dumps(matrix.tolist())
    # print(encoded)

    decoded = json_serializer.loads(encoded)
    # data_type = numpy.dtype(decoded[0])
    # data_array = numpy.frombuffer(base64.decodestring(decoded[1].encode()),
    #                               data_type)
    return numpy.array(decoded).reshape(SHAPE)

def serializer2(serializer):
    matrix = numpy.matlib.randn(SHAPE)

    encoded = serializer.dumps([
        str(matrix.dtype),
        base64.b64encode(matrix).decode(),
        matrix.shape
    ])
    decoded = serializer.loads(encoded)
    data_type = numpy.dtype(decoded[0])
    if isinstance(decoded[1], bytes):
        data_frame = decoded[1]
    else:
        data_frame = decoded[1].encode()
    data_array = numpy.frombuffer(base64.decodestring(data_frame), data_type)
    return data_array.reshape(decoded[2])


def ujson_test1():
    return serializer1(ujson)


def json_test1():
    return serializer1(json)


def msgpack_test1():
    return serializer1(msgpack)

def pickle_test1():
    return serializer1(pickle)


def ujson_test2():
    return serializer2(ujson)


def json_test2():
    return serializer2(json)


def msgpack_test2():
    return serializer2(msgpack)


def pickle_test2():
    return serializer2(pickle)


if __name__ == '__main__':
    import timeit

    for test in ['test1', 'test2']:
        for serializer in ['json', 'ujson', 'msgpack', 'pickle']:
            test_method = "%s_%s" % (serializer, test,)
            print("%(serializer)s %(test)s: %(result)s ms" % {
                  'serializer': serializer,
                  'test': test,
                  'result': timeit.timeit("%s()" % test_method,
                                          setup="from __main__ import %s" % test_method,
                                          number=1000)
            })

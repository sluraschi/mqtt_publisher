from collections import Mapping, Container
from itertools import islice
from sys import getsizeof

CHUNK_SIZE = 100 * 1000  # 100kb
SEGMENT_LINES = 13


def deep_getsizeof(o, ids):
    # Find the memory footprint of a Python object
    #
    # This is a recursive function that drills down a Python object graph
    # like a dictionary holding nested dictionaries with lists of lists
    # and tuples and sets.
    #
    # The sys.getsizeof function does a shallow size of only. It counts each
    # object inside a container as pointer only regardless of how big it
    # really is.
    d = deep_getsizeof
    if id(o) in ids:
        return 0

    r = getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str) or isinstance(0, unicode):
        return r

    if isinstance(o, Mapping):
        return r + sum(d(k, ids) + d(v, ids) for k, v in o.iteritems())

    if isinstance(o, Container):
        return r + sum(d(x, ids) for x in o)
    return r


def get_next_segment(file):
    lines = [x.strip() for x in islice(file, SEGMENT_LINES)]
    return '\n'.join(lines)


def get_all_segments(file):
    segments = list()
    while True:
        next_seg = get_next_segment(file)
        if not next_seg:
            break
        segments.append(next_seg)
    return segments


def split_by_size(file_path):
    with open(file_path, "rb") as f:
        chuncks = list()
        print 'empty chunks size:', getsizeof(chuncks)

        while True:
            piece_of_file = f.read(CHUNK_SIZE)
            print 'piece_of_file size:', getsizeof(piece_of_file)
            print piece_of_file
            if piece_of_file == "":
                break
            chuncks.append(piece_of_file)
            chuncks_size = deep_getsizeof(chuncks, set())
            print 'chuncks size:', getsizeof(chuncks)
            print 'chuncks and contents size:', chuncks_size
    print 'amount of chuncks to send:', len(chuncks)
    return chuncks

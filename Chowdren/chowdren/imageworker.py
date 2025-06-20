from mmfparser import zopfli
import zlib

def worker(in_queue):
    while True:
        obj = in_queue.get()
        if obj is None:
            return
        data, index, p, cache_path = obj
        print 'Compressing %s (%s)' % (index, p)
        #data = zopfli.compress(data)
        data = zlib.compress(data)
        open(cache_path, 'wb').write(data)

import time 
import lzma
import gzip
import bz2

data = b'This is some sample data' * 990000

print('Original data size:', len(data))

start = time.time()
compessed_data_lzma = lzma.compress(data)
end = time.time()

print(end - start)

import time 
import lzma
import gzip
import bz2

data = b'This is some sample data' * 999000
print("------------------------------------")
print('Original data size:', len(data))

print("----------------lzma compress--------------------")
start = time.time()
compessed_data_lzma = lzma.compress(data)
end = time.time()

print(end - start)
print(f"lzma compress data: {len(compessed_data_lzma)}")


print("---------------gzip compress---------------------")
start = time.time()
compessed_data_gzip = gzip.compress(data)
end = time.time()

print(end - start)
print(f"gzip compress data: {len(compessed_data_gzip)}")



print("---------------bz2 compress---------------------")
start = time.time()
compessed_data_bz2 = bz2.compress(data)
end = time.time()

print(end - start)
print(f"bz2 compress data: {len(compessed_data_bz2)}")

import time
import lzma



# compress the file from "txt" to "zip"
with open('3. data_compression\\file.txt', 'rb') as f_in, lzma.open('3. data_compression\\file.zip', 'wb') as f_out:
    f_out.write(f_in.read())
    
# decompress the file from "zip" to "txt"
with lzma.open('3. data_compression\\file.zip', 'rb') as f_in, open('3. data_compression\\uncompressed.txt', 'wb') as f_out:
    f_out.write(f_in.read())





# compress the file from "txt" to "xz"
# with open('3. data_compression\\file.txt', 'rb') as f_in, lzma.open('3. data_compression\\file.xz', 'wb') as f_out:
#     f_out.write(f_in.read())
  
    
# decompress the file from "xz" to "txt"
# with lzma.open('3. data_compression\\file.xz', 'rb') as f_in, open('3. data_compression\\uncompressed.txt', 'wb') as f_out:
#     f_out.write(f_in.read())
    
    
    
    


   
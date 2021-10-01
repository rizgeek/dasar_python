import time
start_time = time.time()

print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')


for i in range(1, 100000000) :
    a = 10

print(time.time() - start_time, "detik"); 



# compile ke bytecode : py -m py_compile nama_file.py
# proses compile ke bytecode akan membuat proses running program akan lebih cepat.
# karena compile program ke bytecode akan membuat proses eksekusi lebih cepat karena program akan lansung di jalankan oleh prosesor dan tidak melalui interpreter sebagai penerjemah


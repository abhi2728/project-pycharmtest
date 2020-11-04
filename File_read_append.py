file_read = open('sample_data.csv', 'r')
if file_read.readable():
    for line in file_read.readlines():
        print(line)
file_read.close()

file_append = open('sample_data.csv', 'a')
if file_append.writable():
    file_append.write('\n6, 30, 1')
file_append.close()

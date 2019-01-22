# 实现监听文件输入
def tailf(filename):
    f = open(filename)
    while True:
        line = f.readline()
        if line.strip():
            yield line.strip()
    f.close()

g = tailf('file.txt')
for i in g:
    print(i)

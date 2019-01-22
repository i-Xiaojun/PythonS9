def wahaha():
    for i in range(50000):
        yield 'wahaha%s'%i

for i in wahaha():
    print(i)
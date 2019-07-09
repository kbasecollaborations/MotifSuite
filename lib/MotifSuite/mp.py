from multiprocessing import Process

def func1(name='1'):
    print("function, %s" % name)
    for i in range(1,100000000):
        x=i*i

def func2(name='2'):
    print("function, %s" % name)
    for j in range(1,100000000):
        y=j*j

def func3(name='3'):
    print("function, %s" % name)
    for i in range(1,100000000):
        x=i*i

def func4(name='4'):
    print("function, %s" % name)
    for j in range(1,100000000):
        y=j*j


p1 = Process(target=func1)
p1.start()
p1.join()
p2 = Process(target=func2)
p2.start()
p2.join()
p3 = Process(target=func3)
p3.start()
p3.join()
p4 = Process(target=func4)
p4.start()
p4.join()
'''
p1.join()
p2.join()
p3.join()
p4.join()
'''

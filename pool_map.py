from multiprocessing import Pool
from time import sleep,time


def fun(fn):
    sleep(1)
    return fn*fn


test = [1, 2, 3, 4, 5, 6]

print('顺序执行:')
s = time()
for i in test:
    fun(i)
e = time()
print('执行时间', e-s)

pool = Pool(processes=6)
r = pool.map(fun, test)
pool.close()
pool.join()
print('最后执行时间',time()-e)

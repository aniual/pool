import multiprocessing as mp
from time import sleep
import os


def worker(msg):
    sleep(1)
    print(msg)
    return 'worker return' + msg


# 创建进程池对象,进程池中包含4个进程
pool = mp.Pool(processes=4)
result = []
for i in range(50):
    msg = 'hello %d' % i
    # 向进程池中加入要执行的事件
    r = pool.apply_async(worker, (msg,))
    result.append(r)

# 获取每个时间函数的返回值
for res in result:
    print(res.get())

# 关闭进程池事件加入通道,即不能在向进程池中加入事件
pool.close()

# 阻塞等待进程池事件结束后回收进程池
pool.join()

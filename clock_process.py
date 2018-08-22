from multiprocessing import Process
import time


class ClockProcess(Process):
    def __init__(self, value):
        Process.__init__(self)
        self.value = value

    # 在process类中重写方法
    def run(self):
        n = 5
        while n > 0:
            print('The time is {}'.format(time.ctime()))
            time.sleep(self.value)
            n -= 1


# 使用自己的进程类创建进程的对象
p = ClockProcess(1)
# start后会自动执行run函数
p.start()
p.join()

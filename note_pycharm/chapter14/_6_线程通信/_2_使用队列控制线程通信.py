"""
    14.6.2 使用队列控制线程通信
"""
import queue
import threading
import time


# 测试阻塞队列的put get 方法
# bq = queue.Queue(2)
# bq.put('python')
# bq.put('python')
# print('111111111111111111')
# bq.put('oython')
# print('222222222222')
def product(bq):
    str_tuple = ('Python', 'Kotlin', 'Swift')
    for i in range(99999):
        print(threading.current_thread().name + '生产者准备生产组元素！')
        time.sleep(0.2)
        bq.put(str_tuple[i % 3])
        print(threading.current_thread().name + "生产者生产元组元素完成！")


def consume(bq):
    while True:
        print(threading.current_thread().name + "消费者准备消费元组元素！")
        time.sleep(0.2)
        t = bq.get()
        print(threading.current_thread().name + "消费者消费[%s]元素完成！" % t)


bq = queue.Queue(maxsize=1)

threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()

threading.Thread(target=consume, args=(bq,)).start()

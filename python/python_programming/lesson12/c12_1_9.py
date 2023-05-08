"""スレッドをまとめてjoinする"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')

if __name__ == '__main__':
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.daemon = True
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
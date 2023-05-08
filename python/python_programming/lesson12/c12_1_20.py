"""ロック"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker2(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker3(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=worker1, args=(lock, ))
    t2 = threading.Thread(target=worker2, args=(lock, ))
    t3 = threading.Thread(target=worker3, args=(lock, ))
    t1.start()
    t2.start()
    t3.start()
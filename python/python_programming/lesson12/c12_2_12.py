"""マップでの実行にtimeoutを設定する"""
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i

if __name__ == '__main__':
    with multiprocessing.Pool(3) as p:
        r = p.map_async(worker1, [100, 200])
        logging.debug('executed')
        logging.debug(r.get(timeout=1))
"""ProcessPoolExecutorでマルチプロセスの処理を実行"""
import concurrent.futures
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker(x, y):
    logging.debug('start')
    time.sleep(3)
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        f1 = executor.submit(worker, 2, 5)
        f2 = executor.submit(worker, 2, 5)
        logging.debug(f1.result())
        logging.debug(f2.result())

if __name__ == '__main__':
    main()
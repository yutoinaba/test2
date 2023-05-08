"""パイプでデータを受け取る"""
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def f(conn):
    conn.send(['test'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn,))
    p.start()
    logging.debug(child_conn.recv())
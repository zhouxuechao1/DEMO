"""
多线程
"""

import _thread
import logging
from time import sleep, ctime

logging.basicConfig(filename='train_log', format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S ',
                    level=logging.INFO)

loops = [2, 4]
def loop0(nloop, nsec, lock):
    logging.info("start loop" + nloop + "at " + ctime())
    sleep(nsec)
    logging.info("end loop" + nloop + "at " + ctime())


def main():
    logging.info("start all at" + ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    logging.info("end all at" + ctime())

if __name__ == '_main_':
    main()
import logging
import os

path = os.path.dirname(os.path.abspath(__file__))
logfile = f'{path}\\app1.log'


logging.basicConfig(
    level=logging.DEBUG,
    filename=logfile,
    filemode='w', # a : append, w: write
    format='%(levelname)s -- %(asctime)s -- %(filename)s:%(lineno)s --%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

logging.debug(f'This is a DEBUG ({logging.DEBUG}) level log')
logging.info(f'This is a INFO ({logging.INFO}) level log')
logging.warning(f'This is a WARNING ({logging.WARNING}) level log')
logging.error(f'This is a ERROR ({logging.ERROR}) level log')
logging.critical(f'This is a CRITICAL ({logging.CRITICAL}) level log')
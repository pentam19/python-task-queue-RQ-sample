import logging
import datetime
from time import sleep

logger = logging.getLogger(__name__)

def add(a, b):
    logger.debug('START: {} + {} = {}'.format(a, b, a + b))
    sleep(3)

    filepath = 'task_created_file.txt'
    with open(filepath, 'a') as f:
        print(datetime.datetime.now(), file=f)
    
    logger.debug('COMPLETE: {} + {} = {}'.format(a, b, a + b))
    return a + b


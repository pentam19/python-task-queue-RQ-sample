import os
from time import sleep
import redis
from rq import Queue
from tasks import add

q = Queue(connection=redis.from_url(os.environ.get('RQ_REDIS_URL')))

# タスクをキューに投げる
tasks = [q.enqueue(add, args=(i, 1)) for i in range(10)]

# タスクが完了するまで待って、結果を出力する場合
#sleep(1)
#print([task.result for task in tasks])


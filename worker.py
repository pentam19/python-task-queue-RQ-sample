import os
import logging
import redis
import rq

logging.basicConfig(level=logging.DEBUG)

with rq.Connection(redis.from_url(os.environ.get('RQ_REDIS_URL'))):
    worker = rq.Worker(['default'])
    worker.work()


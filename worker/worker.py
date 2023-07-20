import logging
import os
from redis import Redis
import requests
import time
import sys

DEBUG = os.environ.get("DEBUG", "").lower().startswith("y")

log = logging.getLogger(__name__)
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)

def initialize_redis(suffix=None):
    redis_server = "redis"+suffix
    redis = Redis(redis_server)
    return redis

def get_random_bytes(suffix=None):
    r = requests.get("http://rng"+suffix+"/32")
    return r.content


def hash_bytes(data, suffix=None):
    r = requests.post("http://hasher"+suffix+"/",
                      data=data,
                      headers={"Content-Type": "application/octet-stream"})
    hex_hash = r.text
    return hex_hash


def work_loop(interval=1, suffix=None, redis_server):
    deadline = 0
    loops_done = 0
    while True:
        if time.time() > deadline:
            log.info("{} units of work done, updating hash counter"
                     .format(loops_done))
            redis.incrby("hashes", loops_done)
            loops_done = 0
            deadline = time.time() + interval
        work_once(suffix)
        loops_done += 1


def work_once(suffix=None, redis_server):
    log.debug("Doing one unit of work")
    time.sleep(0.1)
    random_bytes = get_random_bytes(suffix)
    hex_hash = hash_bytes(random_bytes, suffix)
    if not hex_hash.startswith('0'):
        log.debug("No coin found")
        return
    log.info("Coin found: {}...".format(hex_hash[:8]))
    created = redis_server.hset("wallet", hex_hash, random_bytes)
    if not created:
        log.info("We already had that coin")


if __name__ == "__main__":
    if sys.argv[1] != None:
        suffix = sys.argv[1]
    redis_server = initialize_redis(suffix)    
    while True:
        try:
            work_loop(suffix, redis_server)
        except:
            log.exception("In work loop:")
            log.error("Waiting 10s and restarting.")
            time.sleep(10)
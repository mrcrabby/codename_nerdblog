'''
Created on Jun 6, 2010

@author: dro
'''
import redis

redisDB = redis.Redis(host='localhost', port=6379, db=0)
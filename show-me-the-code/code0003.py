import redis


from code0001 import genCodes


red = redis.Redis(host='localhost', port=6379)


def insertredis():
    aa = genCodes(200, 15)
    red.sadd('myset', aa)
    xx = red.smembers('myset')
    print(xx)


if __name__ == "__main__":
    insertredis()
        



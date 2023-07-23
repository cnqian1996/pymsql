import redis


def main():
    client = redis.Redis(host='58.213.41.44',
                         port=12309,
                         password='1qaz2wsx')
    client.set('username', 'hellokitty', ex=300)
    print(client.ttl('username'))
    print(client.get('username').decode())
    client.set('nickname', '郑义')
    print(client.get('nickname').decode())
    client.incr('yuting')
    client.incr('yuting', 50)
    print(int(client.get('yuting').decode()))
    client.hset('stu1', 'id', '1001')
    client.hset('stu1', 'name', 'zhengyi')
    print(client.hgetall('stu1'))
    print(client.hget('stu1', 'name').decode())
    client.rpush('list1', 10, 20, 30, 40)
    print(client.lrange('list1',0,-1))


if __name__ == '__main__':
    main()

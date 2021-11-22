def consume():
    while True:
        num = yield
        print('consume %s' % num)

consumer = consume()

next(consumer)

for num in range(0,100):
    print("product %s" % num)
    consumer.send(num)

from datetime import datetime
from random import randint

def consumeResponseTopic(request_promises):
    def consume():
        if request_promises:
            print("{now} YES processing".format(now=datetime.now()))
            request_promise = request_promises.pop(randint(0, len(request_promises) - 1))
            request_id, promise = request_promise[0], request_promise[1]
            promise.callback("Hello {counter}!".format(counter=request_id))
        else:
            print("{now} NO  processing".format(now=datetime.now()))
    return consume

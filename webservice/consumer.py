from datetime import datetime
from random import randint
from twisted.internet.task import LoopingCall


class ResponseTopicConsumer:

    def __init__(self):
        self.request_promises = []

    def run(self, interval=0.5):
        LoopingCall(self.consumer).start(interval)
        return self

    def append(self, element):
        self.request_promises.append(element)

    def pop_random(self):
        random_index = randint(0, len(self.request_promises) - 1)
        return self.request_promises.pop(random_index)

    def consumer(self):
        if self.request_promises:
            print("{now} YES processing".format(now=datetime.now()))
            request_promise = self.pop_random()
            request_id, promise = request_promise[0], request_promise[1]
            promise.callback("Hello {request_id}!".format(request_id=request_id))
        else:
            print("{now} NO  processing".format(now=datetime.now()))

from datetime import datetime
from random import randint
from twisted.internet.task import LoopingCall
from codeasevents.consumer.kafka import KafkaConsumer


class ResponseTopicConsumer:

    def __init__(self):
        self.request_promises = []
        self.response_topic = KafkaConsumer('response_topic')

    def run(self, interval=0.5):
        LoopingCall(self.consumer).start(interval)
        return self

    def append(self, element):
        self.request_promises.append(element)

    def pop_random(self):
        if self.request_promises:
            random_index = randint(0, len(self.request_promises) - 1)
            return self.request_promises.pop(random_index)

    def consumer(self):
        for response in self.response_topic:
            if self.request_promises:
                print("{now} YES processing".format(now=datetime.now()))
                request_promise = self.pop_random()
                request_id, promise = request_promise[0], request_promise[1]
                promise.callback("Hello {request_id} {response}!".format(
                    request_id=request_id, response=response))
            else:
                print("{now} No  processing".format(now=datetime.now()))

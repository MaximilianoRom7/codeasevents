from random import randint


class KafkaConsumer:

    def __init__(self, *args, **kwargs):
        pass

    def __iter__(self):
        if randint(0, 4) == 0:
           yield randint(0, 10)

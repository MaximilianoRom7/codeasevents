#!/usr/bin/env python
from klein import Klein
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.internet.defer import Deferred
from codeasevent.consumer import consumeResponseTopic
from codeasevent.serializer import requestSerializer

app = Klein()

request_promises = []

identity = lambda x: x

counter = 0

LoopingCall(consumeResponseTopic(request_promises)).start(0.5)

@app.route("/")
def index(request):
    global counter
    counter += 1
    # serialized = requestSerializer(request)
    d = Deferred().addCallback(identity)
    # request_promises.append((id(request), d))
    request_promises.append((counter, d))
    return d

if __name__ == '__main__':
    app.run("0.0.0.0", 8080)

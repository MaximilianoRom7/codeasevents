#!/usr/bin/env python
from klein import Klein
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from codeasevents.webservice.consumer import ResponseTopicConsumer
from codeasevents.webservice.serializer import requestSerializer


app = Klein()

responseTopicConsumer = ResponseTopicConsumer().run()

identity = lambda x: x

@app.route("/")
def index(request):
    serialized = requestSerializer(request)
    d = Deferred().addCallback(identity)
    responseTopicConsumer.append((id(request), d))
    return d

if __name__ == '__main__':
    app.run("0.0.0.0", 8080)

#!/usr/bin/env pyth
# -*- coding: utf-8 -*-

from __future__ import division
import numbers, json, jsonpickle, Pyro4, socket, select, exceptions, sys, threading

class test_server_class(object):
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def func1(self, a, b):
        return a+b, 'addition'

def run_pyro_daemon(daemon):
    daemon.requestLoop()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(0)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        host = s.getsockname()[0]
    except socket.error as err:
        print 'Socket Error: ', err
        sys.exit(0)
    finally:
        s.close()

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host, 0))

    servername = sys.argv[1]
    srv = test_server_class(servername, serversocket.getsockname()[0], serversocket.getsockname()[1])

    Pyro4.config.REQUIRE_EXPOSE = False
    daemon = Pyro4.Daemon()
    nameserver = Pyro4.locateNS()
    uri = daemon.register(srv)
    nameserver.register(srv.name, uri)

    thread = threading.Thread(target=run_pyro_daemon, args=(daemon,))
    thread.start()
    print 'Pyro daemon started running...'

    print 'Listening on ' + serversocket.getsockname()[0] + ':' + str(serversocket.getsockname()[1])
    serversocket.listen(5)
    while 1:
        client, address = serversocket.accept()
        print 'Connected by ', address
        try:
            data = client.recv(1024)
            if not data:
                break

            json_obj = json.loads(data)
            print 'expected size of the payload: ' + str(json_obj['size'])
            print 'function to call: ' + json_obj['func']
            print 'actual length of payload: ' + str(len(json_obj['param']))
            print 'parameters: ', jsonpickle.decode(json_obj['param'])
        except KeyboardInterrupt as err:
            print '' + err
            break 

    client.close()
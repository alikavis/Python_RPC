#!/usr/bin/env pyth
# -*- coding: utf-8 -*-

from __future__ import division
import numbers, json, jsonpickle, Pyro4, socket, select, exceptions, time, sys
import test_stub as stub

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(0)

    servername = sys.argv[1]
    stub = stub.test_stub(servername)
    print stub.func1(10, 20, time.time())
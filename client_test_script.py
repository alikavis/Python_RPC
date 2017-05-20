#!/usr/bin/env pyth
# -*- coding: utf-8 -*-

from __future__ import division
import numbers, json, jsonpickle, Pyro4, socket, select, exceptions, time, sys
import test_stub as stub

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        sys.exit(0)

    stub = stub.test_stub()
    print stub.func1(int(sys.argv[1]), int(sys.argv[2]), time.time())
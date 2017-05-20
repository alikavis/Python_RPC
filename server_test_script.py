#!/usr/bin/env pyth
# -*- coding: utf-8 -*-

from __future__ import division
import numbers, json, jsonpickle, Pyro4, socket, select, exceptions, sys, threading
import test_skeleton as skeleton

class A(object):
    def __init__(self, name):
        self.name = name
        self.host = host
        self.port = port

    def func1(self, a, b):
        return a+b, 'addition'

if __name__ == '__main__':
    a = A('test')
    server_skeleton = skeleton.test_skeleton(a)
    print 'Running the server'
    server_skeleton.run()

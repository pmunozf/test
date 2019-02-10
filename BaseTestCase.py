#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Pablo Munoz (c) 2019
#
# Unit test case
#
import unittest
import time

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
        test_name = "%s" % (self.id)
        test_name = test_name.split('testMethod=')[1].replace('>>','').replace('_',' ')
        print("\n\n --------> " + test_name)

    def tearDown(self):
        t = time.time() - self.startTime
        print("\n\t\t\t\t\ttime: %.6f \t[ms]" % (t*1000.0))



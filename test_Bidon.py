#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Unit tests for Bidon
#
# Pablo Munoz (c) 2019
#
import unittest
import numpy as np
from BaseTestCase import BaseTestCase

TEST_NAME = 'Bidon'

class TestCase(BaseTestCase):
    def test_bidon(self):
        print('Test bidon')


if __name__ == '__main__':
    print('\n#### {} Tests ####'.format(TEST_NAME))
    unittest.main()

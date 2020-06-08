# -*- coding: utf-8 -*-
import unittest
from pathAgent import *
import PIL.Image

class Test_pathAgent(unittest.TestCase):

    def setUp(self):
        self.nav = pathAgent()

    def tearDown(self):
        print("test navigation success")

    def test_bulid_map(self):
        self.nav.getpath()



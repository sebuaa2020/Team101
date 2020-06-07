# -*- coding: utf-8 -*-
import unittest
from map import *
import PIL.Image

class Test_map(unittest.TestCase):

    def setUp(self):
        self.map = map()

    def tearDown(self):
        print("test map success")

    def test_bulid_map(self):
        self.map.buildmap()

    def test_save_map(self):
        self.map.savemap()
        im = self.map.savemap()
        im.show()





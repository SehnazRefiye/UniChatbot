# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:28:42 2022

@author: Şehnaz Yıldırım
"""

import unittest
from bindingTheory import *
class Testbinding(unittest.TestCase):
    def test_binding(self):
        if gender == "male":
            self.assertEqual(binding.name(x) , "Anaphor", himself)
        elif gender == "female":
            self.assertEqual(binding.name(x), "Anaphor" , herself)
        else:
            pass
if __name__ == '__main__':
    unittest.main()
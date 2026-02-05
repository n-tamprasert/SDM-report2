#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
    # ========== A is less than 1 (Assume B=500) ==========
    def test_case1(self):
        #"""A=0, B=500 -> invalid"""
        self.assertEqual(-1, calc(0, 500))
    
    def test_case2(self):
        #"""A=1, B=500 -> valid (boundary)"""
        self.assertEqual(500, calc(1, 500))
    
    def test_case3(self):
        #"""A=2, B=500 -> valid"""
        self.assertEqual(1000, calc(2, 500))
    
    # ========== A is greater than 999 (Assume B=500) ==========
    def test_case4(self):
        #"""A=998, B=500 -> valid"""
        self.assertEqual(499000, calc(998, 500))
    
    def test_case5(self):
        #"""A=999, B=500 -> valid (boundary)"""
        self.assertEqual(499500, calc(999, 500))
    
    def test_case6(self):
        #"""A=1000, B=500 -> invalid"""
        self.assertEqual(-1, calc(1000, 500))
    
    # ========== B is less than 1 (Assume A=500) ==========
    def test_case7(self):
        #"""A=500, B=0 -> invalid"""
        self.assertEqual(-1, calc(500, 0))
    
    def test_case8(self):
        #"""A=500, B=1 -> valid (boundary)"""
        self.assertEqual(500, calc(500, 1))
    
    def test_case9(self):
        #"""A=500, B=2 -> valid"""
        self.assertEqual(1000, calc(500, 2))
    
    # ========== B is greater than 999 (Assume A=500) ==========
    def test_case10(self):
        #"""A=500, B=998 -> valid"""
        self.assertEqual(499000, calc(500, 998))
    
    def test_case11(self):
        #"""A=500, B=999 -> valid (boundary)"""
        self.assertEqual(499500, calc(500, 999))
    
    def test_case12(self):
        #"""A=500, B=1000 -> invalid"""
        self.assertEqual(-1, calc(500, 1000))
    
    # ========== A is not integer (Assume B=500) ==========
    def test_case13(self):
        #"""A=None, B=500 -> invalid"""
        self.assertEqual(-1, calc(None, 500))
    
    def test_case14(self):
        #"""A="", B=500 -> invalid"""
        self.assertEqual(-1, calc("", 500))
    
    def test_case15(self):
        #"""A=float, B=500 -> invalid"""
        self.assertEqual(-1, calc(1.5, 500))
    
    def test_case16(self):
        #"""A=String, B=500 -> invalid"""
        self.assertEqual(-1, calc("abc", 500))
    
    def test_case17(self):
        #"""A=undefined (None), B=500 -> invalid"""
        self.assertEqual(-1, calc(None, 500))
    
    # ========== B is not integer (Assume A=500) ==========
    def test_case18(self):
        #"""A=500, B=None -> invalid"""
        self.assertEqual(-1, calc(500, None))
    
    def test_case19(self):
        #"""A=500, B="" -> invalid"""
        self.assertEqual(-1, calc(500, ""))
    
    def test_case20(self):
        #"""A=500, B=float -> invalid"""
        self.assertEqual(-1, calc(500, 2.7))
    
    def test_case21(self):
        #"""A=500, B=String -> invalid"""
        self.assertEqual(-1, calc(500, "xyz"))
    
    def test_case22(self):
        #"""A=500, B=undefined (None) -> invalid"""
        self.assertEqual(-1, calc(500, None))
    
    # ========== Additional Edge Cases ==========
    def test_case23(self):
        #"""A=1, B=1 -> valid (both minimum)"""
        self.assertEqual(1, calc(1, 1))
    
    def test_case24(self):
        #"""A=999, B=999 -> valid (both maximum)"""
        self.assertEqual(998001, calc(999, 999))
    
    def test_case25(self):
        #"""A=-1, B=500 -> invalid (negative)"""
        self.assertEqual(-1, calc(-1, 500))
    
    def test_case26(self):
        #"""A=500, B=-1 -> invalid (negative)"""
        self.assertEqual(-1, calc(500, -1))
# ========== BOTH A and B are not integer ==========
    def test_case27(self):
        #"""A=None, B=None -> invalid (both null)"""
        self.assertEqual(-1, calc(None, None))
    
    def test_case28(self):
        #"""A="", B="" -> invalid (both empty string)"""
        self.assertEqual(-1, calc("", ""))
    
    def test_case29(self):
        #"""A=1.5, B=2.7 -> invalid (both float)"""
        self.assertEqual(-1, calc(1.5, 2.7))
    
    def test_case30(self):
        #"""A="abc", B="xyz" -> invalid (both string)"""
        self.assertEqual(-1, calc("abc", "xyz"))
    
    def test_case31(self):
        #"""A=None, B="" -> invalid (null and empty string)"""
        self.assertEqual(-1, calc(None, ""))
    
    def test_case32(self):
        #"""A=1.5, B=None -> invalid (float and null)"""
        self.assertEqual(-1, calc(1.5, None))
    
    def test_case33(self):
        #"""A="abc", B=2.7 -> invalid (string and float)"""
        self.assertEqual(-1, calc("abc", 2.7))
    
    def test_case34(self):
        #"""A="", B=3.14 -> invalid (empty string and float)"""
        self.assertEqual(-1, calc("", 3.14))
    
    def test_case35(self):
        #"""A=None, B="test" -> invalid (null and string)"""
        self.assertEqual(-1, calc(None, "test"))
    
    def test_case36(self):
        #"""A=[], B={} -> invalid (list and dict)"""
        self.assertEqual(-1, calc([], {}))
    
    def test_case37(self):
        #"""A=True, B=False -> invalid (both boolean)"""
        self.assertEqual(-1, calc(True, False))
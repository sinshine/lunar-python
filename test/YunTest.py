# -*- coding: utf-8 -*-
import unittest
from lunar_python import Solar, Lunar


class YunTest(unittest.TestCase):
    def test(self):
        solar = Solar.fromYmdHms(1981, 1, 29, 23, 37, 0)
        lunar = solar.getLunar()
        eight_char = lunar.getEightChar()
        yun = eight_char.getYun(0)
        self.assertEqual(8, yun.getStartYear(), "起运年数")
        self.assertEqual(0, yun.getStartMonth(), "起运月数")
        self.assertEqual(20, yun.getStartDay(), "起运天数")
        self.assertEqual("1989-02-18", yun.getStartSolar().toYmd(), "起运阳历")

    def test2(self):
        lunar = Lunar.fromYmdHms(2019, 12, 12, 11, 22, 0)
        eight_char = lunar.getEightChar()
        yun = eight_char.getYun(1)
        self.assertEqual(0, yun.getStartYear(), "起运年数")
        self.assertEqual(1, yun.getStartMonth(), "起运月数")
        self.assertEqual(0, yun.getStartDay(), "起运天数")
        self.assertEqual("2020-02-06", yun.getStartSolar().toYmd(), "起运阳历")

    def test3(self):
        solar = Solar.fromYmdHms(2020, 1, 6, 11, 22, 0)
        lunar = solar.getLunar()
        eight_char = lunar.getEightChar()
        yun = eight_char.getYun(1)
        self.assertEqual(0, yun.getStartYear(), "起运年数")
        self.assertEqual(1, yun.getStartMonth(), "起运月数")
        self.assertEqual(0, yun.getStartDay(), "起运天数")
        self.assertEqual("2020-02-06", yun.getStartSolar().toYmd(), "起运阳历")

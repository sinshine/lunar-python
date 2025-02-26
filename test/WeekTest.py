# -*- coding: utf-8 -*-
import unittest
from lunar_python import SolarWeek
from lunar_python.util import SolarUtil


class WeekTest(unittest.TestCase):
    def test(self):
        # 一周的开始从星期一开始计
        start = 1
        week = SolarWeek.fromYmd(2019, 5, 1, start)
        self.assertEqual("2019.5.1", week.toString())
        self.assertEqual("2019年5月第1周", week.toFullString())
        # 当月共几周
        self.assertEqual(5, SolarUtil.getWeeksOfMonth(week.getYear(), week.getMonth(), start))
        # 当周第一天
        self.assertEqual("2019-04-29", week.getFirstDay().toString())
        # 当周第一天（本月）
        self.assertEqual("2019-05-01", week.getFirstDayInMonth().toString())

    def test1(self):
        # 一周的开始从星期日开始计
        start = 0
        week = SolarWeek.fromYmd(2019, 5, 1, start)
        self.assertEqual("2019.5.1", week.toString())
        self.assertEqual("2019年5月第1周", week.toFullString())
        # 当月共几周
        self.assertEqual(5, SolarUtil.getWeeksOfMonth(week.getYear(), week.getMonth(), start))
        # 当周第一天
        self.assertEqual("2019-04-28", week.getFirstDay().toString())
        # 当周第一天（本月）
        self.assertEqual("2019-05-01", week.getFirstDayInMonth().toString())

    def test2(self):
        week = SolarWeek.fromYmd(2022, 5, 1, 0)
        self.assertEqual(1, week.getIndex())

    def test3(self):
        week = SolarWeek.fromYmd(2022, 5, 7, 0)
        self.assertEqual(1, week.getIndex())

    def test4(self):
        week = SolarWeek.fromYmd(2022, 5, 8, 0)
        self.assertEqual(2, week.getIndex())

    def test5(self):
        week = SolarWeek.fromYmd(2022, 5, 1, 1)
        self.assertEqual(1, week.getIndex())

    def test6(self):
        week = SolarWeek.fromYmd(2022, 5, 2, 1)
        self.assertEqual(2, week.getIndex())

    def test7(self):
        week = SolarWeek.fromYmd(2022, 5, 8, 1)
        self.assertEqual(2, week.getIndex())

    def test8(self):
        week = SolarWeek.fromYmd(2021, 11, 1, 0)
        self.assertEqual(1, week.getIndex())

    def test9(self):
        week = SolarWeek.fromYmd(2021, 11, 1, 1)
        self.assertEqual(1, week.getIndex())

    def test10(self):
        week = SolarWeek.fromYmd(2021, 5, 2, 2)
        self.assertEqual(1, week.getIndex())

    def test11(self):
        week = SolarWeek.fromYmd(2021, 5, 4, 2)
        self.assertEqual(2, week.getIndex())

    def test12(self):
        week = SolarWeek.fromYmd(2022, 3, 6, 0)
        self.assertEqual(11, week.getIndexInYear())

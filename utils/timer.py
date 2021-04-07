"""
获取当前日期: 如：2月4号 -> 2-04

Version: 0.1
Author: 黄华智
"""
from datetime import datetime
currentDay = datetime.now().day
extraDayZero = '' if currentDay > 9 else '0'
currentMonth = datetime.now().month
extraMonthZero = '' if currentMonth > 9 else '0'
currentYear = datetime.now().year

def getCurrentMonthAndDay():
  return str(currentMonth) + '-' + extraDayZero + str(currentDay)

def getCurrentYearAndMonth():
  return str(currentYear) + '-' + extraMonthZero + str(currentMonth)

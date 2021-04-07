"""
自动生成每日计划文件目录

Version: 0.1
Author: 黄华智
"""
import os
from utils.timer import getCurrentMonthAndDay, getCurrentYearAndMonth

targetPath = '/Users/lawrence.huang/Documents/scheme/' + getCurrentYearAndMonth()
targetFile = getCurrentMonthAndDay() + '.md'

if not os.path.exists(targetPath):
  os.mkdir(targetPath)

os.chdir(targetPath)
targetFilePath = targetPath + '/' + targetFile
if not os.path.exists(targetFilePath):
  f=open(targetFile, 'w')
  print('创建文件：', targetFilePath)
else:
  print('已存在文件：', targetFilePath)
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
为什么不使用线程：http://blog.csdn.net/echoutopia/article/details/51014722
除非能去除GIL（全局解释器锁）限制（如果真的能去除）……否则不要在 Python 编程中使用线程 from "Head First Python"
'''

from multiprocessing import Process
import RPi.GPIO as GPIO
import smart_ultrasonic_car as SUC


DELAY1 = 0.05  # 小车转向驱动电机时间
DELAY2 = 0.03  # 小车转向停止电机时间
FRONT_DISTANCE = 50  # 前置超声波安全距离
SIDE_DISTANCE = 35  # 左右两侧超声波安全距离
DELAY3 = 1  # SSH 输出时间间隔

if __name__ == '__main__':
    try:
        p1 = Process(target=SUC.display, args=(DELAY3,))
        p1.start()
        SUC.drive(DELAY1, DELAY2, FRONT_DISTANCE, SIDE_DISTANCE)

    except KeyboardInterrupt:
        GPIO.cleanup()

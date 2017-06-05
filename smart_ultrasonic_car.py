#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time
import logging
import motor as M
import RPi.GPIO as GPIO
import ultrasonic_x3 as UP


def drive(delay1=0.05, delay2=0.03, distance_f=50, distance_lr=35):  # 小车判断障碍
    while True:
        if (UP.front.probe() > distance_f
                and UP.right.probe() > distance_lr
                and UP.left.probe() > distance_lr):  # 前进
            M.motor.forward(95, 100)  # 修正偏航
        elif (UP.front.probe() <= distance_f
              and UP.right.probe() <= distance_lr
              and UP.left.probe() <= distance_lr):  # 障碍物类型 F
            M.motor.backward()
            time.sleep(0.5)
            M.motor.stop()
            if (UP.right.probe() <= distance_lr):
                M.motor.turn_left()
                time.sleep(delay1)
                M.motor.stop()
                time.sleep(delay2)
            elif (UP.left.probe() <= distance_lr):
                M.motor.turn_right()
                time.sleep(delay1)
                M.motor.stop()
                time.sleep(delay2)
            else:
                M.motor.turn_right()
                time.sleep(0.2)
                M.motor.stop()
                time.sleep(delay2)
        elif (UP.front.probe() <= distance_f
              and UP.right.probe() <= distance_lr):  # 障碍物类型 E
            M.motor.turn_left()
            time.sleep(delay1)
            M.motor.stop()
            time.sleep(delay2)
        elif (UP.front.probe() <= distance_f
              and UP.left.probe() <= distance_lr):  # 障碍物类型 D
            M.motor.turn_right()
            time.sleep(delay1)
            M.motor.stop()
            time.sleep(delay2)
        elif (UP.right.probe() <= distance_lr):  # 障碍物类型 C
            M.motor.forward(50, 100)
            time.sleep(delay1)
        elif (UP.left.probe() <= distance_lr):  # 障碍物类型 B
            M.motor.forward(100, 50)
            time.sleep(delay1)
        else:  # 障碍物类型 A
            M.motor.turn_right()
            time.sleep(delay1)
            M.motor.stop()
            time.sleep(delay2)


def display(delay):  # SSH 输出
    while True:
        full_line = ("Left_Distance: %.2f cm  Front_Distance: %.2f cm  Right_Distance: %.2f cm"
                     % (UP.left.probe(), UP.front.probe(), UP.right.probe()))
        print(full_line)
        time.sleep(delay)


if __name__ == '__main__':
    try:
        drive()

    except KeyboardInterrupt:
        GPIO.cleanup()

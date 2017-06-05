#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO


class ultrasonic(object):
    def __init__(self, direction_trigger, direction_echo, mode=GPIO.BCM):
        self.direction_trigger = direction_trigger
        self.direction_echo = direction_echo
        self.mode = mode
        # 设置 GPIO 口的模式
        GPIO.setmode(self.mode)
        # 定义 GPIO 输入、输出
        GPIO.setup(self.direction_trigger, GPIO.OUT)
        GPIO.setup(self.direction_echo, GPIO.IN)

    def probe(self):
        # 从 trigger 发射 10us 脉冲
        GPIO.output(self.direction_trigger, 1)
        time.sleep(0.00001)
        GPIO.output(self.direction_trigger, 0)
        start = time.time()

        # echo 接收脉冲
        while GPIO.input(self.direction_echo) == 0:
            start = time.time()

        while GPIO.input(self.direction_echo) == 1:
            stop = time.time()

        # 计算脉冲长度
        elapsed = stop - start
        # 距离 = 时间差 * 声速
        distance = elapsed * 34300
        # 需要的是单程距离，所以减半
        distance = distance / 2
        # 返回距离
        return distance


# 定义 GPIO
front_trig = 17
front_echo = 27
right_trig = 22
right_echo = 5
left_trig = 23
left_echo = 24
mode_ = GPIO.BCM
front = ultrasonic(front_trig, front_echo, mode_)
right = ultrasonic(right_trig, right_echo, mode_)
left = ultrasonic(left_trig, left_echo, mode_)

# 检查距离
try:
    if __name__ == '__main__':
        while True:
            print("Left_Distance: %.2f cm Front_Distance: %.2f cm Right_Distance: %.2f cm" % (
                left.probe(), front.probe(), right.probe()))
            time.sleep(0.1)

# 中断时重置GPIO
except KeyboardInterrupt:
    GPIO.cleanup()

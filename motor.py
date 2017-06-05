#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO


class directio(object):
    def __init__(self, IN1, IN2, IN3, IN4, ENA, ENB, MODE=GPIO.BCM):
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4
        self.ENA = ENA
        self.ENB = ENB
        self.MODE = MODE
        # 设置 GPIO 口的模式
        GPIO.setmode(self.MODE)
        # 设置 GPIO 口为输出
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        # PWM
        global PA
        global PB
        # 频率
        PA = GPIO.PWM(self.ENA, 1000)
        PB = GPIO.PWM(self.ENB, 1000)
        # 占空比，范围为 0 ~ 100
        PA.start(100)
        PB.start(100)

    # 停止
    def stop(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 1)
        GPIO.output(self.IN2, 1)
        GPIO.output(self.IN3, 1)
        GPIO.output(self.IN4, 1)

    # 右转
    def turn_right(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 1)
        GPIO.output(self.IN2, 0)
        GPIO.output(self.IN3, 1)
        GPIO.output(self.IN4, 0)

    # 左转
    def turn_left(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 0)
        GPIO.output(self.IN2, 1)
        GPIO.output(self.IN3, 0)
        GPIO.output(self.IN4, 1)

    # 前进
    def forward(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 1)
        GPIO.output(self.IN2, 0)
        GPIO.output(self.IN3, 0)
        GPIO.output(self.IN4, 1)

    # 后退
    def backward(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 0)
        GPIO.output(self.IN2, 1)
        GPIO.output(self.IN3, 1)
        GPIO.output(self.IN4, 0)


# 定义 GPIO 和模式
IN1_ = 6
IN2_ = 12
IN3_ = 13
IN4_ = 19
ENA_ = 26
ENB_ = 20
MODE_ = GPIO.BCM
motor = directio(IN1_, IN2_, IN3_, IN4_, ENA_, ENB_, MODE_)

# 测试
if __name__ == '__main__':
    try:
        motor.forward(50, 50)
        time.sleep(1)
        motor.backward()
        time.sleep(1)
        motor.turn_right()
        time.sleep(1)
        motor.stop()
        motor.turn_left()
        time.sleep(1)
        motor.stop()
        GPIO.cleanup()
        # 偏右
        motor.forward(100, 50)
        time.sleep(1)
        motor.stop()
        # 偏左
        motor.forward(50, 100)
        time.sleep(1)
        motor.stop()
        GPIO.cleanup()
    # 中断时重置GPIO
    except KeyboardInterrupt:
        GPIO.cleanup()
    # 结束时重置 GPIO
    finally:
        GPIO.cleanup()

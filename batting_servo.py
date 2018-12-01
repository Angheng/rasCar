from PCA9685 import Servo
from time import sleep

class Batting_Servo(object):
    channel = 1

    def __init__(self, bus_number=1):
        self.wheel = Servo.Servo(self.channel, bus_number=bus_number, offset=10)
        self.wheel.setup()
        self.set_position()

    def set_position(self, angle=-150):
        self.wheel.write(angle)

    def batting(self, angle=270):
        self.wheel.write(angle)


if __name__ == "__main__":
    bat = Batting_Servo()

    import RPi.GPIO as GPIO

    btnPin = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btnPin, GPIO.In)

    before_input = 0
    while True:
        button_input = GPIO.input(btnPin)

        if button_input is 1:
            bat.batting()
            bat.set_position()
        if button_input != before_input:
            print(button_input)
        before_input = button_input

from PCA9685 import Servo


class Batting_Servo(object):
    channel = 1

    def __init__(self, bus_number=1):
        self.wheel = Servo.Servo(self._channel, bus_number=bus_number, offset=10)
        self.wheel.setup()

    def test(self, angle=10):
        self.wheel.write(angle)


if __name__ == "__main__":
    bat = Batting_Servo()
    bat.test()

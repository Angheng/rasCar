from TCS34725 import TCS34725_RGB
from time import sleep


class Colour_Detector(object):
    def __init__(self):
        self.colour_detector = TCS34725_RGB.TCS34725()

        self.red_range = [[100, 500], [0, 100], [0, 100]]
        self.green_range = [[0, 100], [100, 500], [0, 100]]
        self.blue_range = [[0, 100], [0, 100], [100, 500]]

    def is_red(self):
        return self.red_range[0][0] <= self.get_red() <= self.red_range[0][1] \
               and self.red_range[1][0] <= self.get_green() <= self.red_range[1][1] \
               and self.red_range[2][0] <= self.get_blue() <= self.red_range[2][1]

    def is_green(self):
        return self.green_range[0][0] <= self.get_red() <= self.green_range[0][1] \
               and self.green_range[1][0] <= self.get_green() <= self.green_range[1][1] \
               and self.green_range[2][0] <= self.get_blue() <= self.green_range[2][1]

    def is_blue(self):
        return self.blue_range[0][0] <= self.get_red() <= self.blue_range[0][1] \
               and self.blue_range[1][0] <= self.get_green() <= self.blue_range[1][1] \
               and self.blue_range[2][0] <= self.get_blue() <= self.blue_range[2][1]

    def get_red(self):
        return self.colour_detector.get_raw_data()[0]

    def get_green(self):
        return self.colour_detector.get_raw_data()[1]

    def get_blue(self):
        return self.colour_detector.get_raw_data()[2]

    def get_clear(self):
        return self.colour_detector.get_raw_data()[3]


if __name__ == "__main__":
    cd = Colour_Detector()

    try:
        while(True):
            print(cd.get_red(), cd.get_green(),cd.get_blue())

            if cd.is_red():
                print('red')
            elif cd.is_blue():
                print('blue')
            elif cd.is_green():
                print('green')
            else:
                print('fuck')

            sleep(1)
    except KeyboardInterrupt:
        exit()

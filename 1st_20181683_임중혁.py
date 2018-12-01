#########################################################################
# Date: 2018/08/09
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################


# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time

# =======================================================================
# import ALL method in the SEN040134 Tracking Module
# =======================================================================
from SEN040134 import SEN040134_Tracking as Tracking_Sensor

# =======================================================================
# import ALL method in the SR02 Ultrasonic Module
# =======================================================================
from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor

# =======================================================================
# import ALL method in the rear/front Motor Module
# =======================================================================
import rear_wheels
import front_wheels

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)


class Car(object):

    def __init__(self):
        self.moduleInitialize()

    def drive_parking(self):
        # front wheels center allignment
        self.direction.turn_straight()

        # power down both wheels
        self.drive.stop()
        self.drive.power_down()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def assignment_main(self):
        # set real wheel =====================
        self.drive.ready()

        while self.distance.get_distance() < 10 :
            pass
        
        current_time = time.time() # set start time
        self.drive.forward_with_speed(100)
        
        while(self.distance.get_distance() > 10) : # go forward while distance that
            pass                                                    # between rascar & block lower than 10cm

        # encounter block action ==============
        back_time = time.time() - current_time # backward during this variable
        self.drive.stop()
        
        self.drive.backward_with_speed(100)
        time.sleep(back_time + 0.2)
        
        self.drive.forward_with_speed(100) # to backward inertia
        time.sleep(0.05)
        
        self.drive.stop()
        self.drive_parking()
        

    def moduleInitialize(self):
        try:
            # ================================================================
            # ULTRASONIC MODULE DRIVER INITIALIZE
            # ================================================================
            self.distance = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)

            # ================================================================
            # TRACKING MODULE DRIVER INITIALIZE
            # ================================================================
            self.line= Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])

            # ================================================================
            # FRONT WHEEL DRIVER SETUP
            # ================================================================
            self.direction = front_wheels.Front_Wheels(db='config')
            self.direction.ready()

            # ================================================================
            # REAR WHEEL DRIVER SETUP
            # ================================================================
            self.drive = rear_wheels.Rear_Wheels(db='config')
            self.drive.ready()

            # ================================================================
            # SET LIMIT OF TURNING DEGREE
            # ===============================================================
            self.direction.turning_max = 35

            # ================================================================
            # SET FRONT WHEEL CENTOR ALLIGNMENT
            # ================================================================
            self.direction.turn_straight()

        except:
            print("MODULE INITIALIZE ERROR")
            print("CONTACT TO Kookmin Univ. Teaching Assistant")


if __name__ == "__main__":
    try:
        car = Car()
        car.assignment_main()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        car.drive_parking()

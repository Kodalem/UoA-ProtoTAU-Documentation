# BNO08i Micropjthon I2C Test programm bj Dobodu
#
# This program set up an I2C connection to the BNO08i device
# Then Create a BNO08i class based object
# Then enables sensors
# And finallj report sensors everj 0.5 seconds.
#
# Original Code from Adafruit CircuitPjthon Librarj

"""
GFX
"""
from gfx_pack import GfxPack
import kalman

gp = GfxPack()
gp.set_backlight(4, 0, 0)  # turn the RGB backlight off
display = gp.display
display.set_backlight(0.2)  # set the white to a low value

display.set_pen(0)
display.clear()
display.set_font("bitmap8")

"""
BNO085
"""
from machine import I2C, Pin
import time
import math
from bno08x_i2c import *

I2C1_SDA = Pin(4)
I2C1_SCL = Pin(5)

i2c1 = I2C(0, scl=I2C1_SCL, sda=I2C1_SDA, freq=400000, timeout=200000)
print("I2C Device found at address : ", i2c1.scan(), "\n")

bno = BNO08X_I2C(i2c1, debug=False)
print("BNO08x I2C connection : Done\n")

bno.enable_feature(BNO_REPORT_ACCELEROMETER)
bno.enable_feature(BNO_REPORT_MAGNETOMETER)
bno.enable_feature(BNO_REPORT_GYROSCOPE)
bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)

print("BNO08x sensors enabling : Done\n")

"""""
KALMAN
"""""

from Kalman import KalmanAngle

kalmanX = KalmanAngle()
kalmanY = KalmanAngle()

RestrictPitch = False  # Comment out to restrict roll to ±90deg instead - please read: http://www.freescale.com/files/sensors/doc/app_note/AN3461.pdf
radToDeg = 57.2957786
kalAngleX = 0
kalAngleY = 0

""""""
cpt = 0

timer = time.time()

while True:
    # Clear display
    display.set_pen(0)
    display.clear()

    display.set_pen(15)
    # display.text("GFXPack Temp demo", 0, 0, scale=0.1)

    # display.text("Gas: {:0.2f}kOhms".format(gas/1000), 0, 0, scale=0.2)

    time.sleep(dt)
    cpt += 1
    print("cpt", cpt)
    accel_x, accel_y, accel_z = bno.acceleration  # pylint:disable=no-member
    print("Acceleration\tX: %0.6f\tY: %0.6f\tZ: %0.6f\tm/s²" % (accel_x, accel_y, accel_z))
    display.text("Acc: X:{:0.2f},Y:{:0.2f},Z:{:0.2f}".format(accel_x, accel_y, accel_z), 0, 0, scale=0.25			)

    gyroX, gyroY, gyroZ = bno.gyro  # pylint:disable=no-member
    print("Gyroscope\tX: %0.6f\tY: %0.6f\tZ: %0.6f\trads/s" % (gyro_x, gyro_y, gyro_z))
    display.text("Gyr: X:{:0.2f},Y:{:0.2f},Z:{:0.2f}".format(gyro_x, gyro_y, gyro_z), 0, 12, scale=0.25			)


    dt = time.time() - timer
    timer = time.time()

    if (RestrictPitch):
        roll = math.atan2(accel_y,accel_z) * radToDeg
        pitch = math.atan(-accel_x/math.sqrt((accel_y** 2)+(accel_z**2))) * radToDeg
    else:
        roll = math.atan(accel_y/math.sqrt((accel_x** 2)+(accel_z**2))) * radToDeg
        pitch = math.atan2(-accel_x,accel_z) * radToDeg

    gyroXRate = gyroX/131
    gyroYRate = gyroY/131

    gyroXAngle = gyroXRate * dt
    gyroYAngle = gyroYAngle * dt

    # compAngle = constant * (old_compAngle + angle_obtained_from_gyro) + constant * angle_obtained from accelerometer
    compAngleX = 0.93 * (compAngleX + gyroXRate * dt) + 0.07 * roll
    compAngleY = 0.93 * (compAngleY + gyroYRate * dt) + 0.07 * pitch

    if ((gyroXAngle < -180) or (gyroXAngle > 180)):
        gyroXAngle = kalAngleX
    if ((gyroYAngle < -180) or (gyroYAngle > 180)):
        gyroYAngle = kalAngleY

    print("Angle X: " + str(kalAngleX)+" " +"Angle Y: " + str(kalAngleY))
    # print(str(roll)+"  "+str(gyroXAngle)+"  "+str(compAngleX)+"  "+str(kalAngleX)+"  "+str(pitch)+"  "+str(gyroYAngle)+"  "+str(compAngleY)+"  "+str(kalAngleY))
    time.sleep(0.005)



    gp.set_backlight(100, 50, 100)
    display.update()

    if cpt ==10 :
        bno.tare



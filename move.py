import pid
import Adafruit_PCA9685
import time
from mpu6050 import mpu6050

# moving direction of legs
leftside_direction = 1
rightside_direction = 0
leftside_height = 1
rightside_height = 0

# moving height range of legs
height_change = 30

# moving direction of camera frame
up_down_direction = 1
left_right_direction = 1

# some limit of camera frame
Left_Right_input = 300
Up_Down_input = 300
Left_Right_Max = 500
Left_Right_Min = 100
Up_Down_Max = 500
Up_Down_Min = 270
look_wiggle = 30
move_stu = 1

# steady function configuration
steady_range_Min = -40
steady_range_Max = 130
range_Mid = (steady_range_Min+steady_range_Max)/2
X_fix_output = range_Mid
Y_fix_output = range_Mid
steady_X_set = 73
"""
change these two variable to adjuest the steady status.
	 (X+)
	  |
(Y+)<-+->(Y-)
	  |
	 (X-)
Example: If you want the forhead of the robot to point down,
        you need to increase the value target_X.
"""
target_X = 0
target_Y = 0

# PID configuration and setup
#! or Kalman Filter?
P = 5
I = 0.01
D = 0
x_pid = pid.PID()
x_pid.setKp(P)
x_pid.setKi(I)
x_pid.setKd(D)
y_pid = pid.PID()
y_pid.setKp(P)
y_pid.setKi(I)
y_pid.setKd(D)

# pwm controller
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

pwms = []
for _ in range(16):
    pwms.append(300)
def init_pwm_all():
    '''initial all pwm signal to middle position
    '''
    for i in range(16):
        pwm.set_pwm(i, 0, pwms[i])

sensor = mpu6050(0x68)
def test_mpu_data():
    '''show the accelerometer data from MPU
    '''
    while 1:
        accelerometer_data = sensor.get_accel_data()
        x = accelerometer_data['x']
        y = accelerometer_data['y']
        z = accelerometer_data['z']
        print(f'X:{x} Y:{y} Z:{z}')
        time.sleep(0.3)


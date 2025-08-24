import numpy as np
import math

l1 = 2
l2 = 3

theta1 = float(input("please input theta1:")) * math.pi / 180
theta2 = float(input("please input theta2:")) * math.pi / 180

sin1 = math.sin(theta1)
cos1 = math.cos(theta1)

cos2 = math.cos(theta2)
sin2 = math.sin(theta2)

T01 = np.array([
    [cos1, -sin1, 0, l1 * cos1],
    [sin1, cos1, 0, l1 * sin1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
T12 = np.array([
    [cos2, -sin2, 0, l2 * cos2],
    [sin2, cos2, 0, l2 * sin2],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])


T02 = T01 @ T12


x = T02[0, 3]
y = T02[1, 3]
z = T02[2, 3] 

pos = [x, y, z]


print(f"the position of the end of arm robot is [{pos[0]:.3f}, {pos[1]:.3f}, {pos[2]:.3f}]")
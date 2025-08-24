import numpy as np
import math
import csv

l1=2
l2=3
NUM_SAMPLES = 10000


with open('robot_dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['theta1', 'theta2', 'x', 'y'])
    print("generating the samples...")
    for i in range(NUM_SAMPLES):

        theta1 = np.random.uniform(-math.pi, math.pi) 
        theta2 = np.random.uniform(-math.pi, math.pi)

        sin1=math.sin(theta1)
        cos1=math.cos(theta1)

        cos2=math.cos(theta2)
        sin2=math.sin(theta2)

        T01=np.array([
            [cos1,-sin1,0,l1*cos1],
            [sin1,cos1,0,l1*sin1],
            [0,0,1,0],
            [0,0,0,1]
        ])
        T12=np.array([
            [cos2,-sin2,0,l2*cos2],
            [sin2,cos2,0,l2*sin2],
            [0,0,1,0],
            [0   ,0   ,0,  1     ]
        ])
        T02=T01@T12
        x=T02[0,3]
        y=T02[1,3]
        z=T02[2,3]
    
        writer.writerow([theta1, theta2, x, y])


print("Done.")

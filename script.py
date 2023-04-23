import numpy as np


Ta = float(input("Enter total sleep duration: "))
Tn = float(input("Enter total sleep needed: "))
Tsc = float(input("Enter the time before last use of screen (in minutes): "))
T2 = float(input("Enter the time of bed preperation (in minutes): "))
T3 = float(input("Enter the time of nap (int minutes): "))
Tcaf = float(input("Enter the time before last intake of caffeine (in hours): "))
A = float(input("Enter activeness of the day: "))
E = float(input("Enter sleep-friendliness of the environment: "))
n = int(input("Enter the number of consistent days: "))
Cs = np.array([0, -0.5, 1.2, 0.5, -1/12, -2, -1/125, -1/75])

y = 60.0
y += Cs[1] * np.square(Ta - Tn)
print("Contribution of duration is {}".format(Cs[1] * np.square(Ta - Tn)))
y += Cs[2] * min(Ta, 9) * A
print("Contribution of Activeness is {}".format(Cs[2] * min(Ta, 9) * A))
y += Cs[3] * Ta * E
print("Contribution of Environment is {}".format(Cs[3] * Ta * E))
y += Cs[4] * (60 - Tsc)
print("Contribution of Screen time is {}".format(Cs[4] * (60 - Tsc)))
y += Cs[5] * (8 - Tcaf)
print("Contribution of Caffeine is {}".format(Cs[5] * (8 - Tcaf)))
y += Cs[6] * (np.square(T3 - 15) - 225)
print("Contribution of Nap is {}".format(Cs[6] * (np.square(T3 - 15) - 225)))
y += Cs[7] * (T2 - 5) * (T2 - 45)
print("Contribution of Preparation is {}".format(Cs[7] * (T2 - 5) * (T2 - 45)))
y += np.power(1.05, n)
print("Contribution of Consistency is {}".format(np.power(1.05, n)))
print(y)

import math
import random
import time

x1min = 10
x1max = 50
x2min = -20
x2max = 60
ymax = (30 - 115) * 10
ymin = (20 - 115) * 10
m = None
while True:
    try:
        m = int(input("Введіть m: "))
    except ValueError:
        continue
    else:
        break

x1l = [-1, 1, -1]
x2l = [-1, -1, 1]

y1l = [random.randint(ymin, ymax) for _ in range(5)]
y2l = [random.randint(ymin, ymax) for _ in range(5)]
y3l = [random.randint(ymin, ymax) for _ in range(5)]

star_time = time.perf_counter()

y1 = sum(y1l) / 5
y2 = sum(y2l) / 5
y3 = sum(y3l) / 5

sigma1 = sum([(y1l[i] - y1) ** 2 for i in range(5)]) / m
sigma2 = sum([(y2l[i] - y2) ** 2 for i in range(5)]) / m
sigma3 = sum([(y3l[i] - y3) ** 2 for i in range(5)]) / m


sigma0 = math.sqrt((2*(2*m - 2)) / (m*(m - 4)))

if sigma1 > sigma2:
    Fuv1 = sigma1 / sigma2
else:
    Fuv1 = sigma2 / sigma1

if sigma3 > sigma1:
    Fuv2 = sigma3 / sigma1
else:
    Fuv2 = sigma1 / sigma3

if sigma3 > sigma2:
    Fuv3 = sigma3 / sigma2
else:
    Fuv3 = sigma2 / sigma3

Ouv1 = ((m - 2) / m) * Fuv1
Ouv2 = ((m - 2) / m) * Fuv2
Ouv3 = ((m - 2) / m) * Fuv3

Ruv1 = math.fabs(Ouv1 - 1) / sigma0
Ruv2 = math.fabs(Ouv2 - 1) / sigma0
Ruv3 = math.fabs(Ouv3 - 1) / sigma0

p = [1.73, 2.16, 2.43, 2.62, 2.75, 2.9, 3.08]

if m <= 4:
    Rk = p[0]

elif 4 < m <= 6:
    Rk = p[1]

elif 6 < m <= 8:
    Rk = p[2]

elif 8 < m <= 10:
    Rk = p[3]

elif 10 < m <= 12:
    Rk = p[4]

elif 12 < m <= 15:
    Rk = p[5]
else:
    Rk = p[6]

if Ruv1 < Rk and Ruv2 < Rk and Ruv3 < Rk:
    print("Дисперсія однорідна")

print("Час перевірки за критерієм Романовського: {:.7f} c".format(time.perf_counter() - star_time))

mx1 = sum([x1l[i] for i in range(3)]) / 3
mx2 = sum([x2l[i] for i in range(3)]) / 3
a1 = sum([x1l[i] ** 2 for i in range(3)]) / 3
a2 = sum([x1l[i] * x2l[i] for i in range(3)]) / 3
a3 = sum([x2l[i] ** 2 for i in range(3)]) / 3

my = (y1 + y2 + y3) / 3

a11 = (x1l[0] * y1 + x1l[1] * y2 + x1l[2] * y3) / 3
a22 = (x2l[0] * y1 + x2l[1] * y2 + x2l[2] * y3) / 3

b0 = (my*a1*a3 + a11*a2*mx2 + mx1*a2*a22 - mx2*a1*a22 - a2*a2*my - a11*mx1*a3) / (
            a1*a3 + a2*mx1*mx2 + mx1*mx2*a2 - mx2*a1*mx2 - a2*a2 - mx1*mx1*a3)

b1 = (a11*a3 + mx1*a22*mx2 + my*a2*mx2 - mx2*mx2*a11 - mx1*my*a3 - a22*a2) / (
        a1*a3 + a2*mx1*mx2 + mx1*mx2*a2 - mx2*a1*mx2 - a2*a2 - mx1*mx1*a3)

b2 = (a1*a22 + mx1*a2*my + mx1*a11*mx2 - my*a1*mx2 - mx1*mx1*a22 - a2*a11) / (
            a1*a3 + a2*mx1*mx2 + mx1*mx2*a2 - mx2*a1*mx2 - a2*a2 - mx1*mx1*a3)


dx1 = math.fabs(x1max - x1min) / 2
dx2 = math.fabs(x2max - x2min) / 2
x10 = (x1max + x1min) / 2
x20 = (x2max + x2min) / 2

a0 = b0 - b1 * x10 / dx1 - b2 * x20 / dx2
a1 = b1 / dx1
a2 = b2 / dx2

print("y = {:.4} + {:.4}*x1 + {:.4}*x2".format(b0, b1, b2))
print("y = {:.4} + {:.4}*x1 + {:.4}*x2".format(a0, a1, a2))

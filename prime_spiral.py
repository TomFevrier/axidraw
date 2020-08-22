from pyaxidraw import axidraw
from math import sqrt, cos, sin

def is_prime(nb):
	if nb < 2:
		return False
	for div in range(2, int(sqrt(nb)) + 1):
		if nb % div == 0:
			return False
	return True

ad = axidraw.AxiDraw()
ad.interactive()
ad.options.units = 2
ad.options.pen_pos_up = 80
ad.connect()


for i in range(1, 400):
	if is_prime(i):
		print(i * cos(i), i * sin(i))
		ad.moveto(100 + 0.1 * i * cos(i), 100 + 0.1 * i * sin(i))
		ad.pendown()
		ad.penup()

ad.moveto(0, 0)
ad.disconnect()

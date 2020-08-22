from pyaxidraw import axidraw
import sys
import random

nb_cols = int(sys.argv[1]) if len(sys.argv) > 1 else 10
nb_rows = int(sys.argv[2]) if len(sys.argv) > 2 else nb_cols
step = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5

ad = axidraw.AxiDraw()
ad.interactive()
ad.options.pen_pos_up = 80
ad.options.units = 1
ad.connect()

for i in range(nb_rows):
	for j in range(nb_cols):
		ad.moveto(5 + j * step, 5 + i * step)
		if random.uniform(0, 1) > 0.5:
			ad.line(step, step)
		else:
			ad.move(step, 0)
			ad.line(-step, step)

ad.moveto(0, 0)
ad.disconnect()

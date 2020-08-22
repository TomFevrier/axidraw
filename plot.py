from pyaxidraw import axidraw
import sys

ad = axidraw.AxiDraw()
ad.plot_setup(sys.argv[1])
ad.plot_run()

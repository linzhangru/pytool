#!/usr/bin/python
import xlrd
from xlwt import *


import plotly.offline as py
from   plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt




filename="output.xlsx"
book = xlrd.open_workbook(filename)

try:
    sh = book.sheet_by_name("Sheet1")
except:
    print "Error!"

nrows = sh.nrows
#book = Workbook(encoding='utf-8')
#sheet = book.add_sheet('Sheet1')
#for i in range(1,nrows):
#    print sh.row_values(i)
Native      = sh.col_values(1)[2:]
System      = sh.col_values(2)[2:]
Persist     = sh.col_values(3)[2:]
Foreground  = sh.col_values(17)[2:]
Visible     = sh.col_values(18)[2:]
Perceptible = sh.col_values(19)[2:]
AService    = sh.col_values(20)[2:]
Home        = sh.col_values(21)[2:]
BService    = sh.col_values(22)[2:]
Cached      = sh.col_values(23)[2:]

ZRAM        = sh.col_values(49)[2:]



track_native = go.Scatter(
    x=np.arange(1, len(Native)),
    y=Native,
    name='Native',
    line = dict(
        color=('rgb(22,96,167)'),
        width=2,
    ),
)



data=[track_native,]



layout = dict(title = "OOM_ADJ",
              showlegend = True,
              xaxis = dict(title="index",
                           showgrid=True,
                           showticklabels=True,
                           dtick=len(Native)/200),
              
              yaxis = dict(title="Native (MB)",
                           showgrid=True,
                           range=[0,2000],
                           showticklabels=True,
                           dtick=100,
                           tickwidth=2,
                           ticklen=8)
)

fig=dict(data=data, layout=layout)
#print "tagA"
py.plot(fig, filename="Native.html")
#print "tagB"
plt.ylim([0,2000])
plt.plot(fig)


#print dir(sh)

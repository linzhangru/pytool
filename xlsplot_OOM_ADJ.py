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

track_System = go.Scatter(
    x=np.arange(1,len(System)),
    y=System,
    name='System',
    line = dict(
        color=('rgb(96,22,167)'),
        width=2,
    ),
)

track_Persist = go.Scatter(
    x=np.arange(1,len(Persist)),
    y=Persist,
    name='Persist',
    line = dict(
        color=('rgb(22,167,96)'),
        width=2,
    ),
)

track_Foreground = go.Scatter(
    x=np.arange(1,len(Foreground)),
    y=Foreground,
    name='Foreground',
    line = dict(
        color=('rgb(46,88,21)'),
        width=2,
    ),
)

track_Visible = go.Scatter(
    x=np.arange(1,len(Visible)),
    y=Visible,
    name='Visible',
    line = dict(
        color=('rgb(88,21,46)'),
        width=2,
    ),
)

track_Perceptible = go.Scatter(
    x=np.arange(1,len(Perceptible)),
    y=Perceptible,
    name='Perceptible',
    line = dict(
        color=('rgb(21,46,88)'),
        width=2,
    ),
)

track_AService = go.Scatter(
    x=np.arange(1,len(AService)),
    y=AService,
    name='AService',
    line = dict(
        color=('rgb(10,60,123)'),
        width=2,
    ),
)


track_Home = go.Scatter(
    x=np.arange(1,len(Home)),
    y=Home,
    name='Home',
    line = dict(
        color=('rgb(60,123,10)'),
        width=2,
    ),
)


track_BService = go.Scatter(
    x=np.arange(1,len(BService)),
    y=BService,
    name='BService',
    line = dict(
        color=('rgb(123,10,60)'),
        width=2,
    ),
)


track_Cached = go.Scatter(
    x=np.arange(1,len(Cached)),
    y=Cached,
    name='Cached',
    line = dict(
        color=('rgb(123,10,10)'),
        width=2,
    ),
)

track_ZRAM = go.Scatter(
    x=np.arange(1,len(ZRAM)),
    y=ZRAM,
    name='ZRAM',
    line = dict(
        color=('rgb(10,250,10)'),
        width=2,
    ),
)


data=[track_native,
      track_System,
      track_Persist,
      track_Foreground,
      track_Visible,
      track_Perceptible,
      track_AService,
      track_Home,
      track_BService,
      track_Cached,
      track_ZRAM]



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

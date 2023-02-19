from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import context
import csv

def index(request):
    context = {'name':'mainapp'}
    file = open("Downlaods/csv.csv")
    csvreader = csv.reader(file)
    rows = []
    d = dict()
    for row in csvreader:
       rows.append(row)
    for r in rows:
       d.update({r[0]:r[1]})
       print(r[0]) 

    print(d["Prescot"])
    file.close()
    return render(request, 'home.html',context)

from datetime import datetime
#            BANKNIFTY,DATE,TIME,OPEN,HIGH,LOW,CLOSE,VOLUME
quotes = ['(NIFTY_F1',datetime(2012,01,02,09,16),4638.00,4638.00,4616.05,4626.20,212950),
          ('NIFTY_F1',datetime(2012,01,02,09,17),4626.00,4628.00,4622.30,4625.30,107550),
          ...
         ]


from matplotlib.dates import date2num

quotes = [(date2num(item[0]),) + item[1:] for item in quotes]




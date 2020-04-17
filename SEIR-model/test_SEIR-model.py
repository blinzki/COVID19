import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *
from datetime import datetime, timedelta
import math

# Pablo Eduardo Romero Oestreicher
# ing.pabloeromero@gmail.com
# 03/2020

# The SEIR model differential equations.
def deriv(y, t, N, beta, gamma, sigma):

    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I /N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

def predict(chart_number, date_test):
   
   # Read data file 
   f = open("../README.md","r")
   line = f.readline()
   while line != "":
      data = f.readline()
      print(data)
   f.close()  

   # Model parameters
   N = 992323
   beta = 1.38
   gamma = 1./5
   sigma = 1./7
   b1 = beta

   # Initial conditions.
   I0, R0, E0 = 1, 0, 0
   S0 = N - I0 - R0 - E0 

   y_axis = 1000000
   x_axis = 180 

   if chart_number == 1:
      y_axis = 100 
      x_axis = 35 
    
   # Grid of time
   t = np.linspace(0, x_axis, x_axis)
 
   # Initial conditions vector
   y0 = S0, E0, I0, R0

   # Real data Gran Rosario 
   #x = [1, 1, 1, 1, 1, 2, 2, 2, 2, 8, 8, 11, 13, 21, 24, 33, 48, 55, 62, 65, 72,,,,,,,93, 94, 94, 95]
 
   # Real data Municipo de Rosario
   x = [0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 8, 8, 12, 20, 23, 33, 44, 51, 56, 58, 65, 68, 73, 76, 77, 79, 79, 80, 81, 84, 85, 85, 86]

   # Integrate the SEIR equations over period 1  

   ret = odeint(deriv, y0, t, args=(N, beta, gamma, sigma))
   S1, E1, I1, R1 = ret.T

   # Finding beta at the last point

   # beta from 0.8 to 1.2 + delta in 20 steps
   step = 20000 
   delta = 3 
   beta = 0.4

   l = len(x)
   for i in range(step):
      b =  beta + delta  * (i + 1) / step
      ret = odeint(deriv, y0, t, args=(N, b, gamma, sigma))
      S2, E2, I2, R2 = ret.T
      #if x[l-1] > I2[l]:
      #print(l-1, I2[l-1], x[l-1], sep='\t')    	
      if I2[l-1] >= x[l-1]:
         beta = b
         break 
   b2 = beta

   # Print predictions
   for i in range(x_axis):
      initd = '2020-03-14'
      date = datetime.strptime(initd, "%Y-%m-%d")
      d = date + timedelta(days=i)
      #print(i, str(d.strftime("%Y-%m-%d")), math.floor(I1[i]), sep='\t')

   # R0 interpolation
   ro1=str(round(b1/gamma, 2))
   ro2=str(round(b2/gamma, 2))

   # Plot the data curves: S(t), E(t), I(t) and R(t)
   fig = plt.figure(facecolor='w', figsize=(12, 6))
   ax = fig.add_subplot(111,  axisbelow=True)
   ax.set_title('Rosario SEIR Model COVID-19')
   ax.plot( S2, 'b', alpha=0.5, lw=1, label='Susceptible')
   ax.plot( E2, 'y', alpha=0.5, lw=1, label='Exposed')
   ax.plot( I1, 'r', alpha=0.5, lw=2, label='Infected without containment')
   ax.plot( I2, 'r', alpha=0.5, lw=2, label='Infected with containment')
   ax.plot( R2, 'g', alpha=0.5, lw=1, label='Recovered with immunity')
   ax.plot( x, '-', label='Confirmed case')
   if chart_number == 1: ax.plot( I2, 'o', color='red',label='Free containment')

   ax.annotate("$R1_{0}$="+ ro1, xy=(0.9,0.99),xycoords='axes fraction', fontsize=10)
   ax.annotate("$R2_{0}$="+ ro2, xy=(0.9,0.9),xycoords='axes fraction', fontsize=10)
   ax.set_xlabel('Time/days')
   ax.set_ylabel('Number')
   ax.set_ylim(0,y_axis)
   ax.yaxis.set_tick_params(length=0)
   ax.xaxis.set_tick_params(length=1)
   ax.grid(b=True, which='major', c='w', lw=2, ls='-')
   legend = ax.legend()
   legend.get_frame().set_alpha(0.5)

   for spine in ('top', 'right', 'bottom', 'left'):
       ax.spines[spine].set_visible(False)
  
   if chart_number == 1: plt.savefig('img/seir-interpolation-' + date_test + '.png') 
   if chart_number == 2: plt.savefig('img/seir-covid19-' + date_test  + '.png')

   # write data file 
   #if chart_number == 1:
   #   f = open("../README.md","w")       
   #   f.close()
 
   plt.show()


def test_interpolation():
   __test__ = False
   predict(1, "15-04-20")
   predict(2, "15-04-20")

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *
from datetime import datetime, timedelta
import math

# Pablo Eduardo Romero Oestreicher
# ing.pabloeromero@gmail.com
# 03/2020

# Chart config
y_axis = 1000000
x_axis = 120

# Model parameters
N = 992323
beta = 1.3
gamma = 1./5
sigma = 1./7

# Initial conditions.
I0, R0, E0 = 1, 0, 0
S0 = N - I0 - R0 - E0

# Grid of time
t = np.linspace(0, x_axis, x_axis)

# The SEIR model differential equations.
def deriv(y, t, N, beta, gamma, sigma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I /N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, E0, I0, R0

# Real data Gran Rosario 
#x = [1, 1, 1, 1, 1, 2, 2, 2, 2, 8, 8, 11, 13, 21, 24, 33, 48, 55, 62, 65, 72]

# Real data Municipo de Rosario
x = [1, 1, 1, 1, 2, 2, 2, 2, 3, 8, 8, 12, 20, 23, 33, 44, 51, 56, 58, 65, 68]


# Integrate the SEIR equations over period 1  
beta = 1.2
ret = odeint(deriv, y0, t, args=(N, beta, gamma, sigma))
S1, E1, I1, R1 = ret.T

# Finding beta at the last point

# beta from 1.2 to 2.2 in 20 steps
step = 20
for i in range(step):
   beta =  beta + step * beta / i
   print (beta)   

print (S1)

# Print predictions
for i in range(x_axis):
    initd = '2020-03-14'
    date = datetime.strptime(initd, "%Y-%m-%d")
    d = date + timedelta(days=i)
    print(i,str(d.strftime("%Y-%m-%d")), math.floor(I1[i]), sep='\t')

# Plot the data curves: S(t), E(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111,  axisbelow=True)
ax.set_title('Rosario SEIR Model COVID-19')
ax.plot(t, S1, 'b', alpha=0.5, lw=1, label='Susceptible')
ax.plot(t, E1, 'y', alpha=0.5, lw=1, label='Exposed')
ax.plot(t, I1, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R1, 'g', alpha=0.5, lw=1, label='Recovered with immunity')
ax.plot(x, 'o', label='Confirmed cases')
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

plt.show()

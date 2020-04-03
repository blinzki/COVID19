import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

# SEIR Model 
# Pablo Eduardo Romero Oestreicher
# ing.pabloeromero@gmail.com
# 03/2020

# Chart config
y_axis = 1200000
x_axis = 360

# Model parameters 
N = 992323 
beta = 1.42
gamma = 1./5
sigma = 1./7

# Initial number of infected and recovered individuals, I0 and R0.
I0, R0, E0 = 1, 0, 0

# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0 - E0

# A grid of time points (in days)
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

# Real data 
x = [1, 1, 1, 1, 1, 2, 2, 2, 2, 8, 8, 11, 13, 21, 24, 33, 48, 55, 62, 65]

# Integrate the SEIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, sigma))
S, E, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111,  axisbelow=True)
ax.plot(t, S, 'b', alpha=0.5, lw=1, label='Susceptible')
ax.plot(t, E, 'y', alpha=0.5, lw=1, label='Exposed')
ax.plot(t, I, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R, 'g', alpha=0.5, lw=1, label='Recovered with immunity')
ax.plot(x, 'o', label='Confirmed cases')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number')
ax.set_ylim(0,y_axis)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)

for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)

plt.show()

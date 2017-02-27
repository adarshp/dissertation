from __future__ import division
import numpy as np
from scipy.integrate import odeint
import matplotlib as mpl
mpl.use("pgf")
import matplotlib.pyplot as plt
pgf_with_rc_fonts = {
    "font.family": "Minion Pro",
    "font.serif": [],                   # use latex default serif font
    "font.sans-serif": ["DejaVu Sans"], # use a specific sans-serif font
}
mpl.rcParams.update(pgf_with_rc_fonts)

def figsize(scale):
    fig_width_pt = 281.0
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size

# Define a function which calculates the derivative
m = 1000
g = 100
sigma = 10**(-10)
m_planck = 2.44*(10**18)

plt.figure(figsize = figsize(1.0))
def y_eq(x):
    return 0.192*m_planck*m*sigma*(x**1.5)*np.exp(-x)

def dy_dx(y, x):
    return -(1/x**2)*(y**2-(y_eq(x)**2))
xs = np.linspace(1,1000,10000)
y0 = 1.7*(10**10)
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()
plt.style.use('fivethirtyeight')
plt.rc('font',size=10)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.rc('axes',labelsize=10)
plt.rc('axes',titlesize=10)
plt.loglog(xs, ys,linewidth=0.5)
plt.loglog(xs, y_eq(xs),'--', linewidth=0.5)
plt.ylim(10**(-5), 10**11)
plt.xlabel("x")
plt.ylabel("Number density");
plt.tight_layout()
# plt.savefig('../images/relic_density.pdf')
plt.savefig('relic_density.pgf')

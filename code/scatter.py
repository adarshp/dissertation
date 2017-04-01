# Code to create scatterplot representing separation between signal and
# background events in feature space.

from __future__ import division
import numpy as np
import matplotlib as mpl
# mpl.use('pgf')
import matplotlib.pyplot as plt
pgf_with_rc_fonts = {
    # "pgf.texsystem": "lualatex",
    "font.family": "serif",
    "font.serif": "Minion Pro",                   # use latex default serif font
    # "font.sans-serif": ["DejaVu Sans"], # use a specific sans-serif font
}
mpl.rcParams.update(pgf_with_rc_fonts)

def figsize(scale):
    fig_width_pt = 281.0
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    # fig_size = [fig_width,fig_height]
    fig_size = [fig_width,fig_width]
    return fig_size

plt.style.use('fivethirtyeight')
plt.figure(figsize = figsize(1.0))
plt.rc('font',size=10)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.rc('axes',labelsize=10)


circle = plt.Circle((5,5),2.0,facecolor='none',edgecolor='Green',linewidth=3)
plt.xlabel("Feature One")
plt.ylabel("Feature Two");


np.random.seed(5)
# Create a normal distribution of points, centered at (0, 0) 
signal_r = np.random.normal(15, 1, 500)
signal_theta = np.linspace(0,0.5*np.pi,500)

# Create a normal distribution of points, centered at (1, 1) 
background_r = np.random.normal(20, 1, 500)
background_theta = np.linspace(0,0.5*np.pi,500)

plt.scatter(background_r*np.cos(background_theta), background_r*np.sin(background_theta),alpha=0.4, color='Maroon',label='Background')
plt.scatter(signal_r*np.cos(signal_theta), signal_r*np.sin(signal_theta),alpha=0.4, color='DarkBlue',label='Signal')
plt.legend()
plt.tight_layout()

plt.savefig('scatter.pgf')

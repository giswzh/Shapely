from matplotlib import pyplot
from shapely.geometry.polygon import LinearRing

from figures import SIZE, set_limits

COLOR = {
    True:  '#6699cc',
    False: '#ff3333'
    }

def v_color(ob):
    return COLOR[ob.is_valid]

def plot_coords(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, 'o', color='#999999', zorder=1)

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=v_color(ob), alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 1: valid ring
ax = fig.add_subplot(121)
ring = LinearRing([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 0.8), (0, 0)])

plot_coords(ax, ring)
plot_line(ax, ring)

ax.set_title('a) valid')

set_limits(ax, -1, 3, -1, 3)

#2: invalid self-touching ring
ax = fig.add_subplot(122)
ring2 = LinearRing([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 1), (0, 0)])

plot_coords(ax, ring2)
plot_line(ax, ring2)

ax.set_title('b) invalid')

set_limits(ax, -1, 3, -1, 3)

pyplot.show()


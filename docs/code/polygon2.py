from matplotlib import pyplot
from matplotlib.patches import Circle
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch

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
    
fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 3: invalid polygon, ring touch along a line
ax = fig.add_subplot(121)

ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
int = [(0.5, 0), (1.5, 0), (1.5, 1), (0.5, 1), (0.5, 0)]
polygon = Polygon(ext, [int])

plot_coords(ax, polygon.interiors[0])
plot_coords(ax, polygon.exterior)

patch = PolygonPatch(polygon, facecolor=v_color(polygon), edgecolor=v_color(polygon), alpha=0.5, zorder=2)
ax.add_patch(patch)

ax.set_title('c) invalid')

set_limits(ax, -1, 3, -1, 3)

#4: invalid self-touching ring
ax = fig.add_subplot(122)
ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
int_1 = [(0.5, 0.25), (1.5, 0.25), (1.5, 1.25), (0.5, 1.25), (0.5, 0.25)]
int_2 = [(0.5, 1.25), (1, 1.25), (1, 1.75), (0.5, 1.75)]
# int_2 = [
polygon = Polygon(ext, [int_1, int_2])

plot_coords(ax, polygon.interiors[0])
plot_coords(ax, polygon.interiors[1])
plot_coords(ax, polygon.exterior)

patch = PolygonPatch(polygon, facecolor=v_color(polygon), edgecolor=v_color(polygon), alpha=0.5, zorder=2)
ax.add_patch(patch)

ax.set_title('d) invalid')

set_limits(ax, -1, 3, -1, 3)

pyplot.show()


from numpy import linspace, zeros, cos, sin, diff, pi
from matplotlib.pyplot import subplots

R = 2.0
ReG = [None] * 4
ImG = [None] * 4
L = [None] * 4

#  curve 1
L[0] = 6
ReG[0] = linspace(1.0 / R, R, L[0])
ImG[0] = zeros(L[0])
# curve 2
L[1] = 20
t = linspace(0.0, pi, L[1])
ReG[1] = R * cos(t)
ImG[1] = R * sin(t)
# curve 3
L[2] = 6
ReG[2] = linspace(-R , -1.0 / R, L[2])
ImG[2] = zeros(L[2])
# curve 4
L[3] = 6
t = linspace(-pi, 0.0, L[3])
ReG[3] = (1.0 / R) * cos(t)
ImG[3] = (1.0 / R) * sin(t)


fig, ax = subplots(figsize = (3.5, 3.5), dpi = 256)
ax.set_xlim(left = -2.5, right = 2.5)
ax.set_ylim(bottom = -2.5, top = 2.5)

for i in range(4):
    ax.quiver(ReG[i][:-1], ImG[i][:-1],
    diff(ReG[i]),
    diff(ImG[i]), color = 'C0')
 
    ax.text(x = ReG[i][L[i]//2],
    y = ImG[i][L[i]//2] - 0.25,
    s = fr'$\gamma_{i+1}$')
 
ax.scatter([0.0], [0.0], color = 'C1')
fig.savefig('VGc4no0RZg.jpeg', transparent = False, bbox_inches = 'tight');

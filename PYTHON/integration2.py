import numpy as np
import plotly.graph_objects as go

# Define region (x, y) and function z = f(x, y)
x = np.linspace(0, 2, 50)
y = np.linspace(0, 2, 50)
X, Y = np.meshgrid(x, y)
Z = X + Y  # surface (z = x + y)

# Create surface
surface = go.Surface(
    x=X, y=Y, z=Z,
    colorscale='Viridis',
    opacity=0.8,
    name='Surface z = x + y'
)

# Create base (the projection of R region on xy-plane)
base = go.Surface(
    x=X, y=Y, z=np.zeros_like(Z),
    colorscale=[[0, 'lightgray'], [1, 'lightgray']],
    opacity=0.4,
    showscale=False,
    name='xy-plane'
)

# Add a few sample vertical lines to show height (f(x, y))
sample_points = [(0.5, 0.5), (1, 0.5), (1.5, 1), (1.5, 1.5)]
lines = []
for (x0, y0) in sample_points:
    z0 = 0
    z1 = x0 + y0
    lines.append(go.Scatter3d(
        x=[x0, x0],
        y=[y0, y0],
        z=[z0, z1],
        mode='lines+markers',
        line=dict(color='red', width=5),
        marker=dict(size=4),
        name=f'Height at ({x0},{y0})'
    ))

# Combine all objects
fig = go.Figure(data=[surface, base] + lines)

# Layout settings
fig.update_layout(
    title="Double Integral: Volume under the surface z = f(x, y)",
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z',
        aspectratio=dict(x=1, y=1, z=0.7)
    ),
)

fig.show()

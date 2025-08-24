import plotly.graph_objects as go
import numpy as np
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
z = np.sin(np.sqrt(x**2 + y**2))
 
fig = go.Figure(data=go.Surface(x=x, y=y, z=z, colorscale='Viridis'))  
 
fig.update_layout(
    title='Surface Plot',
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z')
    )
)
fig.show()



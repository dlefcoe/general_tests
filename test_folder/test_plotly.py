
import os
import time
import numpy as np
import plotly.graph_objects as go


# Create the data
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
z = np.sin(np.sqrt(x**2 + y**2))

# Create the figure
fig = go.Figure(data=go.Surface(x=x, y=y, z=z, colorscale='Viridis'))

# Update the layout
fig.update_layout(
    title='Surface Plot',
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z')
    )
)


def display_plotly_chart(fig:go.Figure, chart_file:str = 'my_chart.html'):    


    fig.write_html(chart_file, auto_open=True)

    # Add a short delay to give the browser time to open the file
    print("Opening chart in browser. The file will be deleted in 5 seconds...")
    time.sleep(5)
    

    if os.path.exists(chart_file):
        os.remove(chart_file)
        print(f"File: '{chart_file}' has been deleted.")
    else:
        print(f"File: '{chart_file}' was not deleted properly.")

display_plotly_chart(fig)


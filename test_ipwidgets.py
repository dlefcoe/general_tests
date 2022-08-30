'''
widgets in interactive python 
or jupyter notebook

'''


# %%
import ipywidgets as widgets
from IPython.display import display
from datetime import date


last_connected = widgets.DatePicker(
    description='Pick a Date',
    disabled=False)

display(last_connected)


# %%
def days_between(last):
    return last - date.today()

x = days_between(last_connected.value)
print(x)



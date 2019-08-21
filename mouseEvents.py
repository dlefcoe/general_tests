'''

simulate mouse events in python
lets see where this goes

'''



import pynput as p

mouse = p.mouse.Controller()

# current mouse postion
x = mouse.position
print(x)

# move the mouse
mouse.move(20, -20)

# specify mouse position
mouse.position = (1500, 200)

# right mouse click
mouse.click(p.mouse.Button.right, 1)



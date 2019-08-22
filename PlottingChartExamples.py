


import matplotlib.pyplot as plt

# simple single line (no x values)
h = [20, 50, 100, 1000]
plt.plot(h)
plt.show()

# simple line chart
y = [1995, 2002, 2007, 2018]
h = [20, 50, 100, 1000]
plt.plot(y, h)
plt.show()


# simple green line chart with circles
y = [1995, 2002, 2007, 2018]
h = [20, 50, 100, 1000]
plt.plot(y, h, 'g-o')
plt.show()


# 2 lines on one chart
y = [1995, 2002, 2007, 2018]
h1 = [20, 50, 100, 1000]
h2 = [10, 25, 50, 800]
plt.plot(y, h1)
plt.plot(y, h2)
plt.show()



# 2 lines on one chart with circles and crosses
y = [1995, 2002, 2007, 2018]
h1 = [20, 50, 100, 1000]
h2 = [10, 25, 50, 800]
plt.plot(y, h1, 'g-o')
plt.plot(y, h2, 'r-x')
plt.show()


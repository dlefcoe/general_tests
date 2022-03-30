'''

implement the black scholes module

'''


import numpy as np
from scipy.stats import norm


# define variables
r = 0.01    # 1% = 0.01
s = 30      # price of underlying, ccy
k = 40      # price of strike, ccy
t = 240/365 # number of years
v = 0.30    # volatility in ccy
y = 'call'     # type, call or put

def black_scholes(r,s,k,t,v,y):
    '''calculate bs option price for put or call
    
    args:
        r (float): interest rate. where 0.01 = 1%, 0.05 = 5%
        s (float): current price of the underlying (in currency). so 30 means 30 USD
        k (float): strike price of the option (in currency). so 50 means 50 USD
        t (float): number of years
        v (float): volatility in currency. so 1.5 mean 1.5 usd
        y (string): the option type. So either call or put
    
    return:
        price = the price of the option
    '''
    d1 = (np.log(s/k) + (r + v**2/2)*t) / (v*np.sqrt(t) )
    d2 = d1 - v*np.sqrt(t)
    try:
        if y == 'call':
            price = s*norm.cdf(d1, 0, 1) - k*np.exp(-r*t)*norm.cdf(d2, 0, 1)
        elif y == 'put':
            price = k*np.exp(-r*t)*norm.cdf(-d2, 0, 1) - s*norm.cdf(-d1, 0, 1)
        return price
    except:
        print('there is an error.')

    return 'error'


prem = black_scholes(r,s,k,t,v,y)
print(round(prem, 2))


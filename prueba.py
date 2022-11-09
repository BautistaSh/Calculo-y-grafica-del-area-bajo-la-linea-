import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


x = np.linspace(-1,3,1000)
def f(x): return x**2

# plt.plot(x, f(x))
# plt.axhline(color = 'black')
# plt.fill_between(x, f(x), where=[(x > 0) and (x < 2) for x in x], color = 'green', alpha=0.3)
# x = sy.Symbol('x')
# sy.integrate(f(x), (x,0,2))

def g(x): return x**(1/2)
x = np.linspace(-1, 1.5,100)
plt.plot(x, f(x))
plt.plot(x, g(x))

plt.fill_between(x,f(x),g(x), where=[(x > 0) and (x < 1) for x in x], color = 'green', alpha=0.2)



plt.show()

import matplotlib.pyplot as plt 

euler_y = []
runge_kutta_y = []

tempo = 0
passo = 1e-2
n = 50
y0 = 300

def func (t, y0): 
  return -10*y0


def euler_function (func, y0, tempo, passo, n) :
  euler_y.append(y0)
  for i in range(n):
    yk = y0 + passo * func(tempo, y0)
    euler_y.append(yk)
    y0 = yk
    tempo = tempo + passo


def runge_kutta_function (func, y0, h, n):
  runge_kutta_y.append(y0)

  for i in range(n):
    yk = runge_kutta_y[i]

    t = (i-1)*h
    k1 = func(t, yk)
    k2 = func(t + (h/2), yk + ((h/2)*k1))
    k3 = func(t + (h/2), yk + ((h/2)*k2))
    k4 = func(t + h, yk + (h*k3))
    t = t + h
    runge_kutta_y.append(yk + (h/6)*(k1 + (2*k2) + (2*k3)+ k4))


euler_function(func, y0, tempo, passo, n)
runge_kutta_function(func, y0, passo, n)


print ("{:<15} {:<15}".format('Euler','Range-Kutta'))

for i in range(n): 
  print ("{:<15.7f} {:<15.7f}".format(euler_y[i], runge_kutta_y[i]))


plt.plot(runge_kutta_y)    
plt.plot(euler_y)    
plt.show()
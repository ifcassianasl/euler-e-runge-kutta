
import matplotlib.pyplot as plt 

euler_y = []
runge_kutta_y = []

tempo = 0
passo = 1e-2
n = 15
y0 = 300

def func (t, y0): 
  return -10*y0


def euler_function (func, y0, tempo, passo, n) :
  euler_y.append(y0)
  for i in range(n):
    yk = euler_y[i]
    yk1 = yk + passo * func(tempo, yk)
    euler_y.append(yk1)
    tempo = tempo + passo

    if yk1 <= y0/2:
      return tempo



def runge_kutta_function (func, y0, h, n):
  runge_kutta_y.append(y0)

  for i in range(n):
    yk = runge_kutta_y[i]
    if yk <= y0/2:
      return t

    t = (i-1)*h
    k1 = func(t, yk)
    k2 = func(t + (h/2), yk + ((h/2)*k1))
    k3 = func(t + (h/2), yk + ((h/2)*k2))
    k4 = func(t + h, yk + (h*k3))
    t = t + h
    runge_kutta_y.append(yk + (h/6)*(k1 + (2*k2) + (2*k3)+ k4))



euler_tempo = euler_function(func, y0, tempo, passo, n)
runge_kutta_tempo = runge_kutta_function(func, y0, passo, n)

print(euler_tempo)
print(runge_kutta_tempo)

print ("{:<15}".format('Euler'))
for i in euler_y: 
  print ("{:<15.7f}".format(i))

print ("{:<15}".format('Runge-Kutta'))
for i in runge_kutta_y: 
  print ("{:<15.7f}".format(i))


plt.plot(runge_kutta_y, color='red')    
plt.plot(euler_y, color='green')    
plt.show()
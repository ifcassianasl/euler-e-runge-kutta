
import matplotlib.pyplot as plt 
import numpy as np

euler_y = []
runge_kutta_y = []
tempo_utilizado = [0]

tempo = 0
passo = 1e-2
n = 1
y0 = 300

def func (t, y0): 
  return -10*y0


def euler_function (func, y0, tempo, passo, n):
  itmax = int(n/passo)
  euler_y.append(y0)
  for i in range(itmax):
    yk = euler_y[i]
    yk1 = yk + passo * func(tempo, yk)
    euler_y.append(yk1)
    tempo = tempo + passo
    tempo_utilizado.append(tempo)

    if yk1 <= y0/2:
      return tempo



def runge_kutta_function (func, y0, h, n):
  runge_kutta_y.append(y0)
  itmax = int(n/h)

  for i in range(itmax):
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

print("Tempo em Euler", euler_tempo)

print ("{:<15}".format('Euler'))
for i in euler_y: 
  print ("{:<15.7f}".format(i))

print("\n\n\n\nTempo em Runge-Kutta", runge_kutta_tempo)
print ("{:<15}".format('Runge-Kutta'))
for i in runge_kutta_y: 
  print ("{:<15.7f}".format(i))

def func_teorico (t):
  return 300*np.exp(-10*t)

print ("{:<15}".format('Resultados analíticos'))
resultados_teoricos = []
for i in tempo_utilizado:
  resultado = func_teorico(i)
  resultados_teoricos.append(resultado)
  print ("{:<15.7f}".format(resultado))


plt.plot(runge_kutta_y, color='green')    
plt.plot(euler_y, color='red')    
plt.plot(resultados_teoricos, color='black', linestyle="dotted")    
plt.show()
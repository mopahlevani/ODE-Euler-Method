import numpy
from matplotlib import pyplot
def odeEuler(f,y0,t): 
    y = numpy.zeros(len(t)) 
    y[0] = y0 
    for n in range(0,len(t)-1): 
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n]) 
    return y 
t = numpy.linspace(0,10,100)
y0 = 1
f = lambda y,t: y
y = odeEuler(f,y0,t)
yReal = numpy.exp(t)
pyplot.plot(t,y,'b.-',t,yReal,'r-')
pyplot.legend(['Euler','Real'])
pyplot.axis([0,10,0,20000])
pyplot.grid(True)
pyplot.title("Euler solution of y'=y , y(0)=1")
pyplot.show()
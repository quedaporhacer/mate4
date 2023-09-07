import plotly.graph_objs as go
import numpy as np

# ================ 1 Variable ================

# Se evaluan el etendimiento de los paramentro de la funcion
# El criteo de corte es malisimo (el error)
# -> Corta antes o corta cuando esta en el minimo

# ->  por ejemplo cuando la funcion es Par 
#       en este caso me da valores cercanos pero me movi muccho

f1 = lambda x: x**2
df = lambda x: 2*x
xprev= -4
paso = 1
tolerancia = 0.001
iteraciones = 1
maxiteraciones = 50

next = lambda xprev: xprev - paso * df(xprev)

x = np.linspace(-5,5,200)
y = f1(x)

#Plot
fig = go.Figure(data=[go.Scatter(x=x,y=y,mode='lines',line=go.scatter.Line(color='red'))])
fig.add_trace(go.Scatter(x=[xprev], y=[f1(xprev)]))

if(df(xprev) != 0):
    xnew = next(xprev)
    error = abs(f1(xnew)) -f1(xprev)  # pag5 GradientDescent.pdf
    print(f"x_prev = {xprev}, x_new = {xnew}, error = {error}")
    fig.add_trace(go.Scatter(x=[xnew], y=[f1(xnew)]))

    while(error > tolerancia and df(xnew) != 0 and iteraciones < maxiteraciones):
        iteraciones = iteraciones + 1
        xprev =  xnew
        xnew =  next(xprev)
        xnew = next(xprev)
        error = abs(f1(xnew)) -f1(xprev)
        print(f"x_prev = {xprev}, x_new = {xnew}, error = {error}")
        fig.add_trace(go.Scatter(x=[xnew], y=[f1(xnew)]))

#Plot
fig.show()

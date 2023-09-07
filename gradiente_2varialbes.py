import plotly.graph_objs as go
import numpy as np

# ================ 2 Variable ================

# Se evalúan el rendimiento de los parámetros de la función
# El criterio de corte es malísimo
# -> Corta antes o corta cuando está en el mínimo

# -> por ejemplo cuando la función es Par 
# en este caso me da valores cercanos pero me muevo mucho

f1 = lambda x, y: x**2 - y**2 
dfx = lambda x: 2*x
dfy = lambda y: -2*y

xprev = -4
yprev = 0
paso = 0.2
tolerancia = 0.001
iteraciones = 1
maxiteraciones = 20

xnext = lambda xprev: xprev - paso * dfx(xprev)
ynext = lambda yprev: yprev - paso * dfy(yprev)

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
z = f1(X, Y)

# Plot
fig = go.Figure(data=go.Surface(z=z,x=x,y=y, showlegend=True, opacity=0.7))
fig.update_traces(showscale=False)

fig.add_trace(go.Scatter3d(x=[xprev], y=[yprev], z=[f1(xprev, yprev)],mode='markers',marker=dict(size=10), visible='legendonly'))

if dfx(xprev) != 0 or dfy(yprev) != 0:
    xnew = xnext(xprev)
    ynew = ynext(yprev)

    error = np.sqrt(xnew**2 + ynew**2)  # ¿Qué pasa cuando el vector se acerca al punto silla? -> tiende a 0
    # definimos otra forma de error 
    # print(f"x_prev = {xprev}, x_new = {xnew}, error = {error}")
    fig.add_trace(go.Scatter3d(x=[xnew], y=[ynew], z=[f1(xnew, ynew)],mode='markers',marker=dict(size=20), visible='legendonly'))

    while error > tolerancia and iteraciones < maxiteraciones:
        iteraciones = iteraciones + 1
        xprev = xnew
        xnew = xnext(xprev)
        yprev = ynew
        ynew = ynext(yprev)
        error = abs(f1(xnew, ynew) - f1(xprev, yprev))
        fig.add_trace(go.Scatter3d(x=[xnew], y=[ynew], z=[f1(xnew, ynew)],mode='markers',marker=dict(size=20), visible='legendonly'))

# Plot
fig.show()

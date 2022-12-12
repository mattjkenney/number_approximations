#f: required, a function of y or x in terms of y or x
#y: required, known y value
#x: required, known x value
#h: required, step size
#x_initial: required, minimum value to clip the data chart
#x_final: required, maximum value to approximate
#method: required, a function to calculate the approximation, you can enter
    #any function, however, the function must take arguments
    # "f, y, x, h, x_final, decimals, stepx" in that order, and return
    # "x-values (list or tuple), y-values (list or tuple), and h values
    # (list or tuple)" in that order
    # You can also use the methods built into this module:
    # euler, improved euler, or runge_kutta
#decimals: required, the number of decimals to use for rounding
#stepx: optional, defaults to True. If True, will apply the h-value to the
    #x-axis for each step and approximate the y-value. If False, applies the
    #h-value to the y-axis for each step and approximate the x-value

def euler(f, y, x, h, end, decimals, stepx=True):
    
    ss = []
    cs = []
    hs = []
    if stepx:
        s = x
        c = y
    else:
        s = y
        c = x
    while s <= end:
        ss.append(s)
        cs.append(round(c, decimals))
        c_add = h * f(s, c)
        c += c_add
        s = round(s + h,10)
        hs.append(c_add)
    if stepx:
        xs = ss
        ys = cs
    else:
        xs = cs
        ys = ss
    return xs, ys, hs

def improved_euler(f, y, x, h, x_final, decimals):

    steps = int((x_final - x) / h) + 1
    xs = []
    ys = []
    hs = []
    for i in range(steps):
        xs.append(x)
        ys.append(round(y, decimals))
        k1 = f(x, y)
        u = y + h * k1
        x = round(x + h, 10)
        k2 = f(x, u)
        y_add = h * 0.5 * (k1 + k2)
        y += y_add
        hs.append(y_add)
    return xs, ys, hs

def runge_kutta(f, y, x, h, x_final, decimals, stepx=True):

    def y_add(x, y, h):
        k1 = f(x, y)
        k2 = f(x + 0.5 * h, y + (0.5 * h * k1))
        k3 = f(x + 0.5 * h, y + (0.5 * h * k2))
        x = round(x + h,10)
        k4 = f(x, y + (h * k3))
        y1 = (h / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
        return x, y1
    
    
    xs = []
    ys = []
    hs = []
    while x <= x_final:
        xs.append(x)
        ys.append(y)
        x, y1 = y_add(x, y, h)
        y += y1
        hs.append(y1)
    return xs, ys, hs
        
        

def approximation_chart(f, y, x, h, x_initial, x_final, decimals, method,
                        stepx=True):

    from pandas import DataFrame

    xs, ys, hs = method(f, y, x, h, x_final, decimals, stepx)
    df = DataFrame({'xn': xs, 'yn': ys, 'hs': hs})
    dfi = df[df['xn'] >= x_initial]

    return dfi


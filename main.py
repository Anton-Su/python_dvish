import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def app(func):
    label = tk.Label()
    img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def rect(x, y, width, height):
    inside = -min(width - abs(x), height - abs(y))
    outside = math.sqrt(max(abs(x) - width, 0) ** 2 + max(abs(y) - height, 0) ** 2)
    return outside + inside


def circle(x, y, r):
    return math.sqrt(x ** 2 + y ** 2) - r


def union(*a):
    return min(*a)


def intersect(*a):
    return max(*a)


def difference(a, b):
    return max(a, -b)


def sdf_func(x, y):
    return difference(difference(circle(x, y, .4), circle(x, y, .2)), rect(x - 0.38, y, .3, .5))


def shader(x, y):
    d = sdf_func(x - 0.5, y - 0.5)
    return d > 0, abs(d) * 3, 0


app(shader)

#sum
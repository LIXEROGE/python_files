import tkinter as tk
from PIL import Image as img
from tkinter.filedialog import *
import sys


def _e():
    global f
    print(img)
    f.delete(1.0, "end")
    p = img.open(c.get())
    k = p.load()
    p2 = ""
    p3 = ""
    if g.get()=="rgb3":
        for i2 in range(int(p.size[1]/5)):
            for i1 in range(int(p.size[0]/5)):
                i3 = k[i1*5, i2*5]
                p2 += str(i3[0]).ljust(3, "0")
                p2 += str(i3[1]).ljust(3, "0")
                p2 += str(i3[2]).ljust(3, "0")
                p3 += (str(i3[0]).ljust(3, "0"))
                p3 += (str(i3[1]).ljust(3, "0"))
                p3 += (str(i3[2]).ljust(3, "0"))

            p3 += ","

    elif g.get()=="6553R":
        for i2 in range(int(x.get())):
            for i1 in range(int(y.get())):
                i3 = k[int(i1*p.size[0]/int(x.get())), int(i2*p.size[1]/int(y.get()))]
                p3 += str(i3[0]*65536+i3[1]*256+i3[2]).ljust(8, "0")  # 最大也就8位（255，255，255），好像是什么16777215/滑稽
                """
                p2 += str(i3[1]).ljust(3, "0")
                p2 += str(i3[2]).ljust(3, "0")
                p3 += (str(i3[0]).ljust(3, "0"))
                p3 += (str(i3[1]).ljust(3, "0"))
                p3 += (str(i3[2]).ljust(3, "0"))"""

            p3 += ","
            
    elif g.get()=="rgb1":
        for i2 in range(int(x.get())):
            for i1 in range(int(y.get())):
                i3 = k[int(i1*p.size[0]/int(x.get())), int(i2*p.size[1]/int(y.get()))]
                p3 += chr(int(i3[0]))
                p3 += chr(int(i3[1]))
                p3 += chr(int(i3[2]))

            p3 += ","

    elif g.get().lower()=="6553c":
        for i2 in range(int(x.get())):
            for i1 in range(int(y.get())):
                i3 = k[int(i1*p.size[0]/int(x.get())), int(i2*p.size[1]/int(y.get()))]
                p2 = str(i3[0]*65536+i3[1]*256+i3[2]).ljust(9, "0")
                p3 += chr(int(p2[:3]))
                p3 += chr(int(p2[3:6]))
                p3 += chr(int(p2[6:9]))

            p3 += ","
            
    f.insert(tk.INSERT, p3)
    print(p3)
    pass


def _p():
    c.delete(0, 9999)
    c.insert(0, askopenfilename())


root = tk.Tk()  # C:\Users\86159\Desktop\PythonWriter\helloWorld64.py C:/Users/86159/Desktop/COLOR.png
root.geometry("500x500+500+500")
# root.overrideredirect(True)

b = tk.Label(text="点击退出", font=999, fg="red", cursor="plus")
b.bind("<Button-1>", sys.exit)
b.place(x=420, y=0)

a = tk.Label(text="图片转换3D-class格式器", font=999)
a.place(x=0, y=0)

c = tk.Entry()
c.insert(0, "图片的路径……")
c.place(x=0, y=30)

d = tk.Button(text="点击选择", command=lambda x=0: _p())
d.place(x=0, y=50)

e = tk.Button(text="点击转换", command=lambda x=0: _e())
e.place(x=0, y=80)

f = tk.Text(root, width=50, height=30, undo=1, autoseparators=False)
f.place(x=0, y=110)
f.insert(tk.INSERT, '转换内容……')

g = tk.Entry()
g.insert(0, "6553R")
g.place(x=240, y=30)

h = tk.Label(text="转换格式", font=30)
h.place(x=150, y=28)

m = tk.Label(text="转换大小", font=30)
m.place(x=150, y=56)

x = tk.Entry()
x.insert(0, "120")
x.place(x=240, y=60)

y = tk.Entry()
y.insert(0, "120")
y.place(x=270, y=60)
root.mainloop()



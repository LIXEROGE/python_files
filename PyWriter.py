M__="1.0.4"
from tkinter.filedialog import askdirectory

import os,sys,time,random

os.system("cd "+sys.path[0])
print(sys.path[0])

from tkinter import *
from threading import Thread
from time import sleep
LOP=None
def lprint(spp="_",end='\n',sub='_'):
    print(spp,end=end)

def getaa(p__,b__):
    global aa,bb
    return (1 and b__ in bb)
    pass
#设置tkinter窗口
def err(aaa=''):
    global rv
    print("\a")
    root.title("=__=python编辑器-打开失败，ERROR=" + str(aaa) + "=__=")
def opn():
    p=e1.get()
    pathchoise()

    try:
        root.title("=__=python编辑器-加载中=__=")
        if(not e1.get()):
            e1.delete(0,END)
            e1.insert(END,p)
            raise ZeroDivisionError("用户取消")
        e2.delete(0.0,END)
        p=open(e1.get())
        e2.insert(END, p.read())
        p.close()
        root.title("=__=python编辑器-打开成功=__=")
    except Exception as exc:
        err(exc)
        #'''
    pass
def pathchoise():
    path_ = filedialog.askopenfilename(filetypes=[('所有文件','*.*'),('pythonScripts','*.py')])
    e1.delete(0,END)
    e1.insert(END,path_)
def init():
    global root,e1,e2,c__capcisic,usr,pas
    global theButton1,theButton2,theButton3
    usr=pas=None
    root = Tk()
    #root.attributes("-alpha", 0.78)
    root.config(relief='solid')
    #root.config(font=('times', 20, 'roman') )
    root.geometry("700x450")
    root.title("=__=python编辑器::"+M__+" -from刘予煊=__=")

    #绘制两个label, （）确定行列
    global rand
    rand=random.randint(1,32767)%100
    Label(root, text="                            python编辑器(请确保安装了python) -"+str(rand)).place(y=0)#-from 刘予煊
    #Label(root,text='').gri d(row = 0,column =1)
    #Label(root, text='').gr id(row=0, column=2)
    Label(root,text="文件夹路径:").place(y=22,x=20)
    Label(root, text="文件名:").place(y=122, x=20)
    Label(root,text="请输入代码:").place(y=44,x=20)

    global e11
    #导入两个输入框
    e1 = Entry(root,font=("Calibri",13))
    e11 = Entry(root, font=("Calibri", 13))
    e1.insert(END,sys.path[0]+"\\helloWorld"+str(rand)+".py")#+      "helloWorld"+str(rand)+".py"
    e11.insert(END,"helloWorld"+str(rand)+".py")
    e2 = Text(cursor='target')
    e2.insert(END,f'#!python3\n# -*-coding : UTF-8 -*-\n\nprint("helloWorld{str(rand)}.py is running!")\n\n\n\n\n\n\n')

    #设置输入框的位置
    #e1.g rid(row =1 ,column =0)
    e1.place(x=100, y=25,width=500, height=20)

    #e11.place(x=500, y=25,width=100, height=20)
    e2.place(x=20,y=75)
    #

    scroll = Scrollbar(root)

    #scroll.pack(side=LEFT, fill=Y)  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填
    scroll.place(x=585,y=50,height=350)


    scroll.config(command=e2.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
    #scroll.g rid(row=0, column=5,ipady=150)

    e2.config(yscrollcommand=scroll.set)  # 将滚动条关联到文本框
    #输入内容获取函数print打印
    c__capcisic=0

    # 设置两个按钮，点击按钮执行命令 command= 命令函数
    theButton1 = Button(root, text="运行", width=10, command=show,cursor='hand2')
    theButton2 = Button(root, text="清除", width=10, command=dele,cursor='hand2')
    theButton3 = Button(root, text="退出", width=10, command=xiiit___,cursor='hand2')
    theButton4 = Button(root, text="打开", width=10, command=opn,cursor='hand2')

    # 设置按钮的位置行列及大小
    theButton1.place(x=20,y=410)
    theButton2.place(x=120,y=410)
    theButton3.place(x=220,y=410)
    theButton4.place(x=610,y=20)

func____=getaa
def show():
    global pas,aa,func____
    global usr,bb,c__capcisic
    if func____==None:
        func____=getaa
    a=e1.get()
    b=e2.get('0.0','end')
    if func____(a,b):
        lprint("user：%s"%a)
        lprint("password：%s"%b)
        usr=a
        pas=b
        root.destroy()
    else:
        try:
            c__capcisic += 1
            #Label(root, text=" -----------------------running---------------------").gr id(row=0, column=0)#'<登录失败><次数:'+str(c__capcisic)+'>'
            root.title("=__=python编辑器-加载中=__=")
            #time.sleep(1)
            p=open(e1.get(),'w')
            p.write(b)
            p.close()


            os.system("start "+sys.path[0]+"\\startpys.exe "+e1.get())
        except Exception as p:


            err(p)
            #'''
        else:

            root.title("=__=python编辑器-运行成功=__=")
        #Label(root, text="                      OK!                      ").gri d(row=0, column=0)  # '<登
        #e2.delete(0.0, END)

#清除函数，清除输入框的内容
def dele():
    global usr,pas
    usr=None
    pas=None
    #e1.delete(0,END)
    e2.delete(0.0,END)

def xiiit___():
    global usr,pas
    usr=pas=None
    root.destroy()
def login_getpas(userss___ = [],pas___=['exit'],pasfunc=None,pdrowing=0):
    sleep(1)
    if not pdrowing:
        global aa,usr,pas,LOP,func____
        init()
        aa=userss___
        global bb
        bb=pas___
        func____=pasfunc
        mainloop()
        return usr,pas
def login(userss___ = ['1234','liuyuxuan'],pas___=['4321','suanfa62f'],pasfunc=None,pdrowing:int=0):
    dd=Thread(target=login_getpas)#,args={'userss___ ':['1234','liuyuxuan'],'pas___':['4321','suanfa62f'],'pdrowing':0})
    dd.start()
    return 0
if(__name__=='__main__'):
    os.system(sys.path[0]+"\\hide.exe")
    #pri nt(_default_root)
    lprint(login_getpas( ))
else:
    print(__name__)

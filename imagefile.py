
try:
    import tkinter as tk
    import sys , os , time
    from threading import *
    from PIL import Image , ImageTk
    #from tkinter import *
    os.chdir(sys.path[0])
except Exception as p:
    print(p)
    while(1):
        pass

class CanImage():
    global image
    def __init__(self,root:tk.Tk,path:str,font=("华文行楷", 20),fg=None,logo:str=''):
        '''__init__ -> None
        init image object.'''
        self.root = root
        self.path = path
        self.logo = logo
        self.fg = fg
        self.font = font
        self.PhotoImage = None
        #self.render()
        #self.render2()
        self.render2()
        self.render()

        def __mov__(event):
            '''listening moves. &AAA'''
            global p
            p.show('place', event.x, event.y)

        self.__mov__=__mov__
        #root.bind("<Motion>", self.__mov__)
    def __str__(self):
        return self.path+'\n'+self.logo

    def bind(self,sequence="<Motion>", func=None, add=None):
        ''' bind -> None
        bind on root. '''
        self.root.bind(sequence=sequence, func=func, add=add)
    def render(self):
        if(not self.PhotoImage):
            self.PhotoImage=tk.PhotoImage(file=self.path)
        if self.fg:
            self.img = tk.Label(root, text=self.logo, image=self.PhotoImage, font=self.font, fg=self.fg)
        else:
            self.img = tk.Label(root, text=self.logo, image=self.PhotoImage, font=self.font)

    def render2(self):
        '''
        self.PILimage=Image.open(self.path)
        if self.fg:
            self. img = tk.Label(root, text=self.logo, image=self.PILimage, font=self.font, fg=self.fg)
        else:
            self. img = tk.Label(root, text=self.logo, image=self.PILimage, font=self.font)

        self.PILimage=Image.open(self.path)
        Canvas1 = tk.Canvas(root)
        a,b=self.PILimage.size#image.size
        Canvas1.create_image(a,b, image=ImageTk.PhotoImage(self.PILimage))
        #Canvas1.config(width=100, height=100)
        Canvas1.p a c k(side=tk.LEFT,expand=True,fill=tk.BOTH)'''
        global img,image


        path = self.path

        image = Image.open(path)
        self._image = Image.open(path)

        [imageSizeWidth, imageSizeHeight] = image.size
        global newImageSizeWidth ,newImageSizeHeight
        newImageSizeWidth = int(imageSizeWidth)
        newImageSizeHeight = int(imageSizeHeight)

        #if same:
        #    newImageSizeWidth = int(imageSizeWidth * n)
        #    newImageSizeHeight = int(imageSizeHeight * n)
        #else:
        #    newImageSizeWidth = int(imageSizeWidth / n)
        #    newImageSizeHeight = int(imageSizeHeight / n)

        img = ImageTk.PhotoImage(image)
        self.PhotoImage=img
        #Canvas1 = tk.Canvas(self.root)#----------------------------

        #Canvas1.create_image(newImageSizeWidth / 2, newImageSizeHeight / 2, image=img)
        #Canvas1.config(width=newImageSizeWidth, height=newImageSizeHeight)

        # bg="blue",
        #Canvas1.pa ck(side=tk.LEFT, expand=True, fill=tk.BOTH)
        #self.can = Canvas1#############################---------------------------------------------------------------

    def set_pixel(self,x=0,y=0,RGB=(0,0,0)):
        '''set_pixel -> None
        Set pixel on (x,y).'''
        global image
        pixels = image.load()

        pixels[x,y]=RGB

        _p = self.image.load()

        _p [x, y] = RGB

        return None

    def get_pixel(self,x=0,y=0):
        '''get_pixel -> tuple
        Get pixel on (x,y).'''
        global image

        global image
        pixels = image.load()

        return pixels [x,y]
    def clear(self):
        '''clear -> Exception | None
        Clear the canvas.'''
        try:
            global img , image

            self.can.place_forget()
        except Exception as p:
            return p
        else:
            return None
    def resize(self,x=50,y=50):
        '''resize image.'''
        print("RESIZE "+str(x)+'  -  '+str(y))
        global img,image
        image = self._image.resize((x,y), Image.ANTIALIAS)
        self.image=image

        img = ImageTk.PhotoImage(image)
        self.PhotoImage=img
        #Canvas1 = tk.Canvas(self.root)

        #Canvas1.create_image(newImageSizeWidth / 2, newImageSizeHeight / 2, image=img)
        #Canvas1.config(width=newImageSizeWidth, height=newImageSizeHeight)

        # bg="blue",
        #Canvas1.pa ck(side=tk.LEFT, expand=True, fill=tk.BOTH)
        #self.can = Canvas1
        self.render()

    def show(self, mod='place', x=0, y=0, run=0):
        ''' show the image(on the root). '''
        if mod=='place':
            self.img.place(x=x,y=y)
        #self.can.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        if(run):
            self.root_run()
        else:
            pass
            self.root.update()
    def run(self):
        '''root_run -> None
        run the root.'''
        self.root.mainloop()
'''
def pd():
    pass
    a=100
    time.sleep(1)
    while(a<1000):
        time.sleep(0.08)
        a+=2
        p.resize(x=100, y=100)
        p.show('place',a,a)
    return
'''
if __name__ == '__main__':

    a=open(sys.path[0]+"\\333.png",'r')
    root = tk.Tk()
    root.geometry("600x600")
    # 增加背景图片
    #photo = tk.PhotoImage(file=sys.path[0]+"\\333.png")
    #theLabel = tk.Label(root,text = "我是内容,\n请你阅读",image = photo,font = ("华文行楷", 20),fg = "white")
    #justify = tk.LEFT,compound = tk.CENTER,
    #theLabel.place(x=10,y=10)

    p=CanImage(root,sys.path[0]+"\\333.png",logo='hello')

    #oo=Thread(target=pd)
    #oo.setDaemon(True)
    #oo.start()
    #p.root.attributes('-fullscreen',True)
    p.resize(x=100,y=120)
    p.set_pixel(10,10,(255,255,255,100))
    p.get_pixel(10,10)
    print(p.get_pixel(10,10))
    #p.show(x=30,y=30,run=True)
    x=0
    y=0
    def __mov__(event):
        '''listening moves. &AAA'''
        global p,x,y

        p.show('place',x,y)
        x=x+4
    p.bind(func=__mov__)
    p.run()
    '''except Exception as p:
        print(p)
        while(1):
            pass
    #'''
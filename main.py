import os
import win32con
import win32api
import sys
class Connect:
    data_path = "C:\\Temp\\"
    def __init__(self,id=0):
        self.id = id
        print(self.data_path+str(self.id))
        self.file = open(self.data_path+str(self.id),"w")
        if os.path.isdir(self.data_path):
            pass
        else:
            os.mkdir(self.data_path)
    def write(self,data=""):
        self.file = open(self.data_path + str(self.id), "w+")
        self.file.write(data)
    def read(self):
        self.file.close()
        self.file = open(self.data_path + str(self.id), "r")
        return self.file.read()
    def quit(self):
        self.file.close()
        try:
            os.remove(self.data_path+str(self.id))
        except:
            print("error!")
a = Connect()
print(a.write("y"))
print(a.read())


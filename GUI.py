import tkinter as tk
import qrcode
from PIL import ImageTk, Image  
import a
root = tk.Tk()
id="N"
var = ""
root.geometry('500x400')

def getqrcode(code):
    img = qrcode.make(data=code)
    with open('test.png', 'wb') as f:
        img.save(f)
    image1 = Image.open("test.png")
    test = ImageTk.PhotoImage(image1)
    label1.image = test
    label1["image"]=test    
    
def showcode():
    code=a.getcode(E1.get())
    print(E1.get(),len(E1.get()))
    E.delete(0, 20)
    E.insert(0,code)
    if code != "ERROR":
        
        getqrcode(a.getcode(E1.get()))
    
def vali():
    print(E.get(),len(E.get()))
    w['text']=a.validate(E.get())

E = tk.Entry(root, textvariable=var)
B = tk.Button(root, text ="生成", command = showcode)
E1 = tk.Entry(root)
B2 = tk.Button(root, text ="验证", command = vali)
w = tk.Label(root, text="")
label1 = tk.Label(root)

E1.pack()
B.pack()
E.pack()
B2.pack()
w.pack()

label1.pack()
root.mainloop()

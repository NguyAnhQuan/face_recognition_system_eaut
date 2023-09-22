from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pyodbc as pyo
import cv2
import webbrowser



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")  
        
        #title section
        title_lb1 = Label(self.root,text="Welcome To Help",font=("verdana",30,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\AI Ln\face_recognition system\college_images\dev_admin.png")#image left
        img_top=img_top.resize((1490,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(relx=0, rely=1, anchor='sw')
        
        # Bind a click event to the image label
        f_lb1.bind("<Button-1>", self.open_browser)
        
    def open_browser(self, event):
        webbrowser.open("https://www.facebook.com/NguyennAnhhQuan")

        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop() 
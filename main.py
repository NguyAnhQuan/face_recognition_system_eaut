from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter.messagebox




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        # self.root.wm_iconbitmap("1face.ico")
        
        # first img
        img=Image.open(r"D:\AI Ln\face_recognition system\college_images\eaut.jpg")     
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        # second img
        img1=Image.open(r"D:\AI Ln\face_recognition system\college_images\face_recognition.jpg")     
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        # third img
        img2=Image.open(r"D:\AI Ln\face_recognition system\college_images\eaut2.jpg")     
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        # bg img
        img3=Image.open(r"D:\AI Ln\face_recognition system\college_images\bg.jpg")     
        img3=img3.resize((1530,710),Image.LANCZOS)    
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=800)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=40)
        
        # studen button
        img4=Image.open(r"D:\AI Ln\face_recognition system\college_images\b1.png")     
        img4=img4.resize((600,337),Image.LANCZOS)    
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Studen details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        # detect face button
        img5=Image.open(r"D:\AI Ln\face_recognition system\college_images\b2.png")     
        img5=img5.resize((284,210),Image.LANCZOS)    
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue",command=self.face_data)
        b1_1.place(x=500,y=300,width=220,height=40)
        
        # Attendace face button
        img6=Image.open(r"D:\AI Ln\face_recognition system\college_images\Attendace.jpg")     
        img6=img6.resize((284,210),Image.LANCZOS)    
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendace",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue",command=self.attendance_data)
        b1_1.place(x=800,y=300,width=220,height=40)
        
        # help face button
        img7=Image.open(r"D:\AI Ln\face_recognition system\college_images\help.jpg")     
        img7=img7.resize((284,210),Image.LANCZOS)    
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        # Train face button
        img8=Image.open(r"D:\AI Ln\face_recognition system\college_images\traindata.jpg")     
        img8=img8.resize((284,210),Image.LANCZOS)    
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_dataset)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train data",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue",command=self.train_dataset)
        b1_1.place(x=200,y=580,width=220,height=40)
        
        # photo face button
        img9=Image.open(r"D:\AI Ln\face_recognition system\college_images\photoface.jpg")     
        img9=img9.resize((284,210),Image.LANCZOS)    
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue",command=self.open_img)
        b1_1.place(x=500,y=580,width=220,height=40)
        
        # developer button
        img10=Image.open(r"D:\AI Ln\face_recognition system\college_images\developer.jpg")     
        img10=img10.resize((284,210),Image.LANCZOS)    
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        # Exit button
        img11=Image.open(r"D:\AI Ln\face_recognition system\college_images\exit.jpg")     
        img11=img11.resize((284,210),Image.LANCZOS)    
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Exit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue",command=self.Exit)
        b1_1.place(x=1100,y=580,width=220,height=40)
        
        
        
    
    def open_img(self):
        os.startfile("data")
        
        
    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Face recognition","Are you sure exit this app")
        if self.Exit >0:
            self.root.destroy()
        else:
            return
    
    
        
    # =========================function buttons===============================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_dataset(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        
        
        
        
        
        
        
        
        
        
        


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
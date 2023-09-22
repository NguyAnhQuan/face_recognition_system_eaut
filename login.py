from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from student import Student
import os
import pyodbc as pyo
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from main import Face_Recognition_System



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        # self.root.wm_iconbitmap(r"1face.ico")
    
        
        #bg img
        img=Image.open(r"D:\AI Ln\face_recognition system\college_images\ai-artificial.jpg")     
        img=img.resize((1550,800),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)       

    

        # section login
        frame=Frame(self.root, bg= "gray", borderwidth=0, relief="solid")
        frame.place(x=580, y=170, width=340, height=450)
        # frame.tkraise() 
        
        
        img1=Image.open(r"D:\AI Ln\face_recognition system\college_images\user.png")
        img1=img1.resize((100, 100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1, bg="black" ,borderwidth=0)
        lblimg1.place(x=700, y=180, width=100, height=100)
        
        get_str=Label(frame, text= "Get Started" ,font=("times new roman",20, "bold"),fg="white", bg="gray")
        get_str.place(x=98,y=110)
        
         # label
        username=lbl=Label(frame, text= "Username", font=("times new roman" ,15, "bold"),fg="white",bg="gray")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame, font=("times new roman" ,15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame, text= "Password" ,font=("times new roman" ,15, "bold"),fg="white" ,bg="gray")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame ,show="•", font=("times new roman" ,15, "bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        
        
        # ======Icon Images===========
        img2=Image.open(r"D:\AI Ln\face_recognition system\college_images\user.png")
        img2=img2.resize((25, 25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2, bg="gray",borderwidth=0)
        lblimg2.place(x=620, y=323, width=25, height=25)
        
        img3=Image.open(r"D:\AI Ln\face_recognition system\college_images\pass-icon.png")
        img3=img3.resize((25, 25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3, bg="gray" ,borderwidth=0)
        lblimg3.place(x=620, y=393, width=25, height=25)
        
        
        #login button
        loginbtn=Button(frame,text="Login",command=self.login ,font=("times new roman" ,15, "bold"),bd=3,relief=RIDGE, fg= "white" ,bg="#CCCCCC", activeforeground="#777777",activebackground="#FFFFFF")
        loginbtn.place(x=110, y=310, width=120 ,height=35)
        
        registerbtn=Button(frame,text="New User Register" ,command=self.register,font=("times new roman" ,10, "bold"),borderwidth=0, fg= "white" ,bg="gray", activeforeground="#0066FF",activebackground="gray")
        registerbtn.place(x=15, y=370, width=160 ,height=19)
        
        forgetpassbtn=Button(frame,text="Forget Password" ,command=self.register,font=("times new roman" ,10, "bold"),borderwidth=0, fg= "white" ,bg="gray", activeforeground="#0066FF",activebackground="gray")
        forgetpassbtn.place(x=10, y=390, width=160 ,height=19)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Lỗi", "Cần điền đầy đủ thông tin")
        else:
            # Kết nối đến cơ sở dữ liệu
            cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
            my_cursor = cnxn.cursor()

            # Thực hiện truy vấn để kiểm tra thông tin đăng nhập
            query = "select * from userr where namee = ? and pass = ?"
            my_cursor.execute(query, (self.txtuser.get(), self.txtpass.get()))
            user_data = my_cursor.fetchone()

            # Đóng kết nối sau khi thực hiện truy vấn
            cnxn.close()

            if user_data:
                messagebox.showinfo("Thành công", "Chào mừng bạn đến với Hệ thống Nhận diện Khuôn mặt")
                
                 # Tạo một instance của Face_Recognition_System và đóng cửa sổ đăng nhập
                self.root.withdraw()  # Ẩn cửa sổ đăng nhập
                face_recognition_root = Toplevel(self.root)
                face_recognition_app = Face_Recognition_System(face_recognition_root)
                # hiển thị lại cửa sổ đăng nhập sau khi đóng cửa sổ nhận dạng khuôn mặt:
                self.root.deiconify()  # Hiển thị lại cửa sổ đăng nhập
            else:
                messagebox.showerror("Không hợp lệ", "Tên người dùng và mật khẩu không hợp lệ")
                
    def register(self):
        message = "🛡️ Vui lòng liên hệ Dev Admin trong trường hợp này 🪪👨‍💻\n                                  📞0962784293📲\n                     ✉️📨anhq46724@gmail.com📧"
        messagebox.showerror("Liên hệ admin",message)


        


        
    
        




    
if  __name__ == "__main__": 
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

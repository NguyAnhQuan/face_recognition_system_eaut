from sys import path
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
import pyodbc as pyo
import os
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv

mydata=[]
class Attendance:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Pannel")
        
        #-----------Variables-------------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        # first imag
        img=Image.open(r"D:\AI Ln\face_recognition system\college_images\banner.jpg")
        img=img.resize((800, 200), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0, width=800, height=200)
        
        
        # second image
        img1=Image .open(r"D:\AI Ln\face_recognition system\college_images\banner.jpg")
        img1=img1. resize((800, 200), Image. LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800,y=0, width=800, height=200)
        
        
        # bg img
        img3=Image.open(r"D:\AI Ln\face_recognition system\college_images\bg.jpg")     
        img3=img3.resize((1530,710),Image.LANCZOS)    
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=800)

        #title section
        title_lb1 = Label(self.root,text="Attendance management system",font=("verdana",30,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=130,width=1530,height=45)
        
        main_framee=Frame(bg_img,bd=2,bg="white")
        main_framee.place(x=20,y=50,width=1390,height=600)
        
        # Left Label Frame 
        left_frame = LabelFrame(main_framee,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"))
        left_frame.place(x=10,y=10,width=690,height=580)
        
        img_left=Image.open(r"D:\AI Ln\face_recognition system\college_images\b1.png")     
        img_left=img_left.resize((720,180),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=670,height=130)
 
        left_inside_framee=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_framee.place(x=5,y=135,width=670,height=420) 
        
        # ==================================Text boxes and Combo Boxes====================

        #Student id
        AttendanceID_label = Label(left_inside_framee,text="Attendance-ID:",font=("times-new-roman",12,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_entry = ttk.Entry(left_inside_framee,width=22,textvariable=self.var_atten_roll,font=("times-new-roman",12,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        rollLabel = Label(left_inside_framee,text="Roll:",font=("comicsansns",11,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll = ttk.Entry(left_inside_framee,textvariable=self.var_atten_roll,width=22,font=("comicsansns",11,"bold"))
        atten_roll.grid(row=0,column=3,padx=5,pady=8,sticky=W)
        
        #name
        nameLabel = Label(left_inside_framee,text="Name:",font=("comicsansns",11,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=8,pady=8,sticky=W)

        atten_name = ttk.Entry(left_inside_framee,width=25,textvariable=self.var_atten_id,font=("comicsansns",11,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=8,sticky=W)
        
        #dep
        depLabel = Label(left_inside_framee,text="Department:",font=("comicsansns",11,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=4,pady=8,sticky=W)

        atten_dep = ttk.Entry(left_inside_framee,width=22,textvariable=self.var_atten_name,font=("comicsansns",11,"bold"))
        atten_dep.grid(row=1,column=3,padx=5,pady=8,sticky=W)

        #time
        time_label = Label(left_inside_framee,text="Time:",font=("comicsansns",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=8,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_framee,width=25 ,textvariable=self.var_atten_dep,font=("comicsansns",11,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date 
        date_label = Label(left_inside_framee,text="Date:",font=("comicsansns",11,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_framee,width=22,textvariable=self.var_atten_time,font=("comicsansns",11,"bold"))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        #Attendance
        student_attend_label = Label(left_inside_framee,text="Attend-status:",font=("verdana",11,"bold"),bg="white")
        student_attend_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        self.atten_status=ttk.Combobox(left_inside_framee, width=23, textvariable=self.var_atten_date,font= "comicsansns 11 bold" ,state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1,padx=0, pady=10)
        self.atten_status.current(0)


        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_inside_framee,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=360,width=650,height=50)

        #save button
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=15,pady=5,sticky=W)

        #up button
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=5,sticky=W)

        #delete button
        del_btn=Button(btn_frame,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=5,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=12,command=self.reset_data,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=5,sticky=W)

        
        
        
        # right Label Frame
        right_frame = LabelFrame(main_framee,bd=2,bg="white",relief=RIDGE,text="Student details", font=("times new roman",12,"bold"))
        right_frame.place(x=710,y=10,width=660,height=580)
        
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=650,height=500) 
        
        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance-ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"


        # Set Width of Colums 
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=120)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        # self.fetchData()
        
        
    # ===========================fatch data form mysql attendance===========

    def fetchData(self, rows=None):
        if rows is not None:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("", END, values=i)

        
        
        
        # cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
        # my_cursor = cnxn.cursor()

        # my_cursor.execute("select * from stdattendance")
        # data=my_cursor.fetchall()

        # if len(data)!= 0:
        #     self.attendanceReport.delete(*self.attendanceReport.get_children())
        #     for i in data:
        #         self.attendanceReport.insert("",END,values=i)
        #     cnxn.commit()
        # cnxn.close()
        
    def importCsv (self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV FileFile","*csv"),("All FFile","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
    def reset_data(self):
        self.var_atten_id.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set("Status"),
        self.var_atten_attendance.set("")  
        
            
    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)            
            
            
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content["values"]

        self.var_atten_id.set(row[0]),
        self.var_atten_roll.set(row[1]),
        self.var_atten_name.set(row[2]),
        self.var_atten_dep.set(row[3]),
        self.var_atten_time.set(row[4]),
        self.var_atten_date.set(row[5]),
        self.var_atten_attendance.set(row[6])  
    
            
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
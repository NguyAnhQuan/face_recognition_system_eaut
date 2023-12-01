from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pyodbc as pyo
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")  
        
        
        #=============variables====================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        
        
       
       # first img
        img=Image.open(r"D:\AI Ln\face_recognition system\college_images\st1.jpg")     
        img=img.resize((500,200),Image.LANCZOS)
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
        img2=Image.open(r"D:\AI Ln\face_recognition system\college_images\st2.jpg")     
        img2=img2.resize((500,280),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        # bg img
        img3=Image.open(r"D:\AI Ln\face_recognition system\college_images\bg.jpg")     
        img3=img3.resize((1530,710),Image.LANCZOS)    
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=800)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",28,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=40)
        
        
        main_framee=Frame(bg_img,bd=2,bg="white")
        main_framee.place(x=20,y=50,width=1390,height=600)
            
        # left Label Frame
        Left_frame = LabelFrame(main_framee,bd=2,bg="white",relief=RIDGE,text="Student details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=580)
        
        img2_left=Image.open(r"D:\AI Ln\face_recognition system\college_images\b1.png")     
        img2_left=img2_left.resize((720,180),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img2_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=670,height=130)
        
        # current course information
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=670,height=125)
        
        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep ,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","It","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # course 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year 
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        # Class student information
        class_Student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information", font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=260,width=670,height=290)
        
        
        #student ID
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        
        # student name
        studenName_label=Label(class_Student_frame, text= "Student Name:",font=("times new roman",13, "bold"),bg="white")
        studenName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        studentName_entry=ttk. Entry(class_Student_frame,textvariable=self.var_std_name, width=18, font=("times new roman" ,13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        
        # class didvision
        class_div_label=Label(class_Student_frame, text= "Class Division:", font=("times new roman" ,13, "bold"),bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        # class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div, width=20, font=("times new roman" ,13, "bold"))
        # class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)
        div_combo["values"]=("DCCNTT13.10.1","DCCNTT13.10.2","DCCNTT13.10.3","DCCNTT13.10.4","DCCNTT13.10.5","DCCNTT13.10.6","DCCNTT13.10.7","DCCNTT13.10.8","DCCNTT13.10.9","DCCNTT13.10.10","DCCNTT13.10.11","DCCNTT13.10.12","DCCNTT13.10.13","DCCNTT13.10.14","DCCNTT13.10.15")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=1,sticky=W)
        
        
        
        # Roll No
        roll_no_label=Label(class_Student_frame, text= "Roll No: ", font=("times new roman" ,13, "bold"),bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
                                                                                                        
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll, width=18, font=("times new roman" ,13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
            
        # Gender
        gender_label=Label(class_Student_frame, text= "Gender:", font=("times new roman" ,13, "bold"),bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        # gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender, width=20, font=("times new roman" ,13, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # DoB
        dob_label=Label(class_Student_frame, text= "DOB:",font=("times new roman" ,13, "bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=18, font=("times new roman" ,13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        
        # Email
        email_label=Label(class_Student_frame, text="Email:", font=( "times new roman",13, "bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10, pady=5, sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman" ,13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        
        #phone no
        phone_label=Label(class_Student_frame, text= "Phone No:", font=("times new roman",13, "bold"),bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone, width=18, font=("times new roman" ,13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        # Address
        address_label=Label(class_Student_frame, text= "Address:",font=("times new roman" ,13, "bold"),bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        address_entry=ttk.Entry (class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman" ,13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        
        # Teacher name
        teacher_label=Label(class_Student_frame, text= "Teacher Name:",font=("times new roman" ,13, "bold"),bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        teacher_entry=ttk.Entry (class_Student_frame,textvariable=self.var_teacher, width=18, font=("times new roman" ,13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)


        # radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text= "Take Photo Sample" ,value="Yes")
        radionbtn1.grid(row=6, column=0)
                         
        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text= "No Photo Sample" ,value= "No")
        radionbtn2.grid(row=6,column=1)


        # bbuttons frame
        btn_frame=Frame(class_Student_frame, bd=2, relief=RIDGE, bg ="white")
        btn_frame.place(x=0  ,y=200, width=715, height=40)
        
        save_btn=Button(btn_frame, text= "Save",width=16,command=self.add_data, font= ("times new roman" ,13, "bold"),bg="blue" ,fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame, text= "Update" , width=16  , font=("times new roman" ,13, "bold"),bg="blue",fg="white",command=self.update_fuction)
        update_btn.grid(row=0, column=1)
        
        delete_btn=Button(btn_frame, text= "Delete" , width=16  , font=("times new roman" ,13, "bold"),bg="blue",fg="white",command=self.delete_function)
        delete_btn.grid(row=0, column=2)
        
        reset_btn=Button(btn_frame, text= "Reset" ,width=16 , font=("times new roman" ,13, "bold"),bg="blue",fg="white",command=self.reset_data)
        reset_btn.grid(row=0, column=3)
        
        btn_frame1=Frame(class_Student_frame, bd=2, relief=RIDGE, bg ="white")
        btn_frame1.place(x=0  ,y=235, width=715, height=35)
        
        take_photo_btn=Button(btn_frame1, text= "Take Photo Sample" ,width=33, font= ("times new roman" ,13, "bold"),bg="blue",fg="white",command=self.generate_dataset)
        take_photo_btn.grid(row=0, column=0)
        
        update_photo_btn=Button(btn_frame1, text= "update Photo Sample" ,width=33, font= ("times new roman" ,13, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0, column=1)
        
        
        
        
        
        
        
        
        
        
        
        # right Label Frame
        right_frame = LabelFrame(main_framee,bd=2,bg="white",relief=RIDGE,text="Student details", font=("times new roman",12,"bold"))
        right_frame.place(x=710,y=10,width=660,height=580)
        
        img_right=Image.open(r"D:\AI Ln\face_recognition system\college_images\b1.png")     
        img_right=img_right.resize((720,180),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=670,height=130)
        
        
        # ======seeach system=======
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System", font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=650,height=70)
        
        search_label=Label(search_frame, text= "Search By:", font=("times new roman",13, "bold"),bg="white",fg="red")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)    
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=8)
        search_combo["values"]=("Select ","Roll no","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)   
        
        search_entry=ttk.Entry (search_frame, width=18, font=("times new roman" ,13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)        
        
        search_btn=Button(search_frame, text= "Search" , width=11, font=("times new roman" ,13, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0, column=3,padx=3)
        
        showAll_btn=Button(search_frame, text= "Show All" ,width=11 , font=("times new roman" ,13, "bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0, column=4,padx=3)
        
        
        
        
        
        # ======table frame=======
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210 ,width=650,height=250)
        
        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame, column= ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)



        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #self.student_table.column("dep",width=100)

        
        # ===============================function decration=================================
        
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
            # server = 'NGUYEN-ANH-QUAN\ANHQUANHAV' 
            # database = 'face_recognizer' 
            # username = 'sa' 
            # password = 'Aq20/9/2004' 
            
            # conn = pymssql.connect(server, username, password, database)
            # cursor = conn.cursor()
            
                cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
                my_cursor = cnxn.cursor()
                
                my_cursor.execute("insert into student values( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? )",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()

                                                                                                            ))
                cnxn.commit()
                self.fetch_data()
                cnxn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
                
                
                
                
                
                
                
    #=======================fetch data=================================
    def fetch_data(self):
        try:
            cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
            my_cursor = cnxn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                clean_row = [str(item) for item in i]  # Convert all elements to strings
                self.student_table.insert("", END, values=clean_row)

            cnxn.commit()
            cnxn.close()
        except Exception as e:
            print("Error fetching data:", e)
            
    # def fetch_data(self):
    #     cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
    #     my_cursor = cnxn.cursor()
    #     my_cursor.execute("select * from student")
    #     data=my_cursor.fetchall()
        
    #     if len(data) !=0:
    #         self.student_table.delete(*self.student_table.get_children())
    #         for i in data:
    #             self.student_table.insert("",END,values=i)
    #         cnxn.commit()
    #     cnxn.close()

        
        
    # =============================get cursor==========================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        #cleaning data 
        #cleaned_data = [str(item).replace("'", "").replace(",", "").replace("(", "") for item in data]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),       
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),



    #==========================================update fuction============================================
    def update_fuction(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
                    my_cursor = cnxn.cursor()
                    my_cursor.execute("update student set Dep=?,Course=?,Year=?,Semester=?,Name=?,Division=?,Roll=?,Gender=?,Dob=?,Email=?,Phone=?,Address=?,Teacher=?,PhotoSample=? where Student_id=?",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.va_std_id.get() 
                        
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfylly update compaleted",parent=self.root)
                cnxn.commit()
                self.fetch_data()
                cnxn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
                
                
    #              delete function
    def delete_function(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student", parent=self.root)
                if delete>0:
                    cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
                    my_cursor = cnxn.cursor()
                    sql="delete from student where Student_id=?"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                    
                    cnxn.commit()  # Commit the deletion
                    cnxn.close()
                    
                    self.fetch_data()
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete","Successfully delete student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    
    
    
    
    # reset 
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self. var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

        
        
        
    # ==============================Generate data set or take a photo smaples==========================================
    def generate_dataset (self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
                my_cursor = cnxn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                student_id = int(self.va_std_id.get())  # Lấy giá trị Student_id từ giao diện
                my_cursor.execute("update student set Dep=?,Course=?,Year=?,Semester=?,Name=?,Division=?,Roll=?,Gender=?,Dob=?,Email=?,Phone=?,Address=?,Teacher=?,PhotoSample=? where Student_id=?",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        # self.va_std_id.get()==id+1 
                                                                                                                                                                                                        student_id  
                                                                                                                                                                                                    ))
                cnxn.commit()  # Commit the deletion
                self.fetch_data()
                self.reset_data()
                cnxn.close()

                
                # Load predifiend data in face frontals from opencv 
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3 
                    #minium Neighbor = 5 
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                
                while True: 
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(440,440))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=f"D:/AI Ln/face_recognition system/data/user.{student_id}.{img_id}.jpg" 
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    
                    
                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)






       
       
       
       

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 
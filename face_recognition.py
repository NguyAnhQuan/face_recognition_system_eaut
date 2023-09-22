from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pyodbc as pyo
import os
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime



class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Pannel")
        
        #title section
        title_lb1 = Label(self.root,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\AI Ln\face_recognition system\college_images\02.png")#image left
        img_top=img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=650,height=700)

        # backgorund image 
        bg1=Image.open(r"D:\AI Ln\face_recognition system\college_images\03.png")#image right
        bg1=bg1.resize((950,800),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=650,y=55,width=950,height=700)


        

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_b1_1 = Button(bg_img,text="Face Recognition",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white", command=self.face_recog)
        std_b1_1.place(x=380,y=625,width=200,height=40)
        
        
        
    #=====================Attendance===================

    def mark_attendance(self,d,n,r):
        with open("DiemDanh.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((d not in name_list)) and ((n not in name_list)) and ((r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{d}, {n}, {r}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                cnxn = pyo.connect(driver='{ODBC Driver 17 for SQL Server}', host='NGUYEN-ANH-QUAN\ANHQUANHAV', database='face_recognizer', trusted_connection='yes')
                my_cursor = cnxn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                

                if confidence > 77:
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    

                coord=[x,y,w,y]
            
            return coord    


    #     #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("D:/AI Ln/face_recognition system/classifiler.xml")

        video_Cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_Cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        video_Cap.release()
        cv2.destroyAllWindows()     
 



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
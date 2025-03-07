from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        
        lbl_title = Label(
          self.root,
          text='EMPLOYEE MANAGEMENT SYSTEM',
          font=('times new roman', 37, 'bold'),   
          fg='darkblue',
          bg='white'
        )
        lbl_title.place(x=0, y=0, relwidth=1.0, height=50)
        
        #Image Frame
        img_logo=Image.open('images/logo-1.jpg')
        img_logo = img_logo.resize((50, 50), Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        
        left_margin = 250
        self.logo.place(x=20 + left_margin, y=0, width=50, height=50)
        
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)
        
        # 1st Logo
        img1 = Image.open('images/p1.png')
        img1 = img1.resize((540, 160), Image.LANCZOS) 
        self.photo1 = ImageTk.PhotoImage(img1) 

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)
        
        
        # 2st Logo
        img2 = Image.open('images/p2.png')
        img2 = img2.resize((540, 160), Image.LANCZOS) 
        self.photo2 = ImageTk.PhotoImage(img2) 

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)
        
      
        # 3st Logo
        img3 = Image.open('images/p3.png')
        img3 = img3.resize((540, 160), Image.LANCZOS) 
        self.photo3 = ImageTk.PhotoImage(img3) 

        self.img_3 = Label(img_frame, image=self.photo1)
        self.img_3.place(x=1000, y=0, width=540, height=160)
        
        # main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=215, width=1500, height=560)

        # upper Frame
        upper_frame = LabelFrame(Main_frame, relief=RIDGE, bg='white', text='Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)
        
        # down Frame
        down_frame = LabelFrame(Main_frame, relief=RIDGE, bg='white', text='Employee Information Table', font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()        
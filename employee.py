from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        lbl_title = Label(
            self.root,
            text="EMPLOYEE MANAGEMENT SYSTEM",
            font=("times new roman", 37, "bold"),
            fg="darkblue",
            bg="white",
        )
        lbl_title.place(x=0, y=0, relwidth=1.0, height=50)

        # Image Frame
        img_logo = Image.open("images/logo-1.jpg")
        img_logo = img_logo.resize((50, 50), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)

        left_margin = 250
        self.logo.place(x=20 + left_margin, y=0, width=50, height=50)

        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        img_frame.place(x=0, y=50, width=1530, height=160)

        # 1st Logo
        img1 = Image.open("images/p1.png")
        img1 = img1.resize((540, 160), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)

        # 2st Logo
        img2 = Image.open("images/p2.png")
        img2 = img2.resize((540, 160), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)

        # 3st Logo
        img3 = Image.open("images/p3.png")
        img3 = img3.resize((540, 160), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo1)
        self.img_3.place(x=1000, y=0, width=540, height=160)

        # main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Main_frame.place(x=10, y=215, width=1500, height=560)

        # upper Frame
        upper_frame = LabelFrame(
            Main_frame,
            relief=RIDGE,
            bg="white",
            text="Employee Information",
            font=("times new roman", 11, "bold"),
            fg="red",
        )
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # Labels and Enter fields
        lbl_dep = Label(
            upper_frame, text="Department", font=("arial", 11, "bold"), bg="white"
        )
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(
            upper_frame,
            font=("arial", 12, "bold"),
            width=17,
            state="readonly",
            cursor="hand2",
        )
        combo_dep["value"] = (
            "Select Department",
            "HR",
            "Software Engineer",
            "Manager",
            "Sales",
            "Marketing",
            "Finance",
            "Data Science",
            "Product Management",
            "Customer Support",
            "Quality Assurance",
        )
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # name
        lbl_name = Label(
            upper_frame, font=("arial", 12, "bold"), text="Name:", bg="white"
        )
        lbl_name.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_name.grid(row=0, column=3, padx=2, pady=7)

        # lbl_Designition
        lbl_Designition = Label(
            upper_frame, font=("arial", 12, "bold"), text="Designition:", bg="white"
        )
        lbl_Designition.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_Designition = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_Designition.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # Email
        lbl_email = Label(
            upper_frame, font=("arial", 12, "bold"), text="Email:", bg="white"
        )
        lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=2)

        txt_email = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_email.grid(row=1, column=3, padx=2, pady=7)

        # Address
        lbl_adderss = Label(
            upper_frame, font=("arial", 12, "bold"), text="Address:", bg="white"
        )
        lbl_adderss.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_adderss = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_adderss.grid(row=2, column=1, padx=2, pady=7)

        # married
        lbl_merried_status = Label(
            upper_frame, font=("arial", 12, "bold"), text="Married Status:", bg="white"
        )
        lbl_merried_status.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        com_txt_merried = ttk.Combobox(
            upper_frame,
            state="readonly",
            width=20,
            font=("arial", 11, "bold"),
            cursor="hand2",
        )
        com_txt_merried["value"] = ("Merried", "Unmarried")
        com_txt_merried.current(0)
        com_txt_merried.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Dob
        lbl_dob = Label(
            upper_frame, font=("arial", 12, "bold"), text="DOB:", bg="white"
        )
        lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_dob = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_dob.grid(row=3, column=1, padx=2, pady=7)

        # Doj
        lbl_doj = Label(
            upper_frame, font=("arial", 12, "bold"), text="DOJ:", bg="white"
        )
        lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_doj = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_doj.grid(row=3, column=3, padx=2, pady=7)

        # Id Proof
        com_txt_proof = ttk.Combobox(
            upper_frame,
            state="readonly",
            font=("arial", 12, "bold"),
            width=22,
            cursor="hand2",
        )
        com_txt_proof["values"] = (
            "Select ID Proof",
            "PAN CARD",
            "ADHAR CARD",
            "DRIVING LICENSE",
            "PASSPORT",
        )
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_proof = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_proof.grid(row=4, column=1, padx=2, pady=7)

        # gender
        lbl_gender = Label(
            upper_frame, font=("arial", 12, "bold"), text="Gender:", bg="white"
        )
        lbl_gender.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        com_txt_gender = ttk.Combobox(
            upper_frame,
            state="readonly",
            font=("arial", 12, "bold"),
            width=18,
            cursor="hand2",
        )

        com_txt_gender["values"] = ("Male", "Female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # phone
        lbl_phone = Label(
            upper_frame, font=("arial", 12, "bold"), text="Phone No:", bg="white"
        )
        lbl_phone.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_phone = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_phone.grid(row=0, column=5, padx=2, pady=7)

        # country
        lbl_country = Label(
            upper_frame, font=("arial", 12, "bold"), text="Country:", bg="white"
        )
        lbl_country.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_country = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_country.grid(row=1, column=5, padx=2, pady=7)

        # CTC
        lbl_ctc = Label(
            upper_frame, font=("arial", 12, "bold"), text="Salary(CTC):", bg="white"
        )
        lbl_ctc.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        txt_ctc = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        txt_ctc.grid(row=2, column=5, padx=2, pady=7)

        # Profile img
        img_mask = Image.open("images/saurabh.jpg")
        img_mask = img_mask.resize((200, 220), Image.LANCZOS)
        self.photomask = ImageTk.PhotoImage(img_mask)

        self.img_mask = Label(
            upper_frame, image=self.photomask
        )  # Corrected lebal to Label
        self.img_mask.place(x=1025, y=0, width=200, height=220)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=1290, y=10, width=170, height=210)

        btn_add = Button(
            button_frame,
            text="Save",
            font=("arial", 15, "bold"),
            width=13,
            bg="blue",
            fg="white",
            cursor="hand2",
        )
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update = Button(
            button_frame,
            text="Update",
            font=("arial", 15, "bold"),
            width=13,
            bg="blue",
            fg="white",
            cursor="hand2",
        )
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(
            button_frame,
            text="Delete",
            font=("arial", 15, "bold"),
            width=13,
            bg="blue",
            fg="white",
            cursor="hand2",
        )
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_clear = Button(
            button_frame,
            text="Clear",
            font=("arial", 15, "bold"),
            width=13,
            bg="blue",
            fg="white",
            cursor="hand2",
        )
        btn_clear.grid(row=3, column=0, padx=1, pady=5)

        # down Frame
        down_frame = LabelFrame(
            Main_frame,
            relief=RIDGE,
            bg="white",
            text="Employee Information Table",
            font=("times new roman", 11, "bold"),
            fg="red",
        )
        down_frame.place(x=10, y=280, width=1480, height=270)

        # Search Frame
        search_frame = LabelFrame(
            down_frame,
            relief=RIDGE,
            bg="white",
            text="Search Employee Information",
            font=("times new roman", 11, "bold"),
            fg="red",
        )
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(
            search_frame,
            relief=RIDGE,
            bg="white",
            text="Search By:",
            font=("times new roman", 11, "bold"),
            fg="red",
        )
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # search
        com_txt_search = ttk.Combobox(
            search_frame,
            state="readonly",
            font=("arial", 12, "bold"),
            width=18,
            cursor="hand2",
        )
        com_txt_search["values"] = ("Select Option", "Phone", "id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        txt_search = ttk.Entry(search_frame, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(
            search_frame, text="Search", font=("arial", 11, "bold"), width=14, bg="blue"
        )
        btn_search.grid(row=0, column=3, padx=5)

        btn_ShowAll = Button(
            search_frame,
            text="Show All",
            font=("arial", 11, "bold"),
            width=14,
            bg="blue",
        )
        btn_ShowAll.grid(row=0, column=4, padx=5)

        stayhome = Label(
            search_frame,
            text="Protect Yourself, Protect Others",
            font=("times new roman", 30, "bold"),
            fg="red",
        )
        stayhome.place(x=780, y=0, width=600, height=30)

        # ========================== Employee Table =========================
        # Table Frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "name",
                "email",
                "address",
                "married",
                "dob",
                "doj",
                "idProofcom",
                "idProof",
                "gender",
                "phone",
                "country",
                "salary",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        # Configure Column Headers
        self.employee_table.heading("dep", text="Department")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("married", text="Married")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("doj", text="DOJ")
        self.employee_table.heading("idProofcom", text="ID Proof Type")
        self.employee_table.heading("idProof", text="ID Proof")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("phone", text="Phone")
        self.employee_table.heading("country", text="Country")
        self.employee_table.heading("salary", text="Salary")

        # Configure Column Widths
        self.employee_table.column("#0", width=0, stretch=NO)
        for col in self.employee_table["columns"]:
            self.employee_table.column(col, anchor=W, width=100)

        # Alternate Row Colors
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 10, "bold"))
        style.configure("Treeview", rowheight=25)
        style.configure(
            "Treeview",
            background="#D3D3D3",
            foreground="black",
            fieldbackground="#D3D3D3",
        )
        style.map("Treeview", background=[("alternate", "#E8E8E8")])

        self.employee_table.pack(fill=BOTH, expand=1)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()

from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:

    def __init__(self, root):

        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #============variables=================
        self.var_ref = StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address= StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number= StringVar()


        
        

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("timesnewroman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)



        img2=Image.open(r"logo2.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("timesnewroman",12,"bold"),padx = 2)
        labelframeleft.place(x=5,y=50,width = 425, height = 490)

        lbl_cust_ref= Label(labelframeleft,text = "Customer Ref",font=("timesnewroman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("timesnewroman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)


        #======cust name==================================================

        cname= Label(labelframeleft,font =("arial",12,"bold"),text = "Customer Name:",padx=2,pady= 6)
        cname.grid(row=1, column=0,sticky= W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width = 29)
        txtcname.grid(row=1, column=1)


        #=======================mother name =====================================
        lblmname= Label(labelframeleft, font=("arial",12,"bold"),text="Mother Name:", padx=2, pady=6)
        lblmname.grid(row=2,column=0,sticky= W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width = 29)
        txtmname.grid(row=2,column=1)



        #======================= gender==========================================

        label_gender= Label(labelframeleft,font =("arial",12,"bold"),text = " Gender:",padx =2,pady = 6)
        label_gender.grid(row=3,column=0,sticky= W)

        combo_gender = ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width = 27,state="readonly")
        combo_gender["value"]= ("male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        #================post code================================================
        lblpostCode= Label(labelframeleft,font =("arial",12,"bold"),text = "PostCode:",padx =2,pady = 6)
        lblpostCode.grid(row=4,column=0,sticky= W)
        txtpostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width = 29)
        txtpostCode.grid(row=4,column=1)

        #====================mobile number==========================================

        lblMobile= Label(labelframeleft,font =("arial",12,"bold"),text = "Mobile:",padx =2,pady = 6)
        lblMobile.grid(row=5,column=0,sticky= W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width = 29)
        txtMobile.grid(row=5,column=1)




        #====================Email ID==========================================

        lblEmail= Label(labelframeleft,font =("arial",12,"bold"),text = "Email:",padx =2,pady = 6)
        lblEmail.grid(row=6,column=0,sticky= W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width = 29)
        txtEmail.grid(row=6,column=1)

        #================Nationality===========================================

        lblNationality= Label(labelframeleft,font =("arial",12,"bold"),text = "Nationality:",padx =2,pady = 6)
        lblNationality.grid(row=7,column=0,sticky= W)


        combo_Nationality = ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width = 27,state="readonly")
        combo_Nationality["value"]= ("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column =1)

        #====================ID proof==========================================

        lblIdProof= Label(labelframeleft,font =("arial",12,"bold"),text = "IdProof:",padx =2,pady = 6)
        lblIdProof.grid(row=8,column=0,sticky= W)

        combo_id = ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width = 27,state="readonly")
        combo_id["value"]= ("Aadhar Card","Driving License"," Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column =1)

        #=======================ID Number=========================================

        lblIdNumber= Label(labelframeleft,font =("arial",12,"bold"),text = "IdNumber:",padx =2,pady = 6)
        lblIdNumber.grid(row=9,column=0,sticky= W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width = 29)
        txtIdNumber.grid(row=9,column=1)

        #=================Address==================================================

        lblAddress= Label(labelframeleft,font =("arial",12,"bold"),text = "Address:",padx =2,pady = 6)
        lblAddress.grid(row=10,column=0,sticky= W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width = 29)
        txtAddress.grid(row=10,column=1)


        #========== BUTTON FRAME ==============
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 400, width = 412, height = 40)

        
        
        btnAdd = Button(btn_frame, text = "Add",command=self.add_data,font = (" arial", 11, "bold"), bg = "black", fg = "gold", width= 10)
        btnAdd.grid(row = 0, column = 0, padx = 1)
        
        btnUpdate = Button(btn_frame, text = "Update",command=self.update,font = (" arial", 11, "bold"), bg = "black", fg = "gold", width= 10)
        btnUpdate.grid(row = 0, column = 1, padx = 1)

        btnDelete = Button(btn_frame, text = "Delete",command=self.mDelete,font = (" arial", 11, "bold"), bg = "black", fg = "gold", width= 10)
        btnDelete.grid(row = 0, column = 2, padx = 1)

        btnReset = Button(btn_frame, text = "Reset",command=self.reset,font = (" arial", 11, "bold"), bg = "black", fg = "gold", width= 10)
        btnReset.grid(row = 0, column = 3, padx = 1)
         

    #====================TABLE FRAME=====================================================

        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and Search System",font=("timesnewroman",12,"bold"),padx = 2)
        Table_Frame.place(x=435,y=50,width = 860, height = 490)

        lblSearchBy= Label(Table_Frame,font =("arial",12,"bold"),text = "Search By: ",bg = "red" ,fg ="white")
        lblSearchBy.grid(row= 0,column=0,sticky= W)

        self.search_var=StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",13,"bold"),width = 27,state="readonly")
        combo_Search["value"]= ("mobile", "ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column =1)

        self.txt_search = StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width = 29)
        txtSearch.grid(row= 0,column=2)

        btnSearch = Button(Table_Frame, text = "Search",command=self.search,font = (" arial", 11, "bold"), bg = "black", fg = "gold", width= 10)
        btnSearch.grid(row = 0, column = 3, padx = 1)

        btnShowAll = Button(Table_Frame, text = "Show All",command=self.fetch_data,font = (" arial", 11, "bold"), bg = "black", fg = "gold", width= 10)
        btnShowAll.grid(row = 0, column = 4, padx = 1)



#======================SHOW DATA TABLE====================================================
        details_table = Frame( Table_Frame, bd = 2, relief = RIDGE)
        details_table.place(x = 0, y = 50, width = 860, height = 350)

        scroll_x=ttk.Scrollbar(details_table,orient = HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient = VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ref", "name", "mother", "gender","post","mobile",
                                                   "email","nationality","idProof","idNumber","address"),xscrollcommand = scroll_x.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        scroll_x.config(command =self.Cust_Details_Table.xview)
        scroll_y.config(command =self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref",text = "refer no.")
        self.Cust_Details_Table.heading("Name",text = "Name")
        self.Cust_Details_Table.heading("Mother", text="Mother Name")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("PostCode", text="PostCode")
        self.Cust_Details_Table.heading("Mobile", text="Mobile")
        self.Cust_Details_Table.heading("Email", text="Email")
        self.Cust_Details_Table.heading("Nationality", text="Nationality")
        self.Cust_Details_Table.heading("IdProof", text="Id Proof")
        self.Cust_Details_Table.heading("Idnumber", text="Id Number")
        self.Cust_Details_Table.heading("Address", text="Address")


        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor())
        self.fetch_data()

    def add_data(self): #database connectivity
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"),(
                                                                           self.var_ref.get(),
                                                                           self.var_cust_name.get(),
                                                                           self.var_mother.get(),
                                                                           self.var_gender.get(),
                                                                           self.var_post.get(),
                                                                           self.var_mobile.get(),
                                                                           self.var_email.get(),
                                                                           self.var_nationality.get(),
                                                                           self.var_id_proof.get(),
                                                                           self.var_id_number.get(),
                                                                           self.var_address.get()
                                                                          ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete((* self.Cust_Details_Table.get_children()))
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content("values")

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error",parent=self.root)
        else:

            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("Update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,Idnumber=%s,Address=%s where Ref=%s",(

                                                                                                                                self.var_cust_name.get(),
                                                                                                                                self.var_mother.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_post.get(),
                                                                                                                                self.var_mobile.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_nationality.get(),
                                                                                                                                self.var_id_proof.get(),
                                                                                                                                self.var_id_number.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_ref.get()

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="management")
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()




if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()

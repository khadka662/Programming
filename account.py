import tkinter.messagebox
from PIL import ImageTk ,Image
from tkinter import *
import sqlite3
def reg():
    root = Tk()

    root.title("PING PONG")
    root.iconbitmap('ping.ico')
    root.configure(bg='#12dbba')

    root.geometry("360x380")
    root.resizable(width=False, height=False)
    # Creating a database
    database = sqlite3.connect('registration.db')
    # Creating Cursor
    cursor = database.cursor()
    '''
    #Creating Table
    cursor.execute("""Create Table Information (
    full_name text,
    username text,
    password text,
    confirm_password text 
    )""")
    '''

    def info():
        # Creating a database
        database = sqlite3.connect('registration.db')
        # Creating Cursor
        cursor = database.cursor()
        # Inserting Data Into Table
        cursor.execute("Insert Into Information Values (:name, :username, :password,:confirm_password)",
                       {
                           'name': name_entry.get(),
                           'username': username_entry.get(),
                           'password': password_entry.get(),
                           'confirm_password': confirm_password_entry.get()
                       })
        cursor.execute("Select "
                       "*,oid From Information")
        data = cursor.fetchall()
        print(data)
        # Commiting Changes
        database.commit()


    # create a label
    my_label = Label(root)
    my_label.place(x=0,y=0,relwidth=1,relheight=1)

    # add something to the top of our image
    my_text = Label(root, text=" CREATE AN ACCOUNT", font=("helvetica", 15))
    my_text.grid(row=0, column=2, pady=20)
    # create a frame
    my_frame = Frame(root, bg='#12dbba')
    my_frame.grid(row=1, column=2)

    # creating label
    Full_name = Label(my_frame, text='FullName')
    Full_name.grid(row=1, column=1)

    user_name = Label(my_frame, text='UserName', bd=2)
    user_name.grid(row=2, column=1)
    password = Label(my_frame, text='Password', bd=4)
    password.grid(row=3, column=1)
    confirm_password = Label(my_frame, text='confirm password', bd=2)
    confirm_password.grid(row=4, column=1)

    # creating textbox
    name_entry = Entry(my_frame, width=30, bg='#fafcfb', borderwidth=5, font=" aerial 10 bold")
    name_entry.grid(row=1, column=2, padx=10, pady=10)
    username_entry = Entry(my_frame, width=30, bg='#fafcfb', borderwidth=5, font=" aerial 10 bold")
    username_entry.grid(row=2, column=2, padx=10, pady=10)
    password_entry = Entry(my_frame, width=30, bg="#fafcfb", bd=4, borderwidth=5, font=" aerial 10 bold", show="*")
    password_entry.grid(row=3, column=2, padx=10, pady=10)
    confirm_password_entry = Entry(my_frame, width=30, bg="#fafcfb", bd=4, borderwidth=5, font=" aerial 10 bold",
                                   show="*")
    confirm_password_entry.grid(row=4, column=2, padx=20, pady=20)

    def register():
        if name_entry.get() == "" and username_entry.get() == "" and password_entry.get() == "" and confirm_password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username,Password Correctly")
        elif name_entry.get() == "" and username_entry.get() == "" and password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username,Password Correctly")
        elif name_entry.get() == "" and username_entry.get() == "" and confirm_password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username,Confirm Password Correctly")
        elif name_entry.get() == "" and username_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Username Correctly")
        elif username_entry.get() == "" and password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Username,Password Correctly")
        elif name_entry.get() == "" and password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Name,Password Correctly")
        elif password_entry.get() == "" and confirm_password_entry.get() == "":
            tkinter.messagebox.showinfo("INVALID DETAILS", "Please Enter Your Password Correctly")
        elif password_entry.get() != confirm_password_entry.get():
            tkinter.messagebox.showinfo("INVALID PASSWORD", "Please Enter Your Password Correctly!")
        elif name_entry.get() == "":
            tkinter.messagebox.showinfo("NAME EMPTY", "Please Enter Your Name Correctly!")
        elif username_entry.get() == "":
            tkinter.messagebox.showinfo("USERNAME EMPTY", "Please Enter Your Username Correctly!")
        else:
            # Creating a database
            database = sqlite3.connect('registration.db')
            # Creating Cursor
            cursor = database.cursor()
            # Inserting Data Into Table
            cursor.execute("Insert Into Information Values (:name, :username, :password,:confirm_password)",
                           {
                               'name': name_entry.get(),
                               'username': username_entry.get(),
                               'password': password_entry.get(),
                               'confirm_password': confirm_password_entry.get()
                           })
            cursor.execute("Select *,oid From Information")
            data = cursor.fetchall()
            print(data)
            tkinter.messagebox.showinfo("REGISTRATION SUCCESSFUL", "Login Now To Enjoy The Game")
            # Commiting Changes
            database.commit()

    # Creating Register Button
    register_button = Button(root, text="REGISTER", bd=3, bg="black", fg="white", font=("arial", 15, 'bold'), width=10,
                             height=1, command=register)
    register_button.grid(row=7, column=2, padx=10, pady=10)
    '''
    # Creating Label
    my_label = Label(root, image=bg)
    my_label.place(x=0, y=0,  relwidth=1, relheight=1)
    # Creating Account
    my_house = Label(root, text="Create An Account", Font=("arial", 40, "bold")
    my_house.pack(pady=40)
    '''
    # Commiting Changes
    database.commit()
    mainloop()
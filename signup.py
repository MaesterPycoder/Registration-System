# Importing Modules
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os, datetime, time
from tkcalendar import DateEntry
import mysql.connector

def main():
    # Root Window
    win = tk.Tk()
    win.title("Pythonics SignUp")
    win.geometry('600x400')
    win.resizable(False, False)
    win.wm_iconbitmap('bird.ico')
    imageBG = ImageTk.PhotoImage(Image.open('loginBG.jpg'))
    canvas = tk.Canvas(win, width = 600, height = 400)
    canvas.create_image(0, 0, anchor = "nw", image = imageBG)
    canvas.place_configure(x = 0, y = 0)

    # Variables Declartaion
    name = tk.StringVar()
    emailid = tk.StringVar()
    mobile = tk.StringVar(value = '+91')
    dob = tk.StringVar()
    gender = tk.StringVar()
    password = tk.StringVar()
    reTypePass = tk.StringVar()
    mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Sss@23052000",
                database = "pythonics"
                )
    mycursor = mydb.cursor()

    # SignUp Functions
    def signUp():
        Name_ = name.get()
        mail = emailid.get()
        mob = mobile.get()
        pass_ = password.get()
        gend = gender.get()
        date_ = dob.get()
        repass = reTypePass.get()
        mycursor.execute("select max(id) from account_info")
        id_ = mycursor.fetchone()[0] + 1
        if pass_ != "" and gend !="" and dob.get() != "" and repass != "" and Name_ != "" and mail != "" and mob != "":
            lst = mail.split("@")
            if lst[-1] not in ["gmail.com","yahoo.com","outlook.com","protonmail.com","mail.com",
                                "yandex.com","lycos.com","tutanota.com","zoho.com","icloud.com",
                                "aol.com","gmx.com"]:
                                messagebox.showinfo(title = "Alert!",message = "Invalid mail")
                                emailid.set("")
            mycursor.execute(f"select EmailId from account_info where EmailId = '{mail}'")
            if mycursor.fetchone():
                messagebox.showinfo(title = "Alert!", message = "This Email Already Registered.")
                emailid.set("")
            if len(mob) != 13 and mob[1:].isalnum():
                messagebox.showinfo(title = "Alert!", message = "Enter Valid Number")
                mobile.set("+91")
            mycursor.execute(f"select mobile from account_info where mobile = '{mob}'")
            if mycursor.fetchone():
                messagebox.showinfo(title = "Alert!", message = "This Mobile Number Already Registered.")
                mobile.set("+91")
            if pass_ == repass :
                mycursor.execute(f"insert account_info values({id_},'{Name_}','{mail}','{date_}','{gend}','{mob}','{pass_}')")
                mydb.commit()
                mycursor.close()
                mydb.close()
                messagebox.showinfo(title = 'OK', message = 'Sign Up Successful \n Login Now')
                LogIn()
            else:
                messagebox.showinfo(title = "Alert", message = 'Re-Entered Password is wrong.')
                reTypePass.set("")
        else:
            messagebox.showinfo(title = "Alert!", message = "Enter all credentials")
    def LogIn():
        win.destroy()
        import login
        login.main()

    # Layout Modelling
    label1 = tk.Label(win, text = '*Pythonics Account SignUp*', fg = 'Maroon', bg = 'Lawn Green', font = 'Helvetica 15 bold')
    label1.place(x = 160, y = 10)

    label2 = tk.Label(win, text = 'Enter Credentials:', fg = "Gold", bg = 'Black', font = 'Helvetica 12 bold')
    label2.place(x = 10, y = 40)

    label3 = tk.Label(win, text = 'Name            :', fg = "Gold", bg = 'Black', font = 'Helvetica 12 bold')
    label3.place(x = 100, y = 65)
    nameField = tk.Entry(win, textvariable = name, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12 bold')
    nameField.place(x = 210, y = 65, width = 300)
    nameField.focus()

    label3 = tk.Label(win, text = 'Email-id        :', fg = "Gold", bg = 'Black', font = 'Helvetica 12 bold')
    label3.place(x = 100, y = 95)
    mailField = tk.Entry(win, textvariable = emailid, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12 bold')
    mailField.place(x = 210, y = 95, width = 300)

    label4 = tk.Label(win, text = 'Date of birth:', fg = "Gold", bg = 'Black', font = 'Helvetica 12 bold')
    label4.place(x = 100, y = 125)
    dobField = DateEntry(win, textvariable = dob, width = 12, background = 'Blue', foreground = 'white', borderwidth = 2)
    dobField.place(x = 210, y = 125, width = 200)

    label5 = tk.Label(win, text = 'Gender         :', fg = "Gold", bg = 'Black', font = 'Helvetica 12 bold')
    label5.place(x = 100, y = 155)
    gender.set("Male")
    gender_male = tk.Radiobutton(win, text = "Male", fg = "Black", bg = "Light Cyan", value = "Male", width = "5", variable = gender, font = 'Helvetica 11 bold')
    gender_male.place(x = "210", y = "155")
    gender_female = tk.Radiobutton(win, text = "Female", fg = "Black", bg = "Light Cyan", width = "5", value = "Female", variable = gender, font = 'Helvetica 11 bold')
    gender_female.place(x = "290", y = "155")
    gender_others = tk.Radiobutton(win, text = "Others", fg = "Black", bg = "Light Cyan", width = "5", value = "Others", variable = gender, font = 'Helvetica 11 bold')
    gender_others.place(x = "370", y = "155")

    label6 = tk.Label(win, text = 'MobileNo.    :', fg = "Gold", bg = 'Black', font = 'Helvetica 12 bold')
    label6.place(x = 100, y = 190)
    mobileField = tk.Entry(win, textvariable = mobile, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12 bold')
    mobileField.place(x = 210, y = 190, width = 200)

    label7 = tk.Label(win, text = 'Password    :', fg = "Gold", bg = 'Black', font = 'Helvetica 12 bold')
    label7.place(x = 100, y = 220)
    keyField = tk.Entry(win, show = "*", textvariable = password, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 14 bold')
    keyField.place(x = 210, y = 220, width = 200)

    label8 = tk.Label(win, text = 'Re-enter          :\n Password', fg = "Gold", bg = 'Black', font = 'Helvetica 10 bold')
    label8.place(x = 100, y = 250)
    rekeyField = tk.Entry(win, show = "*", textvariable = reTypePass, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 14 bold')
    rekeyField.place(x = 210, y = 250, width = 200)

    signUpB = tk.Button(win, text = "Sign Up", fg = 'Dark Green', bg = 'Turquoise',activebackground = "Green2", width = 10, height = 1, command = signUp, font = 'Helvetica 10 bold')
    signUpB.place(x = 250, y = 290)

    tk.Label(win, text = time.ctime(), fg = 'Gold', bg = 'Black', font = 'Helvetica 9 bold').place_configure(x = 440, y = 10)
    year = str(datetime.date.today())
    tk.Label(win, text = "SSS UNION", fg = "Gold", bg = 'Black', font = 'Helvetica 10 bold').place_configure(x = 250, y = 350)
    tk.Label(win, text = "© "+year[:4]+" All Rights Reserved", fg = "Gold", bg = 'Black', font = 'Helvetica 10 bold').place_configure(x = 200, y = 370)

    win.mainloop()
if __name__=='__main__':
    main()

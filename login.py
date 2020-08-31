# Importing Modules
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time, datetime, mysql.connector

def main():
    # Login Window
    root = tk.Tk()
    root.title('Pythonics Login')
    root.geometry('600x400')
    root.resizable(False, False)
    root.wm_iconbitmap('bird.ico')
    imageBG = ImageTk.PhotoImage(Image.open('loginBG.jpg'))
    canvas = tk.Canvas(root, width = 600, height = 400)
    canvas.create_image(0, 0, anchor = "nw", image = imageBG)
    canvas.place_configure(x = 0, y = 0)

    # Declaring Variables
    userEmail = tk.StringVar()
    Password = tk.StringVar()
    mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Sss@23052000",
                database = "pythonics"
                )
    mycursor = mydb.cursor()

    # Identity Check Functions
    def clearData():
        userEmail.set("")
        Password.set("")

    def login():
        user = userEmail.get()
        key = Password.get()
        if user == "" or key == "":
            messagebox.showinfo(title = "Sign in-Alert!", message="Enter Creddentilals \n To signed in")
        else:
            mycursor.execute(f"select EmailId from account_info where EmailId='{user}'")
            if mycursor.fetchall():
                mycursor.execute(f"select password from account_info where EmailId = '{user}'")
                __result = mycursor.fetchall()
                __Security_key = __result[0][0]
                if key == __Security_key:
                    ############################################################# Link Main File Here ###########################################################
                    messagebox.showinfo(title = "Access Granted", message="You are successfully signed in")
                    root.destroy()
                    # Shift this Above calling Function
                    # Put Entry Apllication call here
                    ############################################################# Link Main File Here ###########################################################
                else:
                    messagebox.showinfo(title = "Alert!", message="Invalid credentials")
                    clearData()
            else:
                messagebox.showinfo(title = "Alert!", message="Invalid credentials")
                clearData()

    def signUp():
        root.destroy()
        import signup
        signup.main()

    # Login Window
    label1 = tk.Label(root, text = '*Pythonics Account Login*', fg = 'Maroon', bg = 'Lawn Green', font = 'Helvetica 15 bold')
    label1.place(x = 150, y = 20)

    label2 = tk.Label(root, text = 'Enter Credentials:', fg = 'Gold', bg = 'Black', font = 'Helvetica 15 bold')
    label2.place(x = 80, y = 80)

    label3 = tk.Label(root, text = 'UserMail :', fg = 'Gold', bg = 'Black', font = 'Helvetica 12 bold')
    label3.place(x = 60, y = 130)

    user_field = tk.Entry(root, textvariable = userEmail, font = 'Helvetica 15', bg = 'light cyan', width = 25) 
    user_field.place(x = 150, y = 127)
    user_field.focus()

    label4 = tk.Label(root, text = 'Password :', fg = 'Gold', bg = 'Black', font = 'Helvetica 12 bold')
    label4.place(x = 50, y = 187)

    key_field = tk.Entry(root, show = "*", textvariable = Password, font = 'Helvetica 15 bold', bg = 'light cyan') 
    key_field.place(x = 150, y = 180)

    loginB = tk.Button(root, text = "Login", activebackground = "Green1", fg = 'Dark Green', bg = 'Turquoise', width = 10, height = 1, command = login, font = 'Helvetica 10 bold')
    loginB.place(x = 200, y = 230)

    tk.Label(root, text = time.ctime(), fg = 'Gold', bg = 'Black', font = 'Helvetica 10 bold').place(x = 430, y = 10)
    
    year = str(datetime.date.today())
    tk.Label(root, text = "SSS UNION", fg = "White", bg = 'Black', font = 'Helvetica 10 bold').place(x = 250, y = 340)
    tk.Label(root, text = "© "+year[:4]+" All Rights Reserved", fg = "White", bg = 'Black', font = 'Helvetica 10 bold').place(x = 200, y = 360)
    tk.Label(root, text = "@ Not a member ? ,", fg = "Gold", bg = 'Black', font = 'Helvetica 10 bold').place(x = 230, y = 300)
    tk.Button(root, text = "SignUp", command = signUp, activebackground = "Green2", fg = "Maroon", bg = "Light Green").place(x = 370, y = 295)

    root.mainloop()
if __name__ == '__main__':
    main()

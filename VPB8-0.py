from Tkinter import *
import ttk
import tkFont
import tkMessageBox
import time
from datetime import datetime

# Global Variables
Name = ""
Password = ""
Gender = ""
FirstTime = "True"
SkinColor = ""
EyeColor = ""
Hair = ""
Clothes = ""
SavingGoal = 0.0
CurrentBalance = 0.0
DeadLine = ""
Score = 0

# Global function
def UpdateDatabase(str_new):
    output = []
    database = open("Data/Data.db", "r")
    # Go through the database and find the matching line
    for line in iter(database):
        # Get the first element separated by a tab
        elements = line.rsplit("\t")
        name = elements[0]
        if line != "\n":
            if Name != name:
                # Save all lines into output except the one with the same name
                output.append(line)

    database.close()
    output.append("\n")
    output.append(str_new)
    # Open the database and rewrite the database with the new output
    database = open("Data/Data.db", "w")
    database.writelines(output)
    database.close()

# Classes
class MenuPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        # Set up grid for widgets
        self.grid()
        self.resizable(False, False)

        # Create custom fonts
        self.font_title = tkFont.Font(family = "Helvetica", size = 64, weight = "bold")
        self.font_button = tkFont.Font(family = "Tahoma", size = 20)

        # Create title text for main menu
        label_title = Label(self, text = "Virtual\nPiggy Bank", bg = "black", fg = "white",font=self.font_title)
        label_title.grid(sticky = E + W, pady = 10)

        # Create buttons for the menu
        button_login = Button(text = "Log In", font = self.font_button, command = self.login)
        button_register = Button(text = "Register", font = self.font_button, command = self.register)
        button_about = Button(text = "About", font = self.font_button, command = self.about)

        button_login.grid(row = 1, pady = 10)
        button_register.grid(row = 2, pady = 10)
        button_about.grid(row = 3, pady = 10)
        self.centralize_window()
    def about(self):
        tkMessageBox.showinfo("About", "This is a Virtual Piggy Bank.\nCreated by MMU students, S33M$ L3G!T")

    def login(self):
        self.destroy()
        # Go to Log In windows
        LoginPage(None).title("Login")

    def register(self):
        self.destroy()
        RegisterPage(None).title("New User")

class RegisterPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        # Set up grid for widgets
        self.grid()
        self.resizable(False, False)

        #border_avatar = Frame(self, relief=RIDGE, borderwidth=2)-TESTING PURPOSES
        #border_avatar.place(relx=0, rely=0, anchor=NW)


        # Create custom fonts
        self.font_label = tkFont.Font(family = "Tahoma", size = 11)

        # Labels
        self.label_avatar = Label(text = "Avatar:", font = self.font_label)
        self.label_name = Label(text = "Username:", font = self.font_label)
        self.label_password = Label(text = "Password:", font = self.font_label)
        self.label_gender = Label(text = "Gender:", font = self.font_label)
        self.label_skinColor = Label(text = "Skin Color:", font = self.font_label)
        self.label_eyeColor = Label(text = "Eye Color:", font = self.font_label)
        self.label_hair = Label(text = "Hair:", font = self.font_label)
        self.label_clothes = Label(text = "Clothes:", font = self.font_label)

        # Buttons
        self.button_register = Button(text = "Register", command = self.register)
        self.button_cancel = Button(text = "Cancel", command = self.cancel)

        # Load body images
        self.img_Body = []
        self.img_Body.append(PhotoImage(file = "resources/body_white.gif"))
        self.img_Body.append(PhotoImage(file = "resources/body_brown.gif"))
        self.img_Body.append(PhotoImage(file = "resources/body_black.gif"))

        # Load eyes images
        self.img_Eyes = []
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_male_blue.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_male_green.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_male_purple.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_female_blue.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_female_green.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_female_purple.gif"))

        # Load clothes images
        self.img_Clothes = []
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_male_1.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_male_2.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_male_3.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_female_1.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_female_2.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_female_3.gif"))

        # Load hair images
        self.img_Hair = []
        self.img_Hair.append(PhotoImage(file = "resources/hair_male_1.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_male_2.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_male_3.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_female_1.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_female_2.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_female_3.gif"))

        # Canvas
        self.canvas_avatar = Canvas(width = 144, height = 144)

        # Layers
        self.layer_body = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Body[0])
        self.layer_eyes = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Eyes[0])
        self.layer_clothes = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Clothes[0])
        self.layer_hair = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Hair[0])

        # Entries
        self.str_name = StringVar()
        self.entry_name = Entry(textvariable = self.str_name)
        self.str_name.set("Username")

        self.str_password = StringVar()
        self.entry_password = Entry(textvariable = self.str_password, show="*")

        # Combo Boxes
        self.str_gender = StringVar()
        self.cbox_gender = ttk.Combobox(textvariable = self.str_gender, state = "readonly")
        self.cbox_gender["values"] = ("Male", "Female")
        self.cbox_gender.current(0)

        self.str_skinColor = StringVar()
        self.cbox_skinColor = ttk.Combobox(textvariable = self.str_skinColor, state = "readonly")
        self.cbox_skinColor["values"] = ("White", "Brown", "Black")
        self.cbox_skinColor.current(0)

        self.str_eyeColor = StringVar()
        self.cbox_eyeColor = ttk.Combobox(textvariable = self.str_eyeColor, state = "readonly")
        self.cbox_eyeColor["values"] = ("Blue", "Green", "Purple")
        self.cbox_eyeColor.current(0)

        self.str_hair = StringVar()
        self.cbox_hair = ttk.Combobox(textvariable = self.str_hair, state = "readonly")
        self.cbox_hair["values"] = ("Hair 1", "Hair 2", "Hair 3")
        self.cbox_hair.current(0)

        self.str_clothes = StringVar()
        self.cbox_clothes = ttk.Combobox(textvariable = self.str_clothes, state = "readonly")
        self.cbox_clothes["values"] = ("Clothes 1", "Clothes 2", "Clothes 3")
        self.cbox_clothes.current(0)

        # Layout widgets
        # First Column
        self.label_avatar.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.canvas_avatar.grid(row = 1, column = 0, padx = 5, pady = 5, rowspan = 4, columnspan = 2, sticky = W + E + N + S)
        self.label_name.grid(row = 5, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.entry_name.grid(row = 6, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = W + E)
        self.label_password.grid(row = 7, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = W)
        self.entry_password.grid(row = 8, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = W + E)
        self.button_register.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = W + E)
        self.button_cancel.grid(row = 9, column = 1, padx = 5, pady = 5, sticky = W + E)
        # Second Column
        self.label_gender.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = W)
        self.cbox_gender.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = W + E)
        self.label_skinColor.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = W)
        self.cbox_skinColor.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = W + E)
        self.label_eyeColor.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = W)
        self.cbox_eyeColor.grid(row = 5, column = 2, padx = 5, pady = 5, sticky = W + E)
        self.label_hair.grid(row = 6, column = 2, padx = 5, pady = 5, sticky = W)
        self.cbox_hair.grid(row = 7, column = 2, padx = 5, pady = 5, sticky = W + E)
        self.label_clothes.grid(row = 8, column = 2, padx = 5, pady = 5,  sticky = W)
        self.cbox_clothes.grid(row = 9, column = 2, padx = 5, pady = 5, sticky = W + E)

        #Update canvas
        self.updateImage()

    def updateImage(self):

        # Change skin color
        if self.str_skinColor.get() == "White":
            self.canvas_avatar.itemconfig(self.layer_body, image = self.img_Body[0])
        if self.str_skinColor.get() == "Brown":
            self.canvas_avatar.itemconfig(self.layer_body, image = self.img_Body[1])
        if self.str_skinColor.get() == "Black":
            self.canvas_avatar.itemconfig(self.layer_body, image = self.img_Body[2])

        # Change eye color, clothes and hair style based on gender
        if self.str_gender.get() == "Male":
            # Male eye color
            if self.str_eyeColor.get() == "Blue":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[0])
            if self.str_eyeColor.get() == "Green":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[1])
            if self.str_eyeColor.get() == "Purple":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[2])

            # Male clothes
            if self.str_clothes.get() == "Clothes 1":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[0])
            if self.str_clothes.get() == "Clothes 2":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[1])
            if self.str_clothes.get() == "Clothes 3":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[2])

            # Male hair
            if self.str_hair.get() == "Hair 1":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[0])
            if self.str_hair.get() == "Hair 2":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[1])
            if self.str_hair.get() == "Hair 3":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[2])

        elif self.str_gender.get() == "Female":
            # Female eye color
            if self.str_eyeColor.get() == "Blue":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[3])
            if self.str_eyeColor.get() == "Green":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[4])
            if self.str_eyeColor.get() == "Purple":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[5])

            # Female clothes
            if self.str_clothes.get() == "Clothes 1":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[3])
            if self.str_clothes.get() == "Clothes 2":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[4])
            if self.str_clothes.get() == "Clothes 3":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[5])

            # Female hair
            if self.str_hair.get() == "Hair 1":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[3])
            if self.str_hair.get() == "Hair 2":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[4])
            if self.str_hair.get() == "Hair 3":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[5])

        # Update the canvas every 0.1 seconds
        self.loop = self.after(100, self.updateImage)

        #Centralize register window
        self.centralize_window()

    def cancel(self):
        # Stop updating Image
        self.after_cancel(self.loop)
        # Destroy current windows
        self.destroy()
        MenuPage(None).title("Virtual Piggy Bank")

    def register(self):
        # Open/create database for reading and appending
        self.database = open("Data\Data.db", "a+")
        # Name is not taken by default
        self.nameTaken = False
        # Loop through the database to check if the username is taken
        for line in iter(self.database):
            # Get the first element separated by a tab
            self.elements = line.rsplit("\t")
            self.name = self.elements[0]
            if self.str_name.get() == self.name:
                self.nameTaken = True

        # Check name availability
        if self.nameTaken == True:
            tkMessageBox.showerror("Error!", "Username taken! Please try a different username.")
        # Check if password is empty
        elif self.str_password.get() == "":
            tkMessageBox.showerror("Error!", "Password cannot be empty!")
        else:
            # Write data into
            self.data = [self.str_name.get(), self.str_password.get(), self.str_gender.get(), "True", self.str_skinColor.get(), self.str_eyeColor.get(),
                        self.str_hair.get(), self.str_clothes.get(),"0.0", "0.0", "None", "0"]
            self.database.writelines("\n" + "\t".join(self.data))
            self.database.close()
            tkMessageBox.showinfo("Register Success!", self.str_name.get() + " has been registered!")
            self.destroy()
            MenuPage(None).title("Virtual Piggy Bank")


class LoginPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        # Set up grid for widgets
        self.grid()
        self.resizable(False, False)

        self.str_username = StringVar()
        self.str_password = StringVar()

        self.lbl_username = Label(text="Username :")
        self.lbl_password = Label(text="Password :")
        self.entry_username = Entry(textvariable = self.str_username)
        self.entry_username.focus_set()
        self.entry_password = Entry(textvariable = self.str_password ,show="*")
        self.btnLogin = Button(text="Login",command = self.Login)
        self.btnCancel = Button(text="Cancel", command=self.Cancel)

        # Display widgets
        self.lbl_username.grid(row=0,column=0,sticky=E)
        self.lbl_password.grid(row=1,column=0,sticky=E)
        self.entry_username.grid(row=0 ,column= 1)
        self.entry_password.grid(row=1, column =1)
        self.btnLogin.grid(pady=5,padx=5,row=2,column=1, sticky = W)
        self.btnCancel.grid(pady=5, padx=5,row=2,column=1, sticky = E)

        # Initialized login chances
        self.count = 2

        #Centralize login window
        self.centralize_window()


    def Login(self):
        # Using global variables
        global Name
        global Password
        global Gender
        global FirstTime
        global SkinColor
        global EyeColor
        global Hair
        global Clothes
        global SavingGoal
        global CurrentBalance
        global DeadLine
        global Score
        self.NameExist = False
        self.database = open("Data\Data.db", "r")
        for line in iter(self.database):
            # Get the first element separated by a tab
            self.elements = line.rsplit("\t")
            self.name = self.elements[0]
            if self.str_username.get() == self.name:
                self.NameExist = True
                self.password = self.elements[1]
                break
        self.database.close()
        if self.NameExist == False:
            tkMessageBox.showerror("Error", "Username Does Not Exist!")
            self.entry_username.focus_set()
            self.entry_username.selection_range(0, END)

        elif self.str_password.get() == self.password:
            Name = self.elements[0]
            Password = self.elements[1]
            Gender = self.elements[2]
            FirstTime = self.elements[3]
            SkinColor = self.elements[4]
            EyeColor = self.elements[5]
            Hair = self.elements[6]
            Clothes = self.elements[7]
            SavingGoal = self.elements[8]
            CurrentBalance = self.elements[9]
            DeadLine = self.elements[10]
            Score = self.elements[11]
            # Go to Set Target windows if first time user
            if FirstTime == "True":
                # After fisrt time logging in, FirstTime become False
                FirstTime = "False"
                # Preparing new string to be write into database
                self.newData = [Name, Password, Gender, FirstTime, SkinColor, EyeColor, Hair, Clothes, SavingGoal, CurrentBalance, DeadLine, Score]
                self.newString = ("\t".join(self.newData))
                # Update the database
                UpdateDatabase(self.newString)
                self.destroy()
                SetTargetPage(None).title("Virtual Piggy Bank")
            else:
                # Go to Main Program windows if not first time user
                self.destroy()
                MainProgramPage(None).title("Virtual Piggy Bank")

        else:
            # Every failed login attempt remove the attempt count by 1
            tkMessageBox.showwarning("Error", "Wrong password! \n(" + str(self.count) +
                                  " chance remaining)")
            self.entry_password.focus_set()
            self.entry_password.selection_range(0, END)
            if self.count == 0:
                tkMessageBox.showerror("Fail to login","You had failed to login with 3 attempts. The program will now close.")
                self.destroy()
            else:
                self.count = self.count - 1

    def Cancel(self):
        self.destroy()
        MenuPage(None).title("Virtual Piggy Bank")

class SetTargetPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        # Set up grid for widgets
        self.grid()
        self.resizable(False, False)
        self.TargetString = StringVar()
        self.TargetLab = Label(text="Target Amount (RM) : ", pady=10)
        self.TargetEnt = Entry(textvariable=self.TargetString)
        self.DateString = StringVar()
        self.DateLab = Label(text="Deadline(dd/mm/yy) : ", pady=10)
        self.DateEnt = Entry(textvariable=self.DateString)
        self.SubmitBut = Button(text="Submit", pady=10, command=self.CheckInput)

        # Position widgets
        self.TargetLab.grid(row=0, sticky=E)
        self.TargetEnt.grid(row=0, column=1)
        self.DateLab = Label(text="Deadline(dd/mm/yy): ", pady=10).grid(row=1, column=0, sticky=E)
        self.DateEnt.grid(row=1, column=1)
        self.SubmitBut.grid(row=2, columnspan=2)
        self.centralize_window()


    def CheckInput(self):

        # Initialize input condition
        self.isNumber = False
        self.isDateFormat = False
        self.isVaildDate = False

        # Check for date input format
        try:
            self.InputTarget = float(self.TargetString.get())
            self.isNumber = True

        except ValueError:
            # Print error message if wrong format
            self.TargetEnt.focus_set()
            self.TargetEnt.selection_range(0, END)
            tkMessageBox.showerror("Error!!!", "Must enter a number!")

        # Check for date input format
        try:
            self.inputDate = datetime.strptime(self.DateString.get(), "%d/%m/%y").date()
            # Get current date
            self.currentdate = datetime.today().date()
            self.datedifference = (self.inputDate - self.currentdate)
            self.isDateFormat = True
        except ValueError:
            tkMessageBox.showerror("Error!", "Date input must be in dd/mm/yy, eg. 30/11/16")
            self.DateEnt.focus_set()
            self.DateEnt.selection_range(0, END)

        # Check if date is at least one day after the current date
        if self.datedifference.days > 0:
            self.isValidDate = True
        else:
            tkMessageBox.showerror("Error!", "Date input must be at least one day after the current date!")
            self.DateEnt.focus_set()
            self.DateEnt.selection_range(0, END)


        if self.isValidDate == True and self.isNumber == True and self.isDateFormat == True:

            # Preparing new string to be write into database
            self.newData = [Name, Password, Gender, FirstTime, SkinColor, EyeColor, Hair, Clothes,
                            self.TargetString.get(), "0.0", self.DateString.get(), str(Score)]
            self.newString = ("\t".join(self.newData))
            # Update the database
            UpdateDatabase(self.newString)
            tkMessageBox.showinfo("Success",
                                  "You had successfully set your target!\nPlease login again to start using.")
            self.destroy()
            MenuPage(None).title("Virtual Piggy Bank")
        else:
            tkMessageBox.showerror("Error!", "Bad input!")
            self.isNumber = False
            self.isDateFormat = False
            self.isValidDate = False


class MainProgramPage(Tk):
    def __init__(self, parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def centralize_window(self):  # To centralize the window
        self.update_idletasks()  # refresh
        width = self.winfo_width()  # get screen width
        height = self.winfo_height()  # get screen height
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def initialize(self):
        # Set up grid for widgets
        self.grid()
        self.resizable(False,False)
        border1 = Frame(self, relief=SOLID, borderwidth=2)
        border1.place(relx=0.02, rely=0.19, anchor=NW)
        border2 = Frame(self,relief = SOLID, borderwidth=2)
        border2.place(relx=0.79 , rely=0.19, anchor=NW)

        # Create custom fonts
        self.font_label = tkFont.Font(family = "Tahoma", size = 12)
        self.font_bold = tkFont.Font(family = "Tahoma", size = 14, weight = "bold")
        self.font_info = tkFont.Font(family = "Tahoma", size = 10)

        # Load body images
        self.img_Body = []
        self.img_Body.append(PhotoImage(file = "resources/body_white.gif"))
        self.img_Body.append(PhotoImage(file = "resources/body_brown.gif"))
        self.img_Body.append(PhotoImage(file = "resources/body_black.gif"))

        # Load eyes images
        self.img_Eyes = []
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_male_blue.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_male_green.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_male_purple.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_female_blue.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_female_green.gif"))
        self.img_Eyes.append(PhotoImage(file = "resources/eyes_female_purple.gif"))

        # Load clothes images
        self.img_Clothes = []
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_male_1.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_male_2.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_male_3.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_female_1.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_female_2.gif"))
        self.img_Clothes.append(PhotoImage(file = "resources/clothes_female_3.gif"))

        # Load hair images
        self.img_Hair = []
        self.img_Hair.append(PhotoImage(file = "resources/hair_male_1.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_male_2.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_male_3.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_female_1.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_female_2.gif"))
        self.img_Hair.append(PhotoImage(file = "resources/hair_female_3.gif"))

        # Canvas
        self.canvas_avatar = Canvas(width = 144, height = 144)

        # Layers
        self.layer_body = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Body[0])
        self.layer_eyes = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Eyes[0])
        self.layer_clothes = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Clothes[0])
        self.layer_hair = self.canvas_avatar.create_image(0, 2, anchor = NW, image = self.img_Hair[0])

        # Date
        # Get current date as date object
        self.currentdate = datetime.today().date()
        # Convert current date into string object
        self.str_currentdate = self.currentdate.strftime('%m/%d/%Y')
        # Convert deadline string into date object
        self.date_deadline = datetime.strptime(DeadLine, "%d/%m/%y").date()
        # Calculate dayes left by subtracting current date with dead line (date object)
        self.daysleft = (self.date_deadline - self.currentdate).days
        self.label_date = Label(text =self.str_currentdate, font = self.font_bold)

        # Labels (Using borders)-LEFT
        self.label_biography = Label(text = "Biography").place(relx=0.115, rely=0.19,anchor=E)
        self.label_nameTitle = Label(border1,text = "Name:", font = self.font_label, justify = LEFT)
        self.label_name = Label(border1,text = Name, font = self.font_info)
        self.label_genderTitle = Label(border1,text = "Gender:", font = self.font_label, justify = LEFT)
        self.label_gender = Label(border1,text = Gender, font = self.font_info)
        self.label_targetTitle = Label(border1, text="Target:", font=self.font_label, justify=LEFT)
        self.label_target = Label(border1, text= SavingGoal)

        # Labels (Using borders)-RIGHT
        self.label_status = Label(text="Status").place(relx=0.97, rely=0.19, anchor=E)
        self.label_titleRewardScore = Label(border2, text="Reward Score:", font=self.font_label, justify=LEFT)
        self.int_rewardScore = int(int(self.daysleft) * int(float(SavingGoal)) / 10)
        self.label_rewardScore = Label(border2, text=self.int_rewardScore)
        self.label_titleCurrentBalance = Label(border2, text="Current Balance:", font=self.font_label, justify=LEFT)
        self.d_CurrentBalance = float(CurrentBalance)
        self.label_currentBalance = Label(border2, text=str(self.d_CurrentBalance))
        self.label_titleDaysLeft = Label(border2, text="Days Left:", font=self.font_label, justify=LEFT)
        self.label_daysLeft = Label(border2, text=self.daysleft)


        #Time
        self.label_time = Label(text = "" , font=self.font_bold)

        # Labels
        self.label_withdrawal = Label(text = "Withdrawal:", font = self.font_label)
        self.label_deposit = Label(text = "Deposit:", font = self.font_label)
        self.label_totalScoreTitle = Label(text = "Score : ", font =self.font_bold, justify = LEFT)
        self.int_totalScore = int(Score)
        self.label_totalScore = Label(text = self.int_totalScore, font = self.font_bold, justify = LEFT)
        self.blank_space = Label(text = "" )
        self.blank_space2 = Label(text= "")
        self.blank_spacebtm = Label(text = "")

        # Buttons
        self.advice_btn = Button(text="Advice", bg="grey", fg="black", justify=LEFT, command=self.advice)
        self.reset_btn = Button(text="Reset", bg="grey", fg="black", justify=LEFT, command = self.reset)
        self.deadline_label = Label(text="Deadline - " + DeadLine, font=self.font_bold, justify=LEFT)
        self.update_btn = Button(text = "Update", bg = "black",fg = "white", command = self.update)
        self.logout_btn = Button(text = "Logout",bg = "orange", fg = "black", command = self.logout)

        # Entries
        self.d_withdrawal = DoubleVar()
        self.entry_withdrawal = Entry(textvariable = self.d_withdrawal)

        self.d_deposit = DoubleVar()
        self.entry_deposit = Entry(textvariable = self.d_deposit)


        # Layout widgets (GRID)
        # Column 0
        self.label_totalScoreTitle.grid(row = 0, column = 0,padx = 5, pady = 5, sticky = W)
        self.label_totalScore.grid(row = 0, column = 1,padx = 5, pady = 5, sticky = W)
        self.blank_space.grid(row = 1, column = 1,padx = 5, pady = 5, sticky = W)
        self.blank_space2.grid(row=2, column=1, padx=5, pady=5, sticky= W)
        self.label_nameTitle.grid(row = 7, column = 1, padx = 5, pady = 5, sticky = W)
        self.label_name.grid(row = 8, column = 1, padx = 5, pady = 5, sticky = W)
        self.label_genderTitle.grid(row = 9, column = 1, padx = 5, pady = 5, sticky = W)
        self.label_gender.grid(row = 10, column = 1, padx = 5, pady = 5, sticky = W)
        self.label_targetTitle.grid(row = 11, column = 1 ,padx = 5 ,pady = 5, sticky = W)
        self.label_target.grid(row = 12, column = 1, padx = 5 , pady = 5 , sticky = W)
        self.blank_spacebtm.grid(row = 13, column = 1, padx = 5 , pady = 5 , sticky = W)

        # Column 1
        self.label_withdrawal.grid(row= 14, column=1, padx=5, pady=5, sticky=W)
        self.entry_withdrawal.grid(row = 15, column = 1, padx = 5, pady = 5, sticky = E + W)
        self.advice_btn.grid(row = 16, column = 1, padx = 5, pady = 5, sticky = E + W)
        # Column 2
        self.label_time.grid(row=0, column=2, padx=5, pady=5)
        self.canvas_avatar.grid(row=8, column=2, padx=5, pady=5, rowspan=4)
        self.update_btn.grid(row = 15, column = 2, padx = 5, pady = 5, sticky = E + W)
        self.logout_btn.grid(row = 16, column = 2, padx = 5, pady= 5, sticky = E + W)
        self.deadline_label.grid(row = 1, column = 2, padx = 5, pady= 5)
        # Column 3
        self.label_deposit.grid(row = 14, column = 3, padx = 5, pady = 5, sticky = W)
        self.entry_deposit.grid(row = 15, column = 3, padx = 5, pady = 5, sticky = E + W)
        self.reset_btn.grid(row = 16, column = 3, padx = 5, pady = 5, sticky = E + W)
        # Column 4
        self.label_date.grid(row = 0 , column = 4 , padx = 5 , pady = 5, sticky = W)
        self.label_titleRewardScore.grid(row = 7 , column = 4 , padx = 5 , pady = 5, sticky = W)
        self.label_rewardScore.grid(row = 8 , column = 4 , padx = 5 , pady = 5, sticky = W)
        self.label_titleCurrentBalance.grid(row = 9 , column = 4 , padx = 5 , pady = 5, sticky = W)
        self.label_currentBalance.grid(row = 10 , column = 4 , padx = 5 , pady = 5, sticky = W)
        self.label_titleDaysLeft.grid(row = 11 , column = 4 , padx = 5 , pady = 5, sticky = W)
        self.label_daysLeft.grid(row = 12 , column = 4 , padx = 5 , pady = 5, sticky = W)
        self.renderAvatar()
        self.tick()
        self.centralize_window()

    def logout(self):
        # Preparing new string to be write into database
        self.newData = [Name, Password, Gender, FirstTime, SkinColor, EyeColor, Hair, Clothes,
                        str(SavingGoal), str(self.d_CurrentBalance), DeadLine, str(self.int_totalScore)]
        self.newString = ("\t".join(self.newData))
        UpdateDatabase(self.newString)
        self.destroy()
        self.after_cancel(self.loop)
        MenuPage(None).title("Virtual Piggy Bank")

    def tick(self):
        # Update time label
        self.str_time = time.strftime('%H:%M:%S')
        self.label_time.config(text = self.str_time)
        # Update date label
        self.str_currentdate = self.currentdate.strftime('%m/%d/%Y')
        # Check if the deadline is reached and goal is not yet reached
        if self.daysleft <= 0 and float(self.d_CurrentBalance) < float(SavingGoal):
            tkMessageBox.showerror("Mission Failed!", "You did not achieve your goal within the given time!")
            # Reset saving goals
            self.destroy()
            SetTarget(None).title("Set Target")
        # Loop this function every seconds
        self.loop = self.after(1000,self.tick)

    def reset(self):
        # Reset saving goals
        self.destroy()
        # Stop the loop
        self.after_cancel(self.loop)
        SetTargetPage(None).title("Set Target")

    def update(self):
        global Score
        global CurrentBalance
        # Check for target input format
        try:
            self.d_CurrentBalance = self.d_CurrentBalance - self.d_withdrawal.get() + self.d_deposit.get()
            self.label_currentBalance.config(text = str(self.d_CurrentBalance))
            if self.d_CurrentBalance >= float(SavingGoal):
                self.int_totalScore = self.int_totalScore + self.int_rewardScore
                self.label_totalScore.config(text = self.int_totalScore)
                tkMessageBox.showinfo ("Congratulations!","You have reached your goal!")
                # Preparing new string to be write into database
                self.newData = [Name, Password, Gender, FirstTime, SkinColor, EyeColor, Hair, Clothes,
                                "0.0", "0.0", "None", str(self.int_totalScore)]
                self.newString = ("\t".join(self.newData))
                # Update the database
                UpdateDatabase(self.newString)
                # Uodate the global variables
                Score = str(self.int_totalScore)
                # Reset saving goals
                self.destroy()
                # Stop the loop
                self.after_cancel(self.loop)
                SetTargetPage(None).title("Set Target")

        except ValueError:
            # Print error message if wrong format
            tkMessageBox.showerror("Error", "Must enter a number!")

    def advice(self):
        # Round up to 2 decimal places
        self.moneyperday = float("{0:.2f}".format(float((float(SavingGoal) - float(CurrentBalance)) / (self.date_deadline - self.currentdate).days)))
        tkMessageBox.showinfo("Advice", "For the next " + str(self.daysleft)  + " day(s) you need to save RM" + str(self.moneyperday) + " per day.")

    def renderAvatar(self):

        # Display skin color
        if SkinColor == "White":
            self.canvas_avatar.itemconfig(self.layer_body, image = self.img_Body[0])
        if SkinColor == "Brown":
            self.canvas_avatar.itemconfig(self.layer_body, image = self.img_Body[1])
        if SkinColor == "Black":
            self.canvas_avatar.itemconfig(self.layer_body, image = self.img_Body[2])

        # Display eye color, clothes and hair style based on gender
        if Gender == "Male":
            # Male eye color
            if EyeColor == "Blue":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[0])
            if EyeColor == "Green":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[1])
            if EyeColor == "Purple":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[2])

            # Male clothes
            if Clothes == "Clothes 1":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[0])
            if Clothes == "Clothes 2":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[1])
            if Clothes == "Clothes 3":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[2])

            # Male hair
            if Hair == "Hair 1":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[0])
            if Hair == "Hair 2":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[1])
            if Hair == "Hair 3":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[2])

        elif Gender == "Female":
            # Female eye color
            if EyeColor == "Blue":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[3])
            if EyeColor == "Green":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[4])
            if EyeColor == "Purple":
                self.canvas_avatar.itemconfig(self.layer_eyes, image = self.img_Eyes[5])

            # Female clothes
            if Clothes == "Clothes 1":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[3])
            if Clothes == "Clothes 2":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[4])
            if Clothes == "Clothes 3":
                self.canvas_avatar.itemconfig(self.layer_clothes, image = self.img_Clothes[5])

            # Female hair
            if Hair == "Hair 1":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[3])
            if Hair == "Hair 2":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[4])
            if Hair == "Hair 3":
                self.canvas_avatar.itemconfig(self.layer_hair, image = self.img_Hair[5])


if __name__ == "__main__":
    app = MenuPage(None)
    app.title("Virtual Piggy Bank")
    app.mainloop()

# Import Stuff
from tkinter import TclError

# Import Widgets
import ttkbootstrap as ttk

# Import Custom Widgets
from kanwar import MessageBox

# Import Security
from kanwar import authenticate

# Import database
from kanwar import database

# Import Tabs
from kanwar import Attendance
from kanwar import Department
from kanwar import Student
#from kanwar.test import Test # as it's included by reuslt tab
from kanwar import Result
from kanwar import Staff
from kanwar import Report
from kanwar import Session

########################################################################
# Peform Authentication or not
Authenticate = False

########################################################################
# Themse for GUI
themes = ['united', 'cosmo','yeti', 'clam', 'solar', 'pulse', 'vista',
         'winnative', 'xpnative', 'default', 'litera',
          'darkly', 'lumen', 'alt', 'journal',
          'classic', 'superhero', 'minty', 'flatly',
           'cyborg', 'sandstone','vapor','morph']

########################################################################
# Free For all or not

########################################################################
# Making GUI Object
style = ttk.Style(theme=themes[0])

root = style.master
root.focus()
root.title("Kanwar Adnan")
padx,pady = 10,100
root.geometry("940x620+100+80")
root.minsize(940,620)
style.configure('New.TNotebook',tabposition='nw')
style.configure('TNotebook.Tab',background='white')

########################################################################
# Frames
mainframe = ttk.Frame(root)
mainframe.pack(fill='both', expand=1)

########################################################################
# Notebook for tabs
nb = ttk.Notebook(mainframe)
nb.pack(fill='both', expand=1,side='left')

########################################################################
# Creating Pages
page1 = ttk.Frame(nb)
page2_ = ttk.Frame(nb)

########################################################################
# Adding pages to notebook1
nb.add(page1 , text= 'Take Attendance ')
nb.add(page2_ , text= 'Data Management')

########################################################################
# Tabs to notebook1
# Attendance Tab
attendanceTab = Attendance(root,page1)

########################################################################
# Notebook2
nb2 = ttk.Notebook(page2_,style='New.TNotebook')
nb2.pack(fill='both',expand=1)

########################################################################
# creatings pages for notebook2
page2 = ttk.Frame(nb2)  # CLASS
page3 = ttk.Frame(nb2)  # STUDENTS
page5 = ttk.Frame(nb2)  # USERS
page6 = ttk.Frame(nb2)  # USERS
page7 = ttk.Frame(nb2)  # RESULTS
page8 = ttk.Frame(nb2)  # REPORTS

########################################################################
# Adding pages to notebook
nb2.add(page2, text = 'Classes')
nb2.add(page3, text = 'Students')
nb2.add(page7, text = 'Results')
nb2.add(page5, text = 'Staff')
nb2.add(page8, text = 'Reports')
nb2.add(page6, text = 'Sessions')

########################################################################
# Adding tabs to notebook2

# CLASS TAB
classTab = Department(root,page2)

# Student Tab
studentTab = Student(root,page3)

# Result Tab and Test Tab
resultTab = Result(root,page7)

# Staff Tab
staffTab = Staff(root,page5)

# Report Tab
reportTab = Report(root,page8)

# Session Tab
sessionTab = Session(root,page6)

###########################################################
# Making Tabs change their position
def makeTabChange():
    def reorder(event):
        try:
            index = nb.index(f"@{event.x},{event.y}")
            nb.insert(index, child=nb.select())

        except TclError:
            pass


    def reorder2(event):
        try:
            index = nb2.index(f"@{event.x},{event.y}")
            nb2.insert(index, child=nb2.select())

        except TclError:
            pass

    nb2.bind("<B1-Motion>", reorder2)
    nb2.bind("<B1-Motion>", reorder)
    nb.bind("<B1-Motion>", reorder)

###########################################################
# Allowing to change positions of tabs
makeTabChange()

###########################################################
# Creating DB
database.createdb()    

###############################################################
# Returns the size of window
# For Debug
def Size(event):
    print(root.winfo_height(),root.winfo_width())
root.bind('<Alt-Return>',Size)

###############################################################
# On Quit Options It may lead you to login and signup
def quit_me():
    op = MessageBox("Confirm",'Press the desired button ! ',
                    b1='Exit',b2='Cancel',b3='Login')

    if op.choice=='Login':
        attendanceTab.reset_page1()
        authenticate.Login_System(root=root,nb=nb)
    elif op.choice=='Exit':
        root.quit()
        root.destroy()

###########################################################
# On Quit Options
def quit_me_2():
    op = MessageBox("Confirm",'Do you really wish to exit?',
                    b1='Yes',b2='No')

    if op.choice=='Yes':
        root.quit()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", quit_me)

###############################################################
# Unbinds short keys
def unbinder():
    try:
        root.unbind('<Return>')
        root.unbind('<Control-o>')
        root.unbind('<Control-u>')
        root.unbind('<Control-d>')
        root.unbind('<Control-r>')
        root.unbind('<Control-s>')
        root.unbind('<Control-f>')
    except:
        pass

###############################################################
# Binds Short keys
def assign_commands_nb(event=None):
    tab = nb.index(nb.select())
    unbinder()
    if tab==0:
        unbinder()
        root.bind("<Return>",attendanceTab.add_attendance)
        root.bind("<Control-u>",attendanceTab.update_attendance)
        root.bind("<Control-d>",attendanceTab.delete_attendance)
        root.bind("<Control-r>",attendanceTab.reset_page1)
    elif tab==1:
        unbinder()
        root.bind("<Return>",classTab.add_class)
        root.bind("<Control-u>",classTab.update_class)
        root.bind("<Control-d>",classTab.delete_class)
        root.bind("<Control-r>",classTab.reset_class)
        root.bind("<Control-s>",classTab.export_class)
        root.bind("<Control-f>",lambda  e : classTab.txt_search.focus_set())

nb.bind("<<NotebookTabChanged>>",lambda e : assign_commands_nb(e))

###############################################################
# Bind short keys for the coming tabs
def assign_commands_nb2(event=None):
    tab = nb2.index(nb2.select())

    if tab==0 or tab=="":
        root.bind("<Return>",classTab.add_class)
        root.bind("<Control-u>",classTab.update_class)
        root.bind("<Control-d>",classTab.delete_class)
        root.bind("<Control-r>",classTab.reset_class)
        root.bind("<Control-s>",classTab.export_class)
        root.bind("<Control-f>",lambda  e : classTab.txt_search.focus_set())
    if tab==1:
        root.bind("<Return>",studentTab.add_student)
        root.bind("<Control-u>",studentTab.update_student)
        root.bind("<Control-d>",studentTab.delete_student)
        root.bind("<Control-r>",studentTab.reset_student)
        root.bind("<Control-s>",studentTab.export_student)
        root.bind("<Control-o>",studentTab.sort_student)
        root.bind("<Control-f>",lambda e : studentTab.txt_search_page3.focus_set())
    if tab==2:
        root.bind("<Return>",resultTab.add_result)
        root.bind("<Control-u>",resultTab.update_result)
        root.bind("<Control-d>",resultTab.delete_result)
        root.bind("<Control-r>",resultTab.reset_result)
        root.bind("<Control-s>",resultTab.export_result)
        root.bind("<Control-o>",resultTab.sort_result)
        root.bind("<Control-f>",lambda  e : resultTab.txt_search_page7.focus_set())
    if tab==3:
        root.bind("<Return>",staffTab.add_user)
        root.bind("<Control-u>",staffTab.update_user)
        root.bind("<Control-d>",staffTab.delete_user)
        root.bind("<Control-r>",staffTab.reset_user)
        root.bind("<Control-s>",staffTab.export_user)
        root.bind("<Control-o>",staffTab.sort_user)
        root.bind("<Control-f>",lambda  e : staffTab.txt_search_page5.focus_set())
    if tab==5:
        unbinder()

nb2.bind("<<NotebookTabChanged>>",lambda e : assign_commands_nb2(e))

###############################################################
# Checking previous logins if found logged in = true then it will open that
authenticate.check_previous_Login(root,nb)

###########################################################
# Unbind for the first time
unbinder()

###########################################################
# binding the first pages's keys
root.bind("<Return>",attendanceTab.add_attendance)
root.bind("<Control-u>",attendanceTab.update_attendance)
root.bind("<Control-d>",attendanceTab.delete_attendance)
root.bind("<Control-r>",attendanceTab.reset_page1)

###########################################################
# Hiding tabs under construction
nb2.hide(4)
nb2.hide(5) 

###########################################################
# Checking perform authtenication or not
if Authenticate:
    authenticate.Login_System(root,nb)
    if authenticate.LOGGER !='Admin':
        nb.tab(1,state='disabled')
    else:
        try:
            nb.tab(1,state='normal')
        except:
            pass
###########################################################

# Running the GUI
root.mainloop()
###########################################################

"""
    All Rights Are reserved to Kanwar Adnan.
    Contact : kanwaradnanrajput@gmail.com
    for source code
"""

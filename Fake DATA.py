#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install Faker


# In[2]:


#import Faker
from faker import Faker
# create an instance of faker
fake = Faker()
# print fake name
print("Name: ", fake.name())
# create an instance of faker
# in hindi
fake1 = Faker("hi_IN")
# print fake name in hindi
print("Name1: ", fake1.name())


# In[ ]:


from tkinter import *
from faker import Faker
root = Tk()
fake = Faker()
root.title("Fake data generator")
root.geometry("955x445")
frame1 = Frame(root, bg="gold2", relief=GROOVE, borderwidth=5)
frame1.place(x=40, y=40)
frame2 = Frame(root, bg="black", relief=GROOVE, borderwidth=5)
frame2.place(x=250, y=20)
def change():
    if var1.get()==True:
        checkbtn1.config(fg='red3')
    else:
        checkbtn1.config(fg='black')
    if var2.get()==True:
        checkbtn2.config(fg='red3')
    else:
        checkbtn2.config(fg='black')
    if var3.get()==True:
        checkbtn3.config(fg='red3')
    else:
        checkbtn3.config(fg='black')
    if var4.get()==True:
        checkbtn4.config(fg='red3')
    else:
        checkbtn4.config(fg='black')
    if var5.get()==True:
        checkbtn5.config(fg='red3')
    else:
        checkbtn5.config(fg='black')
  
# create label
label = Label(frame1, text="Select the options \n to display their \n related fake data:", font=("haveltica 15 underline bold"), bg="gold2")
label.pack(side=TOP, pady=15, anchor='n')
#createing check buttons
var1 = IntVar()
checkbtn1=Checkbutton(frame1, text='Name', variable=var1, font=("haveltica 14 bold"), bg="gold2", command=change)
checkbtn1.pack(side=TOP, padx=40, anchor='w') 
var2 = IntVar()
checkbtn2=Checkbutton(frame1, text='Email', variable=var2, font=("haveltica 14 bold"), bg="gold2", command=change)
checkbtn2.pack(side=TOP, padx=40, anchor='w') 
var3 = IntVar()
checkbtn3=Checkbutton(frame1, text='Country', variable=var3, font=("haveltica 14 bold"), bg="gold2", command=change)
checkbtn3.pack(side=TOP, padx=40, anchor='w')  
var4 = IntVar()
checkbtn4=Checkbutton(frame1, text='Text', variable=var4, font=("haveltica 14 bold"), bg="gold2", command=change)
checkbtn4.pack(side=TOP, padx=40, anchor='w')  
var5 = IntVar()
checkbtn5=Checkbutton(frame1, text='URL', variable=var5, font=("haveltica 14 bold"), bg="gold2", command=change)
checkbtn5.pack(side=TOP, padx=40, anchor='w') 
def display():
    list.delete(0,4)
    if var1.get()==True:
        list.insert(0, f"Name: {fake.name()}")
    if var2.get()==True:
        list.insert(1, f"Email: {fake.email()}")
    if var3.get()==True:
        list.insert(2, f"Country: {fake.country()}")
    if var4.get()==True:
        list.insert(3, f"Text: {fake.text()}")
    if var5.get()==True:
        list.insert(4, f"URL: {fake.url()}")
btn = Button(frame1, text="Display Data", font=("haveltica 15 bold"), bg="yellow2", command=display)
btn.pack(side=BOTTOM, pady=15, anchor='n')
list = Listbox(frame2, font=("haveltica 15 bold"), width=60, height=15)
hscroll_bar = Scrollbar(frame2, orient='horizontal')
vscroll_bar = Scrollbar(frame2, orient='vertical')
list.focus_set()
hscroll_bar.pack(side = BOTTOM,fill =X)
vscroll_bar.pack(side = RIGHT,fill =Y)
list.pack(fill = BOTH, expand = True)
hscroll_bar.config(command = list.xview)
vscroll_bar.config(command = list.yview)
list.config(xscrollcommand = hscroll_bar.set, yscrollcommand = vscroll_bar.set)
root.mainloop()


# In[ ]:





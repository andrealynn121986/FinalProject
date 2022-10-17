
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window=Tk()
window.minsize(900,700)




#opening 1st image file

image3 = Image.open("C:\SDEV140\onion.png")

#resizing the image
image3 = image3.resize((150, 150), Image.Resampling.LANCZOS)

test3 = ImageTk.PhotoImage(image3)

#opening 2nd image file

image1 = Image.open("C:\SDEV140\hot-dogs.jpg")

#resizing the image

image1 = image1.resize((150, 150), Image.Resampling.LANCZOS)

test = ImageTk.PhotoImage(image1)

#opening 3rd image file

image2 = Image.open("C:\SDEV140\diet2.png")

#resizing the image

image2 = image2.resize((150, 150), Image.Resampling.LANCZOS)

test2 = ImageTk.PhotoImage(image2)

#setting 1st image in label l3


l3=tk.Label(window,image=test)

l3.place(x=250,y=10)#position the label

#setting 2nd image in label l4

l4=tk.Label(window,image=test2)

l4.place(x=400,y=10)#position the label

#setting 3rd image in Lable 15

l5=tk.Label(window,image=test3)

l5.place(x=50,y=10)#position the label





def calculate():
  
      #Where you calculate all the items
    dic = {'Fries': [w1,3.99],
           'hot dog': [w2,4.99],
           'Coke': [w3,1.99],
           'Chili Topping': [w4,.75],
           'Ketchup': [w5, .25],
           'Onion Rings': [w6,3.99],
           'Chocolate': [w7, 2.99],
           'Vanilla Cone':[w8,2.99],
           'Diet Coke': [w9,1.99]}
                           
    total = 0
    for key, val in dic.items():
        if val[0].get() != "":
            total += int(val[0].get())*val[1]
           
    window.after(1000, calculate)
        
#where to set up the child window 
    def open_popup():
        top= Toplevel(window)
        top.title("Total")
        content=(str(total))
        top.geometry("750x250")
        Label(top,text="Your total is",
              font=('times 28')).pack()
        Label(top,text=content,
              
               font=('times 28')).pack()
        
    #creating the button   
    Button(window, text= "Your Total Bill", command= open_popup).place(x=570,y=340)
    
   
    
  
   
      
#creating the title label 

label8 = Label(window,
               text="Bubba's Dogs",
               font="times 36 bold")
label8.place(x=540, y=20)

  
  #This is where you label the items 

  
label10 = Label(window,
                text="Fries 3.99",
                font="times 18")
label10.place(x=200, y=200)
  
w1 = Entry(window)
w1.place(x=200, y=230)
  
label11 = Label(window, text="Hot Dog 4.99",
                font="times 18")
label11.place(x=200, y=260)
  
w2 = Entry(window)
w2.place(x=200, y=300)
  
label12 = Label(window, text="Coke 1.99",
                font="times 18")
label12.place(x=200, y=340)
  
w3 = Entry(window)
w3.place(x=200, y=380)


label13 = Label(window,
                text="Chilli Topping .75",
                font="times 18")
label13.place(x=390, y=260)
  
w4 = Entry(window)
w4.place(x=390, y=300)
  
label14 = Label(window,
                text="Ketchup .25",
                font="times 18")
label14.place(x=590, y=260)
  
w5 = Entry(window)
w5.place(x=590, y=300)
  
label15 = Label(window,
                text="Onion Rings 3.99",
                font="times 18")
      
label15.place(x=390, y=200)
  
w6 = Entry(window)
w6.place(x=390, y=230)
label19 = Label(window,
                text="Diet Coke 1.99",
                font="times 18")
  
label19.place(x=390, y=340)
  
w9 = Entry(window)
w9.place(x=390, y=380)
   
label17 = Label(window,
                text="Chocolate 1.99",
                font="times 18")
  
label17.place(x=200, y=410)
  
w7 = Entry(window)
w7.place(x=200, y=450)
label18 = Label(window,
                text="Vanilla Cone 1.99",
                font="times 18")
  
label18.place(x=390, y=410)
  
w8 = Entry(window)
w8.place(x=390, y=450) 
  
#creating the exit button
b3 = tk.Button(window,text="exit",command=window.destroy,font=("Arial", 15))

b3.place(x=100,y=460)
#ending the program
window.after(1000, calculate)
window.mainloop()

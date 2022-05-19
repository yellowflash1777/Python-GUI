#importing library
import tkinter as tk
 
#creating a window 
win=tk.Tk()

#giving title
win.title("Demo")

#defining geometry
win.geometry("960x540")

#initilazing text we want to display
my_text=tk.Label(win,text="Hey Pack") 
my_text1=tk.Label(win,text="hey Grid")
my_text2=tk.Label(win,text="hey ") 


#pack method
my_text.pack(anchor="ne")#by default if will display on center top

#grid method
#my_text.grid(row=90,column=188)

#place method
#my_text2.place(x=120,y=150)

#adding buttons
#creating function for button command
def button_fun():
    #print("hey")
    my_button_label=tk.Label(win,text="hey")
    my_button_label.pack(anchor="nw")

my_button=tk.Button(win,text="Print Hey",command=button_fun)
my_button.pack(anchor="ne")

#creating entry
my_entry=tk.Entry(win,font=('ariel',20))
my_entry.pack()

def entry_fun():
    my_info=my_entry.get()
    my_text4=tk.Label(win,text=f'The enterd text is : {my_info}')
    my_text4.pack()

my_button3=tk.Button(win,text="Submit",command=entry_fun)
my_button3.pack()

#creating a closing button
def button_destroy():
    win.destroy()


#styling button    
my_button2=tk.Button(win,text="Destroy",font=('ariel',25),command=button_destroy,fg="white",bg="black",activebackground="white",activeforeground="black",padx=23,pady=23)
my_button2.pack(side="bottom")



#initilazing loop
win.mainloop()
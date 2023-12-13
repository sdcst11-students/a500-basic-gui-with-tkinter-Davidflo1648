import tkinter as tk
from tkinter.constants import LEFT

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

nF1=tk.Frame()

dogPic=tk.PhotoImage(file="dog.png")
flabel1=tk.Label(window,image=dogPic)
flabel2=tk.Label(window,text="Client Database")
fbutton1=tk.Button(window,text="Search By Name")
fentry1=tk.Entry(window,width=18)

nF2=tk.Frame()

flabel3=tk.Label(window,text="Name")
flabel4=tk.Label(window,text="Type")
flabel5=tk.Label(window,text="Breed")
flabel6=tk.Label(window,text="Owner")
flabel7=tk.Label(window,text="Birthdate")

nF3=tk.Frame()

fentry2=tk.Entry(window,width=10)
fentry3=tk.Entry(window,width=10)
fentry4=tk.Entry(window,width=10)
fentry5=tk.Entry(window,width=10)
fentry6=tk.Entry(window,width=10)

nF4=tk.Frame()

fbutton2=tk.Button(window,text="< Previous")
fbutton3=tk.Button(window,text="Next >")

nF1.grid()
flabel1.grid(row=0,column=0,columnspan=3)
flabel2.grid(row=1,column=3)
fbutton1.grid(row=0,column=4)
fentry1.grid(row=0,column=5)

nF2.grid()
flabel3.grid(row=5,column=1)
flabel4.grid(row=5,column=2)
flabel5.grid(row=5,column=3)
flabel6.grid(row=5,column=4)
flabel7.grid(row=5,column=5)

nF3.grid()
fentry2.grid(row=6,column=1)
fentry3.grid(row=6,column=2)
fentry4.grid(row=6,column=3)
fentry5.grid(row=6,column=4)
fentry6.grid(row=6,column=5)

nF4.grid()
fbutton2.grid(row=7,column=1)
fbutton3.grid(row=7,column=5)

window.mainloop()
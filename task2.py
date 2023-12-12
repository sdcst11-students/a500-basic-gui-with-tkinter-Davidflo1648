import tkinter as tk
from tkinter.constants import LEFT

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

nF1=tk.Frame()

dogPic=tk.PhotoImage(file="dog.png")
flabel1=tk.Label(window,image=dogPic)
flabel2=tk.Label(window,text="Client Database")
fbutton1=tk.Button(window,text="Search By Name")
fentry1=tk.Entry(window,text="Entry widgets can be typed in",width=10)

nF1.grid()
flabel1.grid(row=1,column=1,columnspan=3)
flabel2.grid(row=2,column=3)

window.mainloop()
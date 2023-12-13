import tkinter as tk

window=tk.Tk()
window.title('Example')
window.geometry('260x134')

dogPic=tk.PhotoImage(file="dog.png")
flabel1=tk.Label(window,image=dogPic)
flabel2=tk.Label(window,text='Pochacco!')
flabel3=tk.Label(window,text='A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero',background='#aaffff')

flabel1.grid(row=1,column=2)
flabel2.grid(row=1,column=3)
flabel3.grid(row=4,rowspan=2,column=1,columnspan=4)

window.mainloop()
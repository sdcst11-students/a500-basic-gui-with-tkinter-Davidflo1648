import tkinter as tk

window=tk.Tk()
window.title('Example')
window.geometry('260x134')

dogPic=tk.PhotoImage(file="dog.png")
flabel1=tk.Label(window,image=dogPic)
flabel2=tk.Label(window,text='Pochacco!')
flabel3=tk.Label(window,text='A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero',background='#aaffff')

flabel1.place(x=75,y=50)
flabel2.place(x=100,y=50)
flabel3.place()

window.mainloop()
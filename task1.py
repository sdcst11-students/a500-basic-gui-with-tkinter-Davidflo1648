import tkinter as tk
from tkinter.constants import LEFT

window = tk.Tk()
window.title("tk")
window.geometry("300x100")

nF = tk.Frame()

fEntry1 = tk.Entry(window,text="Entry widgets can be typed in",width=10)
fLabel1 = tk.Label(window,text="x")
fEntry2 = tk.Entry(window,text="Entry widgets can be typed in",width=10)
fLabel2 = tk.Label(window,text="=")
fEntry3 = tk.Entry(window,text="Entry widgets can be typed in",width=30)

nF.pack()
fEntry1.pack(side=LEFT)
fLabel1.pack(side=LEFT)
fEntry2.pack(side=LEFT)
fLabel2.pack(side=LEFT)
fEntry3.pack(side=LEFT)

window.mainloop()
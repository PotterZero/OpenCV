import tkinter as tk
from tkinter import *
import cv2

def endtask():
    # Window and title
    window = Tk()
    window.title("End Task")
    window.attributes('-topmost', True)
    window.geometry("750x100+200+400")

    # Content
    lbl = Label(window, text="Da nhan dien thanh cong", fg="black", font=("Time New Roman", 50))
    lbl.grid(column=0, row=0)

    # Button
    End_button = Button(window, text="Ket thuc", width=20, command=window.destroy)
    End_button.grid(column=0, row=1)

    window.mainloop()

# Call the endtask function
endtask()

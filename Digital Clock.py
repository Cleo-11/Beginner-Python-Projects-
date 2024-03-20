# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:08:10 2024

@author: cleon
"""

#Creating a Digital Clock with Python 

#We start with importing the libraries tkinter and time
from tkinter import Label, Tk
import time 

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("320x50")
app_window.resizable(1,1)

text_font=("Arial", 40,'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 100 

label = Label(app_window, font=text_font, bg = background, fg=foreground, bd = border_width)
label.grid(row = 0, column = 1)


def digital_clock(): 
  time_live = time.strftime("%H:%M:%S")
  label.config(text = time_live)
  label.after(200, digital_clock)
  
digital_clock()

app_window.mainloop()
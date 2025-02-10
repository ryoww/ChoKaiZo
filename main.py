import customtkinter as ctk
import tkinter as tk
from PIL import Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.geometry('800x600')
app.title('ChoKaiZo')

tabview = ctk.CTkTabview(app)

app.mainloop()